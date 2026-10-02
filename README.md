# sora

Sora (空, "sky") is a monorepo of drone projects. Each project may contain CAD
models, hardware, firmware, Linux board support, or any combination of them.

## Projects

| Project                      | Description                                                                 |
| ---------------------------- | --------------------------------------------------------------------------- |
| [pinion](projects/pinion/)   | Single board computer: TI AM62L with an integrated STM32H7 flight controller based on the Pixhawk FMUv6C |

New projects are named after bird anatomy; see [NAMING.md](NAMING.md).

## Layout

```
sora/
├── lib/kicad/          # submodule: shared KiCad symbols, footprints, 3D models
├── LICENSES/           # full licence texts
├── docs/specs/         # design records for the repo itself
└── projects/<name>/
    ├── specs/          # reference documents, pin maps, diagrams, notes
    ├── hardware/       # KiCad projects, one folder per board
    ├── firmware/       # board files overlaid onto upstream firmware
    ├── linux/          # device trees, kernel and bootloader config, distro builds
    └── cad/            # mechanical models
```

A project only has the folders it needs.

## Cloning

```sh
git clone --recurse-submodules <url>
git lfs install   # once per machine; CAD binaries are stored with Git LFS
```

## Conventions

- **Overlay, not vendoring.** Upstream trees (PX4, the kernel, U-Boot, Armbian)
  are never committed. Projects hold only their own board files, patches and a
  pinned upstream version; scripts check the upstream out into a gitignored
  `build/` folder.
- **Reference documents are fetched, not committed.** Each project's
  `specs/sources.yaml` lists them and `specs/fetch.sh` downloads them.

## Licensing

| Path                                   | Licence                                    |
| -------------------------------------- | ------------------------------------------ |
| `projects/*/hardware/`, `projects/*/cad/` | [CERN-OHL-P-2.0](LICENSES/CERN-OHL-P-2.0.txt) |
| `projects/*/firmware/`                 | [BSD-3-Clause](LICENSES/BSD-3-Clause.txt)  |
| `projects/*/linux/`                    | [GPL-2.0-only](LICENSES/GPL-2.0-only.txt)  |
| `projects/*/specs/`, all documentation | [CC-BY-4.0](LICENSES/CC-BY-4.0.txt)        |

`lib/kicad` is a separate repository with its own terms.

Copyright © 2026 Ben Brenkman.
