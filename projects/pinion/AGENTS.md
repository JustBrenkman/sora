# pinion

Single board computer with an integrated flight controller, on one PCB:

- **Compute:** TI AM62L running Linux.
- **Flight controller:** STM32H743 running PX4, derived from the Pixhawk FMUv6C
  (PX4 board `px4/fmu-v6c`, which uses the STM32H743VI).

The repo-wide rules in the root `AGENTS.md` apply.

## Where things are

| Path                              | Contents                                                    |
| --------------------------------- | ----------------------------------------------------------- |
| `specs/sources.yaml`, `fetch.sh`  | Manifest and downloader for FMUv6C reference documents      |
| `specs/reference/`                | Downloaded documents; gitignored, may be empty              |
| `specs/pinout/`                   | Pin map; the source of truth for firmware and device tree   |
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

## Commands

```sh
specs/fetch.sh                  # download reference documents
firmware/scripts/setup-px4.sh   # check out PX4 and link the board in
```
