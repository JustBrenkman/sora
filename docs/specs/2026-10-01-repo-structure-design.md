# Repository structure

Date: 2026-10-01

## Purpose

Sora is a monorepo for drone projects. A project may contain CAD models,
hardware, firmware, Linux board support, or any combination. The first project,
pinion, is an AM62L single board computer with an integrated STM32H743 flight
controller derived from the Pixhawk FMUv6C.

## Decisions

| Topic                 | Decision                                                                 | Reason                                                              |
| --------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Top-level layout      | Project-first: `projects/<name>/{specs,hardware,firmware,linux,cad}`     | Projects are self-contained; shared items stay at the root          |
| Upstream source trees | Overlay only; scripts check out PX4, kernel, U-Boot, Armbian at a pinned version | Keeps the repo small and makes upstream bumps explicit        |
| Reference documents   | Manifest (`sources.yaml`) plus `fetch.sh`; downloads are gitignored      | Vendor datasheets are not redistributable; the repo is to be public |
| KiCad libraries       | `JustBrenkman/kicad-lib` as a submodule at `lib/kicad`                   | One library across repos, pinned per commit, clean fresh clones     |
| Hardware layout       | One folder per board under `hardware/`; main board plus accessories      | Accessory boards are expected                                       |
| Linux layout          | Shared `dts/`, `kernel/`, `u-boot/`; one thin folder per distro          | The device tree is written once, whichever distro is built          |
| Project names         | Bird anatomy; first project is `pinion`                                  | See `NAMING.md`                                                     |
| CAD storage           | `cad/` per project; Git LFS for binary formats                           | Binary models must not bloat history                                |
| Licensing             | CERN-OHL-P-2.0 hardware and CAD, BSD-3-Clause firmware, GPL-2.0-only linux, CC-BY-4.0 specs and docs | Matches the upstream each part derives from |
| Agent context files   | `AGENTS.md` at the root and per project; `CLAUDE.md` imports it          | One source for every agent tool                                     |

## Not included

CI, root-level `tools/`, KiCad project files, PX4 board files, device trees and
any remote. They are added when there is content for them.
