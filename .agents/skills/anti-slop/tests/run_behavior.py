#!/usr/bin/env python3
"""Execute prepared blind cases through ephemeral Codex app-server threads.

This runs models. It never reads expected checks, scores outputs, or fakes tool results.
The app-server JSONL transcript and normalized messages are preserved per execution.
"""
from __future__ import annotations
import argparse
import asyncio
import hashlib
import json
import shutil
import subprocess
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from evaluate_behavior import skill_digest

RUNTIME_REFERENCES = (
    'quality-framework.md', 'execution-contract.md', 'editorial-method.md',
    'writing-profile.md', 'english-profile.md', 'design-profile.md',
    'visual-style.md', 'domain-research.md', 'browser-audit.md',
    'finding-evidence.md', 'rules.md',
)
CONFIG = {
    'features.apps': False, 'features.plugins': False,
    'features.shell_tool': False, 'features.multi_agent': False,
    'features.skill_search': False, 'web_search': 'disabled',
}


def digest_files(root: Path) -> dict:
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file()}


def runtime_pack(snapshot: Path) -> str:
    paths = [snapshot / 'SKILL.md', *(snapshot / 'references' / n for n in RUNTIME_REFERENCES)]
    return '\n\n'.join('## Loaded runtime source: ' + str(p.relative_to(snapshot)) + '\n' + p.read_text()
                       for p in paths)


