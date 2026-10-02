# Naming projects

Sora (空) is Japanese for sky. Projects inside it are named after bird anatomy.

## Rules

- One lowercase word, ASCII only, no hyphens or digits.
- The name is the folder under `projects/` and is reused wherever the project
  needs an identifier:
  - PX4 board target: `sora_<name>`
  - Device tree: `k3-<soc>-sora-<name>.dts`
  - KiCad main board: `<name>-main`
- Pick a part whose role hints at what the project does, where that is possible.

## In use

| Name     | Meaning                                              | Project                                      |
| -------- | ---------------------------------------------------- | -------------------------------------------- |
| `pinion` | Outer section of the wing, carrying the flight feathers | AM62L SBC with integrated STM32H7 flight controller |

## Candidates

| Name       | Meaning                                         |
| ---------- | ----------------------------------------------- |
| `alula`    | Small "thumb" feathers that control slow flight |
| `remex`    | A flight feather of the wing                    |
| `rectrix`  | A tail feather, used for steering               |
| `covert`   | Feathers covering the base of the flight feathers |
| `keel`     | Breastbone ridge anchoring the flight muscles   |
| `furcula`  | The wishbone, a spring between the shoulders    |
| `syrinx`   | The vocal organ                                 |
| `talon`    | Claw                                            |
| `tarsus`   | Lower leg                                       |
| `rachis`   | Central shaft of a feather                      |
| `vane`     | The flat web of a feather                       |
| `barb`     | A branch of the feather vane                    |
| `mantle`   | Upper back                                      |
| `crest`    | Head feathers                                   |

Move a name from Candidates to In use when a project takes it.
