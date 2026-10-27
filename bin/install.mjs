#!/usr/bin/env node
/** Installs the skill. Runtime operations belong in the agent conversation. */
import { cpSync, existsSync, lstatSync, mkdirSync, mkdtempSync, readFileSync, realpathSync, renameSync, rmSync, statSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, isAbsolute, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const SOURCE = join(ROOT, ".agents", "skills", "anti-slop");
const pkg = JSON.parse(readFileSync(join(ROOT, "package.json"), "utf8"));
const FLAGS = new Set(["--omp", "--codex", "--all", "--list", "--uninstall", "-h", "--help", "-v", "--version"]);

export function parseArgs(args) {
  const flags = new Set();
  const dirs = [];
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    // npm/npx may forward a standalone option separator.
    if (arg === "--") continue;
    if (arg === "--dir") {
      const value = args[++i];
      if (!value || value.startsWith("-")) throw new Error("--dir requires a path; use ./ for paths beginning with '-'.");
      dirs.push(resolve(value));
    } else if (FLAGS.has(arg)) {
      flags.add(arg);
    } else {
      throw new Error(`Unknown installer argument: ${arg}. To audit, revise, or draft, use $anti-slop in your agent conversation. See --help.`);
    }
  }
  return { flags, dirs };
}

export function selectTargets({ flags, dirs }, home = homedir()) {
  const skills = (base) => join(home, base, "skills");
  const targets = [...dirs];
  if (flags.has("--omp") || flags.has("--all")) targets.push(skills(".agents"));
  if (flags.has("--codex") || flags.has("--all")) targets.push(skills(".codex"));
  // Explicit --dir is isolated unless known harness targets were also selected.
  if (!targets.length) {
    for (const base of [".agents", ".codex"]) {
      if (existsSync(skills(base))) targets.push(skills(base));
    }
    if (!targets.length) targets.push(skills(".agents"));
  }
  return [...new Set(targets)];
}

export function skillVersion(dir) {
  try {
    const text = readFileSync(join(dir, "SKILL.md"), "utf8");
    const frontmatter = text.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/)?.[1];
    const version = frontmatter?.match(/^  version:\s*["']?([^\s"']+)["']?\s*$/m)
      ?? frontmatter?.match(/^version:\s*["']?([^\s"']+)["']?\s*$/m);
    return version?.[1] ?? "unknown";
  } catch {
    return null;
  }
}

export function installSkill(source, base, fsOps = { renameSync }) {
  const dest = join(base, "anti-slop");
  const entry = lstatSync(dest, { throwIfNoEntry: false });
  if (entry && (entry.isSymbolicLink() || !entry.isDirectory())) {
    throw new Error(`Refusing to replace a symlink or non-directory: ${dest}`);
  }
  const inside = (parent, child) => {
    const rel = relative(parent, child);
    return rel === "" || (!rel.startsWith("../") && rel !== ".." && !isAbsolute(rel));
  };
  const refuseOverlap = (src, target) => {
    if (inside(src, target) || inside(target, src)) throw new Error("Source and installation target overlap (including the same directory).");
  };
  refuseOverlap(resolve(source), resolve(dest));
  mkdirSync(base, { recursive: true });
  refuseOverlap(realpathSync(source), join(realpathSync(base), "anti-slop"));
  const stage = mkdtempSync(join(base, ".anti-slop-stage-"));
  const staged = join(stage, "anti-slop");
  let backup = null;
  let movedOld = false;
  try {
    cpSync(source, staged, { recursive: true });
    if (!statSync(join(staged, "SKILL.md")).isFile()) throw new Error("Staged skill lacks SKILL.md.");
    if (existsSync(dest)) {
      const backupBase = join(dirname(base), "anti-slop-backups");
      mkdirSync(backupBase, { recursive: true });
      backup = join(mkdtempSync(join(backupBase, "update-")), "anti-slop");
      fsOps.renameSync(dest, backup);
      movedOld = true;
    }
    try {
      fsOps.renameSync(staged, dest);
    } catch (err) {
      if (movedOld) {
        try { fsOps.renameSync(backup, dest); }
        catch (restoreError) {
          throw new Error(`Install failed (${err.message}); restore failed (${restoreError.message}). Previous copy retained at ${backup}.`);
        }
      }
      throw err;
    }
    return { dest, backup };
  } finally {
    rmSync(stage, { recursive: true, force: true });
  }
}

export function main(args = process.argv.slice(2)) {
  const parsed = parseArgs(args); // Reject invalid arguments before any filesystem mutation.
  const has = (flag) => parsed.flags.has(flag);
  if (has("-h") || has("--help")) {
    console.log(`anti-slop installer v${pkg.version}

This executable installs the skill. Run $anti-slop audit/revise/draft in an agent conversation.

With no target option, detect ~/.agents/skills and ~/.codex/skills.
If neither exists, use ~/.agents/skills.

Options:
  --omp          select ~/.agents/skills
  --codex        select ~/.codex/skills
  --all          select both known directories
  --dir <path>   select only <path>/anti-slop (repeatable; combine with other targets)
  --list         show targets without creating or installing anything
  --uninstall    remove active copies; update backups are retained
  -h, --help     this help
  -v, --version  print version

Updates stage a fresh copy and move the old folder to ../anti-slop-backups.
Obsolete files leave the active skill; custom files remain recoverable in the backup.`);
    return;
  }
  if (has("-v") || has("--version")) { console.log(pkg.version); return; }
  const targets = selectTargets(parsed);
  if (has("--list")) {
    console.log(`anti-slop v${pkg.version} would ${has("--uninstall") ? "remove" : "install"}:`);
    for (const base of targets) console.log(`  ${join(base, "anti-slop")}`);
    return;
  }
  if (!has("--uninstall") && !existsSync(join(SOURCE, "SKILL.md"))) throw new Error(`Skill source missing: ${SOURCE}`);
  for (const base of targets) {
    const dest = join(base, "anti-slop");
    if (has("--uninstall")) {
      if (existsSync(dest)) { rmSync(dest, { recursive: true, force: true }); console.log(`removed  ${dest}`); }
      else console.log(`absent   ${dest}`);
      continue;
    }
    const previous = skillVersion(dest);
    const installed = installSkill(SOURCE, base);
    console.log(`installed ${skillVersion(dest)}${previous ? ` (was ${previous})` : " (new install)"} -> ${dest}`);
    if (installed.backup) console.log(`backup    ${installed.backup}`);
  }
}

if (process.argv[1] && existsSync(process.argv[1]) && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { main(); } catch (err) { console.error(`FAIL: ${err.message}`); process.exitCode = 1; }
}
