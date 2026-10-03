# pinion

A single board computer with an integrated flight controller, on one PCB.

| Section           | Part           | Role                                                 |
| ----------------- | -------------- | ---------------------------------------------------- |
| Compute           | TI AM62L       | Linux companion computer                             |
| Flight controller | ST STM32H743   | PX4 autopilot, derived from the Pixhawk FMUv6C       |

**Status:** pin maps, block diagrams and the schematic TODO list are written
(`specs/`, `hardware/pinion-main/SCHEMATIC_TODO.md`). No schematic, board files
or device tree exist yet.

## Layout

| Folder                  | Contents                                                        |
| ----------------------- | --------------------------------------------------------------- |
| [specs/](specs/)        | Reference documents, pin maps, diagrams, design notes           |
| [hardware/](hardware/)  | KiCad projects: the main board and accessory boards             |
| [firmware/](firmware/)  | PX4 board support for the `sora_pinion` target                  |
| [linux/](linux/)        | Device tree, kernel and U-Boot configuration, Armbian build     |
| `cad/`                  | Enclosure, mounts and board STEP exports                        |
