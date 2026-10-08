#!/usr/bin/env node
/**
 * anti-slop skill installer.
 * Copies the self-contained skill folder into the skill directories of
 * agent harnesses that follow the `.agents/skills/` convention.
 *
 * Usage:
 *   npx github:a7garden/anti-slop            install/update (auto-detected targets)
 *   npx github:a7garden/anti-slop -- --omp   only the omp skills dir
 *   npx github:a7garden/anti-slop -- --codex only the codex skills dir
 *   npx github:a7garden/anti-slop -- --dir <path>  also install into <path>/anti-slop
 *   npx github:a7garden/anti-slop -- --all   force both known dirs (create if missing)
 *   npx github:a7garden/anti-slop -- --list  show targets without installing
 *   npx github:a7garden/anti-slop -- --uninstall   remove installed copies
 *
 * Update: re-run the same command. The copy is replaced with the latest version.
 */
import { cpSync, existsSync, mkdirSync, rmSync, statSync } from "node:fs";
import { homedir } from "node:os";
import { createRequire } from "node:module";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const pkg = require("../package.json");
const SOURCE = resolve(dirname(fileURLToPath(import.meta.url)), "..", ".agents", "skills", "anti-slop");

const args = process.argv.slice(2);
const has = (flag) => args.includes(flag);
const dirArgs = [...args.entries()].filter(([, v]) => v === "--dir").map(([i]) => args[i + 1]).filter(Boolean);

if (has("-h") || has("--help")) {
  console.log(`anti-slop installer v${pkg.version}

Installs the anti-slop skill (rules, language profiles, examples, tests) into
agent skill directories following the .agents/skills/ convention.

Targets are auto-detected: ~/.agents/skills (omp) and ~/.codex/skills (codex).
If none exists, ~/.agents/skills is created.

Options:
  --omp          install only into ~/.agents/skills
  --codex        install only into ~/.codex/skills
  --all          force both known dirs (create if missing)
  --dir <path>   additionally install into <path>/anti-slop (repeatable)
  --list         show targets without installing
  --uninstall    remove installed copies from the targets
  -h, --help     this help
  -v, --version  print version

Update: re-run the same npx command; the installed copy is replaced.
`);
  process.exit(0);
}
if (has("-v") || has("--version")) {
  console.log(pkg.version);
  process.exit(0);
}

if (!existsSync(join(SOURCE, "SKILL.md"))) {
  console.error(`FAIL: skill folder not found at ${SOURCE}; the package looks broken.`);
  process.exit(1);
}

const skills = (base) => join(homedir(), base, "skills");
const candidates = [];
if (has("--omp") || has("--all")) candidates.push([skills(".agents"), true]);
if (has("--codex") || has("--all")) candidates.push([skills(".codex"), true]);
if (!candidates.length) {
  for (const base of [".agents", ".codex"]) {
    if (existsSync(skills(base))) candidates.push([skills(base), false]);
  }
  if (!candidates.length) candidates.push([skills(".agents"), true]);
}
for (const dir of dirArgs) candidates.push([resolve(dir), true]);

const targets = [
  ...new Map(
    candidates.map(([dir, create]) => {
      if (!existsSync(dir)) {
        if (!create) return [dir, null];
        try {
          mkdirSync(dir, { recursive: true });
        } catch (err) {
          console.error(`FAIL: cannot create ${dir}: ${err.message}`);
          process.exit(1);
        }
      }
      return [dir, dir];
    }),
  ).values(),
].filter(Boolean);

const installDirOf = (dir) => join(dir, "anti-slop");

if (has("--list")) {
  console.log(`anti-slop v${pkg.version} would install to:`);
  for (const dir of targets) console.log(`  ${installDirOf(dir)}`);
  process.exit(0);
}

for (const dir of targets) {
  const dest = installDirOf(dir);
  if (has("--uninstall")) {
    if (existsSync(dest)) {
      rmSync(dest, { recursive: true, force: true });
      console.log(`removed  ${dest}`);
    } else {
      console.log(`absent   ${dest}`);
    }
    continue;
  }
  cpSync(SOURCE, dest, { recursive: true });
  const info = statSync(join(dest, "SKILL.md"));
  if (!info.isFile()) {
    console.error(`FAIL: ${dest} did not receive SKILL.md`);
    process.exit(1);
  }
  console.log(`installed ${pkg.version} -> ${dest}`);
}

if (!has("--uninstall")) {
  console.log(`\nUpdate later by re-running the same command.`);
}
