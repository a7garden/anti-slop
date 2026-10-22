"""Synthetic protocol tests for the runner, never model-quality evidence."""
import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from run_behavior import execute


class FakeServer:
    """Minimal in-memory JSONL peer with real client tool-output handling."""
    def __init__(self, read_path=None):
        self.stdout = self
        self.stdin = self
        self.returncode = None
        self.queue = asyncio.Queue()
        self.requests = []
        self.turn = 0
        self.read_path = read_path
        self.tool_results = []

    def emit(self, message):
        self.queue.put_nowait((json.dumps(message) + '\n').encode())

    def complete(self):
        text = 'Synthetic response for turn ' + str(self.turn)
        self.emit({'method': 'item/completed', 'params': {'item': {
            'type': 'agentMessage', 'phase': 'final_answer', 'text': text}}})
        self.emit({'method': 'turn/completed', 'params': {'turn': {
            'id': 'turn-' + str(self.turn), 'status': 'completed'}}})

    def write(self, data):
        message = json.loads(data)
        self.requests.append(message)
        method, identifier = message.get('method'), message.get('id')
        if method == 'initialize':
            self.emit({'id': identifier, 'result': {'userAgent': 'synthetic-unit-test'}})
        elif method == 'thread/start':
            self.emit({'id': identifier, 'result': {'thread': {'id': 'synthetic-thread'},
                       'model': 'synthetic', 'reasoningEffort': 'synthetic'}})
        elif method == 'turn/start':
            self.turn += 1
            self.emit({'id': identifier, 'result': {'turn': {'id': 'turn-' + str(self.turn)}}})
            if self.read_path is not None:
                self.emit({'id': 'tool-' + str(self.turn), 'method': 'item/tool/call',
                           'params': {'tool': 'read_file', 'arguments': {'path': self.read_path}}})
            else:
                self.complete()
        elif isinstance(identifier, str) and identifier.startswith('tool-'):
            self.tool_results.append(message['result'])
            self.complete()

    async def readline(self):
        return await self.queue.get()

    async def drain(self):
        pass

    def terminate(self):
        self.returncode = 0

    def kill(self):
        self.returncode = -9

    async def wait(self):
        return self.returncode


class RunnerTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        snapshot = self.root / 'snapshot'
        project = snapshot / 'tests/fixtures/project-context'
        project.mkdir(parents=True)
        (project / 'README.md').write_text('Known synthetic project source.\n')
        self.args = SimpleNamespace(output=self.root/'output', workspace=self.root/'workspaces',
                                    snapshot=snapshot, timeout=1,
                                    manifest={'skill_digest': 'synthetic-digest'})

    async def run_peer(self, peer, case):
        async def launch(*args, **kwargs):
            return peer
        with patch('run_behavior.asyncio.create_subprocess_exec', new=launch):
            return await execute(case, 1, self.args, 'Synthetic runtime instructions only.')

    async def test_real_turn_boundaries_and_evidence_are_preserved(self):
        peer = FakeServer()
        case = {'id': 'continuation', 'context': 'Response-only synthetic test.',
                'turns': ['First actual user turn.', 'Second actual user turn.']}
        result = await self.run_peer(peer, case)
        self.assertEqual(result['status'], 'completed')
        starts = [m['params'] for m in peer.requests if m.get('method') == 'turn/start']
        self.assertEqual([p['threadId'] for p in starts], ['synthetic-thread'] * 2)
        self.assertEqual([p['input'][0]['text'] for p in starts], case['turns'])
        self.assertEqual([m['turn'] for m in result['outputs']], [1, 2])
        trace = (self.args.output/'runs/continuation-1/trace.txt').read_text()
        self.assertIn('Second actual user turn.', trace)
        self.assertIn('Synthetic response for turn 2', trace)
        self.assertIn('WORKSPACE HASHES UNCHANGED', trace)
        self.assertTrue(result['trace_sha256'])
        self.assertTrue(result['protocol_sha256'])
        thread = next(m['params'] for m in peer.requests if m.get('method') == 'thread/start')
        self.assertEqual(thread['dynamicTools'], [])
        self.assertEqual(thread['environments'], [])

    async def test_project_reads_are_real_and_cannot_escape_fixture(self):
        case = {'id': 'project', 'context': 'Read tests/fixtures/project-context only.',
                'turns': ['Read the source.']}
        peer = FakeServer('README.md')
        result = await self.run_peer(peer, case)
        self.assertTrue(result['tool_events'][0]['success'])
        self.assertEqual(peer.tool_results[0]['contentItems'][0]['text'],
                         'Known synthetic project source.\n')
        outside = self.root/'outside.txt'
        outside.write_text('must not appear in tool output')
        peer = FakeServer(str(outside))
        case['id'] = 'outside'
        result = await self.run_peer(peer, case)
        self.assertFalse(result['tool_events'][0]['success'])
        self.assertNotIn('must not appear', peer.tool_results[0]['contentItems'][0]['text'])
        self.assertTrue(result['workspace_unchanged'])

    async def test_unavailable_tool_does_not_gain_project_access(self):
        peer = FakeServer('README.md')
        result = await self.run_peer(peer, {'id': 'restricted', 'context': 'Response-only.',
                                           'turns': ['Hello.']})
        self.assertFalse(result['tool_events'][0]['success'])
        self.assertIn('unavailable', peer.tool_results[0]['contentItems'][0]['text'])


if __name__ == '__main__':
    unittest.main()
