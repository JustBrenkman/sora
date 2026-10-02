# sora

Monorepo of drone projects. Each project under `projects/<name>/` may contain
`specs/`, `hardware/`, `firmware/`, `linux/` and `cad/`; a project only has the
folders it needs. Each project has its own `AGENTS.md` with board-specific facts.

## Rules

- **Never vendor upstream source.** PX4, the kernel, U-Boot and Armbian are
  checked out by scripts into gitignored `build/` folders. Only board files,
  patches and pinned versions are committed.
- **Never commit vendor PDFs.** Add them to the project's `specs/sources.yaml`;
  `specs/reference/` is gitignored.
- **Do not hand-edit KiCad files** (`.kicad_sch`, `.kicad_pcb`, `.kicad_pro`,
  library tables). They are edited in KiCad. Do not generate new KiCad projects.
- **`lib/kicad` is a submodule** (JustBrenkman/kicad-lib). Change parts in that
  repository, then bump the submodule here.
- **CAD binaries go through Git LFS** (see `.gitattributes`).
- **Pin assignments come from `specs/pinout/`.** Firmware and device trees
  follow it, not the other way round.

## Naming

Projects are named after bird anatomy; see `NAMING.md`. The name is reused as
the PX4 target (`sora_<name>`) and in the device tree filename.

## Licensing

| Path                 | SPDX identifier  |
| -------------------- | ---------------- |
| `hardware/`, `cad/`  | CERN-OHL-P-2.0   |
| `firmware/`          | BSD-3-Clause     |
| `linux/`             | GPL-2.0-only     |
| `specs/`, docs       | CC-BY-4.0        |

New source files carry the matching `SPDX-License-Identifier` header.

## Commits

- Commit messages are a single line, with no body.
- Do not add AI attribution: no `Co-Authored-By` trailer and no
  "generated with" line.
- Do not commit unless asked.
