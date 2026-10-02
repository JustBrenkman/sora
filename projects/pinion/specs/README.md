# pinion specs

Reference material for building pinion's flight controller section from the
Pixhawk FMUv6C, plus the design documents derived from it.

| Folder       | Committed | Contents                                                              |
| ------------ | --------- | --------------------------------------------------------------------- |
| `reference/` | no        | Third-party documents downloaded by `fetch.sh`                        |
| `pinout/`    | yes       | STM32H743 pin map: the FMUv6C assignment and pinion's deviations from it |
| `diagrams/`  | yes       | Block diagram, power tree, bus topology                               |
| `notes/`     | yes       | Design decisions and differences between the FMUv6C and pinion        |

`pinout/` is the source of truth for pin assignments. The PX4 board files in
`../firmware/` and the device tree in `../linux/` follow it.

## Fetching reference documents

```sh
./fetch.sh          # download anything missing and verify checksums
./fetch.sh --sums   # print checksums, for updating sources.yaml
```

To add a document, append an entry to `sources.yaml`, run `./fetch.sh --sums`
and paste the checksum into the entry.

## What is in the manifest

- **Pixhawk standards:** DS-018 (Autopilot v6C), DS-009 (connectors) and DS-010
  (autopilot bus), pinned to a commit of `pixhawk/Pixhawk-Standards`.
- **PX4 `px4/fmu-v6c` board support at v1.17.0:** `board.h`, `board_config.h`,
  the DMA map, SPI, I2C and timer configuration, `defconfig` and the sensor
  start-up script. These are the authoritative FMUv6C pin and bus assignments.
- **TI AM62L datasheet** (SPRSPA1B).

## Documents to add by hand

These could not be downloaded by script or do not have a confirmed URL yet.
Save them into `reference/` under the given name.

| Document                                   | Save as                               | Note                                   |
| ------------------------------------------ | ------------------------------------- | -------------------------------------- |
| STM32H743 datasheet (DS12110)              | `st/stm32h743-datasheet.pdf`          | st.com does not respond to scripted downloads |
| STM32H7 reference manual (RM0433)          | `st/rm0433-reference-manual.pdf`      | st.com does not respond to scripted downloads |
| AM62L technical reference manual           | `ti/am62l-trm.pdf`                    | URL not confirmed                      |
| FMUv6C schematic, if one is published      | `pixhawk/fmuv6c-schematic.pdf`        | No public source confirmed             |
| Datasheets for the FMUv6C sensors and PMIC | `parts/<part-number>.pdf`             | Part list comes from DS-018 and `rc.board_sensors` |
