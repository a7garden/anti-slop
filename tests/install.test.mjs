import test from "node:test";
import assert from "node:assert/strict";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, renameSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { installSkill, parseArgs, selectTargets, skillVersion } from "../bin/install.mjs";

function fixture(fn) {
  const root = mkdtempSync(join(tmpdir(), "anti-slop-install-test-"));
  try { fn(root); } finally { rmSync(root, { recursive: true, force: true }); }
}
function sourceAt(root) {
  const source = join(root, "source");
  mkdirSync(source);
  writeFileSync(join(source, "SKILL.md"), '---\nname: anti-slop\nmetadata:\n  version: "2.0.0"\n---\n');
  return source;
}

test("rejects runtime words, unknown flags and missing --dir values before installation", () => {
  for (const args of [["audit", "sample.md", "--list"], ["--unknown"], ["--dir"], ["--dir", "--uninstall"]]) {
    assert.throws(() => parseArgs(args));
  }
  const result = spawnSync(process.execPath, ["bin/install.mjs", "audit", "sample.md", "--list"], { encoding: "utf8" });
  assert.equal(result.status, 1);
});

test("npm-style symlink entrypoints execute the installer", () => fixture((root) => {
  const alias = join(root, "anti-slop");
  symlinkSync(fileURLToPath(new URL("../bin/install.mjs", import.meta.url)), alias);
  const result = spawnSync(process.execPath, [alias, "--version"], { encoding: "utf8" });
  assert.equal(result.status, 0);
  const pkg = JSON.parse(readFileSync(new URL("../package.json", import.meta.url), "utf8"));
  assert.equal(result.stdout.trim(), pkg.version);
}));

test("explicit targets are isolated and --list has no filesystem side effects", () => fixture((root) => {
  const target = join(root, "explicit");
  assert.deepEqual(selectTargets(parseArgs(["--dir", target]), root), [target]);
  assert.deepEqual(selectTargets(parseArgs(["--dir", target, "--codex"]), root), [target, join(root, ".codex", "skills")]);
  const result = spawnSync(process.execPath, ["bin/install.mjs", "--dir", target, "--list"], { encoding: "utf8" });
  assert.equal(result.status, 0);
  assert.equal(existsSync(target), false);
}));

test("updates replace obsolete instructions while preserving all old files in a backup", () => fixture((root) => {
  const source = sourceAt(root);
  const base = join(root, "skills");
  const initial = installSkill(source, base);
  assert.equal(initial.backup, null);
  writeFileSync(join(initial.dest, "obsolete.md"), "old instructions");
  writeFileSync(join(initial.dest, "custom.txt"), "user customization");
  const updated = installSkill(source, base);
  assert.equal(existsSync(join(updated.dest, "obsolete.md")), false);
  assert.equal(existsSync(join(updated.dest, "custom.txt")), false);
  assert.equal(readFileSync(join(updated.backup, "custom.txt"), "utf8"), "user customization");
  assert.equal(readFileSync(join(updated.backup, "obsolete.md"), "utf8"), "old instructions");
  assert.equal(skillVersion(updated.dest), "2.0.0");
  assert.deepEqual(readdirSync(base), ["anti-slop"]);
}));

test("failed replacement restores the old active copy", () => fixture((root) => {
  const source = sourceAt(root);
  const base = join(root, "skills");
  const { dest } = installSkill(source, base);
  writeFileSync(join(dest, "keep.txt"), "recover me");
  let calls = 0;
  assert.throws(() => installSkill(source, base, { renameSync(from, to) {
    calls++;
    if (calls === 2) throw new Error("simulated disk failure");
    renameSync(from, to);
  } }));
  assert.equal(readFileSync(join(dest, "keep.txt"), "utf8"), "recover me");
  assert.deepEqual(readdirSync(base), ["anti-slop"]);
}));

test("refuses symlink targets and identical source/destination", () => fixture((root) => {
  const source = sourceAt(root);
  const base = join(root, "skills");
  mkdirSync(base);
  symlinkSync(source, join(base, "anti-slop"), "dir");
  assert.throws(() => installSkill(source, base));
  assert.equal(existsSync(join(source, "SKILL.md")), true);
  rmSync(join(base, "anti-slop"));
  installSkill(source, base);
  assert.throws(() => installSkill(join(base, "anti-slop"), base));
}));

test("refuses nested or aliased source targets and dangling symlinks", () => fixture((root) => {
  const source = sourceAt(root);
  assert.throws(() => installSkill(source, source));
  const alias = join(root, "alias");
  symlinkSync(source, alias, "dir");
  assert.throws(() => installSkill(source, alias));
  const base = join(root, "skills");
  mkdirSync(base);
  symlinkSync(join(root, "missing"), join(base, "anti-slop"), "dir");
  assert.throws(() => installSkill(source, base));
}));