async def execute(case: dict, repetition: int, args, pack: str) -> dict:
    run_id = str(uuid.uuid4())
    label = f"{case['id']}-{repetition}"
    directory = args.output / 'runs' / label
    directory.mkdir(parents=True, exist_ok=False)
    workspace = args.workspace / label
    workspace.mkdir(parents=True, exist_ok=False)
    project = workspace / 'project'
    has_project = 'tests/fixtures/project-context' in case['context']
    if has_project:
        shutil.copytree(args.snapshot / 'tests/fixtures/project-context', project)
    before = digest_files(workspace)
    (directory / 'before.json').write_text(json.dumps(before, indent=2) + '\n')
    raw = (directory / 'protocol.jsonl').open('w')
    trace = (directory / 'trace.txt').open('w')
    stderr = (directory / 'server-stderr.txt').open('w')
    request_id = 0
    completed = {}
    outputs = []
    tool_events = []
    current_turn = 0
    started_at = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    base = ('The following anti-slop runtime sources are already loaded. Apply only the modules relevant '
            'to the actual task. This is a runtime execution, not skill maintenance. '
            'There are no browser, network, shell, write, or user-question-UI capabilities. '
            'Use text choices if a question is necessary. Do not claim an action that was not performed.\n\n')
    environment = '\n\n## Actual case environment\n' + case['context']
    if has_project:
        environment += ('\nThe current project root is ' + str(project) + '. '
                        'The read_file tool is available only for that actual read-only fixture. '
                        'A path of . lists its files; other paths read UTF-8 files. '
                        'All runtime skill sources are already loaded above. No other filesystem is accessible.')
    else:
        environment += '\nThis is a response-only environment. No tools are exposed.'
    instructions = base + pack + environment
    tools = []
    if has_project:
        tools = [{'type': 'function', 'name': 'read_file',
                  'description': 'Read the current isolated project source snapshot; use . to list files. Read-only, no network. Paths are relative to the current project.',
                  'inputSchema': {'type': 'object', 'properties': {'path': {'type': 'string'}},
                                  'required': ['path'], 'additionalProperties': False}}]
    command = ['codex', 'app-server', '--stdio']
    for key, value in CONFIG.items():
        command += ['-c', key + '=' + json.dumps(value)]
    proc = None
    metadata = {'case_id': case['id'], 'repetition': repetition, 'run_id': run_id,
                'skill_digest': args.manifest['skill_digest'], 'executed_at': started_at,
                'case_context': case['context'], 'runtime_references': list(RUNTIME_REFERENCES),
                'tool_policy': 'project read_file only' if has_project else 'response-only',
                'runtime_sources_preloaded': True}
    trace.write('EXECUTION ' + label + '\nRUN_ID ' + run_id + '\n')
    trace.write('CONTEXT\n' + case['context'] + '\n')
    trace.flush()

    def log(direction, message):
        raw.write(json.dumps({'direction': direction, 'at': datetime.now(timezone.utc).isoformat(),
                              'message': message}, ensure_ascii=False) + '\n')
        raw.flush()

    async def send(message):
        log('client', message)
        proc.stdin.write((json.dumps(message, ensure_ascii=False) + '\n').encode())
        await proc.stdin.drain()

    async def receive():
        line = await asyncio.wait_for(proc.stdout.readline(), timeout=args.timeout)
        if not line:
            raise RuntimeError('App server exited before a complete response')
        message = json.loads(line)
        log('server', message)
        method, params = message.get('method'), message.get('params', {})
        if method == 'item/tool/call' and 'id' in message:
            success = False
            try:
                if not has_project or params.get('tool') != 'read_file':
                    raise PermissionError('Tool is unavailable in this case')
                path = params['arguments']['path']
                prefix = 'tests/fixtures/project-context/'
                if path.startswith(prefix):
                    path = path[len(prefix):]
                candidate = (project / path).resolve()
                if candidate != project.resolve() and project.resolve() not in candidate.parents:
                    raise PermissionError('Path is outside the isolated source fixture')
                if candidate.is_dir():
                    body = '\n'.join(str(p.relative_to(project)) for p in sorted(candidate.rglob('*')) if p.is_file())
                else:
                    body = candidate.read_text()
                success = True
            except Exception as error:
                body = type(error).__name__ + ': ' + str(error)
            result = {'contentItems': [{'type': 'inputText', 'text': body}], 'success': success}
            tool_events.append({'turn': current_turn, 'arguments': params.get('arguments'),
                                'success': success, 'output': body})
            trace.write('TOOL read_file ' + json.dumps(params.get('arguments'), ensure_ascii=False) + '\n' + body + '\n')
            trace.flush()
            await send({'id': message['id'], 'result': result})
        elif method and 'id' in message:
            trace.write('UNSUPPORTED SERVER REQUEST ' + method + '\n')
            await send({'id': message['id'], 'error': {'code': -32601, 'message': 'Capability unavailable in this evaluation environment'}})
        elif method == 'item/completed':
            item = params['item']
            if item.get('type') == 'agentMessage':
                text = item.get('text', '')
                phase = item.get('phase') or 'unspecified'
                outputs.append({'turn': current_turn, 'phase': phase, 'text': text})
                trace.write('ASSISTANT ' + phase + '\n' + text + '\n')
                trace.flush()
            elif item.get('type') not in {'userMessage', 'reasoning', 'dynamicToolCall'}:
                trace.write('ITEM ' + json.dumps(item, ensure_ascii=False) + '\n')
                trace.flush()
        elif method == 'turn/completed':
            completed[params['turn']['id']] = params['turn']
            trace.write('TURN STATUS ' + params['turn']['status'] + '\n')
            trace.flush()
        elif method == 'error':
            trace.write('SERVER ERROR ' + json.dumps(params, ensure_ascii=False) + '\n')
            trace.flush()
        return message

    async def rpc(method, params):
        nonlocal request_id
        request_id += 1
        identifier = request_id
        await send({'id': identifier, 'method': method, 'params': params})
        while True:
            message = await receive()
            if message.get('id') == identifier and ('result' in message or 'error' in message):
                if 'error' in message:
                    raise RuntimeError(json.dumps(message['error']))
                return message['result']

    try:
        proc = await asyncio.create_subprocess_exec(*command, cwd=str(workspace), stdin=asyncio.subprocess.PIPE,
                                                    stdout=asyncio.subprocess.PIPE, stderr=stderr, limit=16*1024*1024)
        init = await rpc('initialize', {'clientInfo': {'name': 'anti_slop_eval', 'version': '1.0'},
                                        'capabilities': {'experimentalApi': True}})
        await send({'method': 'initialized', 'params': {}})
        thread = await rpc('thread/start', {'ephemeral': True, 'cwd': str(workspace), 'environments': [],
                                            'approvalPolicy': 'never', 'sandbox': 'read-only',
                                            'config': CONFIG, 'developerInstructions': instructions, 'dynamicTools': tools})
        metadata.update({k: thread.get(k) for k in ['model', 'modelProvider', 'reasoningEffort', 'serviceTier', 'sandbox', 'instructionSources']})
        metadata['thread_id'] = thread['thread']['id']
        metadata['harness'] = init['userAgent']
        trace.write('MODEL ' + str(metadata['model']) + ' EFFORT ' + str(metadata['reasoningEffort']) + '\n')
        trace.write('CAPABILITIES ' + metadata['tool_policy'] + '; environment access disabled; no mutation or network tools\n')
        for index, user_turn in enumerate(case['turns'], 1):
            current_turn = index
            trace.write('TURN ' + str(index) + ' USER\n' + user_turn + '\n')
            trace.flush()
            response = await rpc('turn/start', {'threadId': metadata['thread_id'],
                                                'input': [{'type': 'text', 'text': user_turn}]})
            turn_id = response['turn']['id']
            while turn_id not in completed:
                await receive()
            if completed[turn_id]['status'] != 'completed':
                raise RuntimeError('Turn did not complete: ' + json.dumps(completed[turn_id]))
        metadata['status'] = 'completed'
    except Exception as error:
        metadata['status'] = 'execution-error'
        metadata['error'] = type(error).__name__ + ': ' + str(error)
        trace.write('EXECUTION ERROR ' + metadata['error'] + '\n')
    finally:
        if proc and proc.returncode is None:
            proc.terminate()
            try:
                await asyncio.wait_for(proc.wait(), 10)
            except asyncio.TimeoutError:
                proc.kill()
                await proc.wait()
        after = digest_files(workspace)
        (directory / 'after.json').write_text(json.dumps(after, indent=2) + '\n')
        metadata['workspace_unchanged'] = before == after
        metadata['elapsed_seconds'] = round(time.monotonic() - started, 3)
        metadata['tool_events'] = tool_events
        metadata['outputs'] = outputs
        trace.write('WORKSPACE HASHES ' + ('UNCHANGED' if before == after else 'CHANGED') + '\n')
        trace.write('RUN ' + metadata['status'].upper() + '\n')
        trace.close(); raw.close(); stderr.close()
        metadata['trace_sha256'] = hashlib.sha256((directory/'trace.txt').read_bytes()).hexdigest()
        metadata['protocol_sha256'] = hashlib.sha256((directory/'protocol.jsonl').read_bytes()).hexdigest()
        (directory / 'execution.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
    return metadata


async def main(args):
    args.manifest = json.loads((args.inputs / 'run-manifest.json').read_text())
    if skill_digest(args.snapshot) != args.manifest['skill_digest']:
        raise ValueError('Frozen runtime snapshot differs from the prepared revision')
    cases = []
    for path in sorted(args.inputs.glob('*.json')):
        if path.name == 'run-manifest.json':
            continue
        case = json.loads(path.read_text())
        if set(case) != {'id', 'context', 'turns'}:
            raise ValueError('Executor inputs must be blind id/context/turns only')
        if not args.case or case['id'] in args.case:
            cases.append(case)
    args.output.mkdir(parents=True, exist_ok=True)
    args.workspace.mkdir(parents=True, exist_ok=True)
    pack = runtime_pack(args.snapshot)
    jobs = [(c, n) for c in cases for n in range(1, args.repetitions + 1)]
    gate = asyncio.Semaphore(args.concurrency)
    progress = []
    async def job(case, repetition):
        async with gate:
            result = await execute(case, repetition, args, pack)
            progress.append({'case_id': result['case_id'], 'repetition': repetition,
                             'status': result['status'], 'elapsed_seconds': result['elapsed_seconds']})
            (args.output / 'progress.json').write_text(json.dumps(progress, indent=2) + '\n')
            print(f"{len(progress)}/{len(jobs)} {result['case_id']} #{repetition}: {result['status']} ({result['elapsed_seconds']}s)", flush=True)
            return result
    results = await asyncio.gather(*(job(c, n) for c, n in jobs))
    summary = {'total': len(results), 'completed': sum(r['status']=='completed' for r in results),
               'errors': [{k:r.get(k) for k in ['case_id','repetition','error']} for r in results if r['status']!='completed'],
               'skill_digest': args.manifest['skill_digest'],
               'model_configurations': sorted(set((r.get('model',''),r.get('reasoningEffort','')) for r in results)),
               'limit': 'Executions are recorded, not automatically semantically scored. Runtime references were preloaded; no live browser/network/mutation tools were exposed.'}
    (args.output / 'execution-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary), flush=True)
    if summary['errors']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--concurrency', type=int, default=4)
    parser.add_argument('--repetitions', type=int, default=3)
    parser.add_argument('--case', action='append')
    parser.add_argument('--timeout', type=int, default=300)
    args = parser.parse_args()
    if not 1 <= args.concurrency <= 4 or args.repetitions < 1:
        parser.error('Use 1–4 concurrent executions and at least one repetition')
    asyncio.run(main(args))
