# pinion

Single board computer with an integrated flight controller, on one PCB:

- **Compute:** TI AM62L running Linux.
- **Flight controller:** STM32H743 running PX4, derived from the Pixhawk FMUv6C
  (PX4 board `px4/fmu-v6c`, which uses the STM32H743VI).

The repo-wide rules in the root `AGENTS.md` apply.

## Where things are

| Path                              | Contents                                                    |
| --------------------------------- | ----------------------------------------------------------- |
| `specs/sources.yaml`, `fetch.sh`  | Manifest and downloader for reference documents             |
| `specs/reference/`                | Downloaded documents; gitignored, may be empty              |
| `specs/pinout/`                   | pinmap pin maps; the source of truth for firmware, device tree and schematic |
| `specs/notes/`, `specs/diagrams/` | Decisions, reference inventory, block diagrams              |
| `hardware/pinion-main/SCHEMATIC_TODO.md` | What is left to draw, per part                       |
| `hardware/pinion-main/`           | KiCad project for the main board                            |
| `firmware/px4/boards/sora/pinion/`| PX4 board files, laid out as in the PX4 tree                |
| `firmware/PX4_VERSION`            | Pinned PX4 tag                                              |
| `linux/dts/`, `kernel/`, `u-boot/`| Distro-independent board support                            |
| `linux/armbian/`                  | Armbian build configuration that consumes the above         |
| `cad/`                            | Mechanical models (Git LFS)                                 |

## Facts to keep straight

- The reference design is the **FMUv6C**, not the v6X or v5X. When reading PX4
  sources, use `boards/px4/fmu-v6c` at the tag in `firmware/PX4_VERSION`.
- The PX4 target is `sora_pinion`; the vendor folder is `sora`, the model `pinion`.
- pinion is not pin-identical to the FMUv6C. Check `specs/pinout/` and
  `specs/notes/` for deviations before copying anything from the reference board.
- Run `specs/fetch.sh` before looking for reference documents.
- Pin maps are `pinmap` files (`*.pindef.json`, `*.pinasg.ron`). Change them with
  `pinmap assign`/`unassign`/`note --project specs/pinout/<fmu|io|soc>.pinasg.ron`,
  not by hand, then regenerate the `.md` pinouts; see `specs/pinout/README.md`.
  Do not introduce CSV or spreadsheet pin tables.
- The three processors are U1 (STM32H743, `fmu`), U2 (STM32F103 PX4IO, `io`) and
  U3 (AM62L, `soc`). Schematic net labels on them match the pinasg nets.

## Commands

```sh
specs/fetch.sh                  # download reference documents
specs/tools/check_nets.py       # check nets between the three processors
firmware/scripts/setup-px4.sh   # check out PX4 and link the board in
```
