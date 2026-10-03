# pinion specs

Reference material for pinion's two halves, the Pixhawk FMUv6C flight controller
and the TI AM62L computer, plus the design documents derived from it.

| Folder       | Committed | Contents                                                              |
| ------------ | --------- | --------------------------------------------------------------------- |
| `reference/` | no        | Third-party documents downloaded by `fetch.sh`                        |
| `pinout/`    | yes       | pinmap pin definitions and assignments for the STM32H743, STM32F103 and AM62L |
| `diagrams/`  | yes       | Block diagram, power tree, bus topology                               |
| `notes/`     | yes       | Design decisions, reference inventory, AM62L I/O supply groups        |
| `tools/`     | yes       | Scripts that generate the pin definitions and check nets across chips |

Start with `notes/decisions.md` (what pinion keeps and changes),
`notes/reference-inventory.md` (every part of both reference designs) and
`diagrams/block-diagram.md`.

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

Paths are relative to `reference/`.

| Folder                 | Source                                   | Contents |
| ---------------------- | ---------------------------------------- | -------- |
| `pixhawk/`             | `pixhawk/Pixhawk-Standards`, pinned commit | DS-018 (Autopilot v6C), DS-009 (connectors), DS-010 (autopilot bus) |
| `holybro/`             | docs.holybro.com, Pixhawk 6C             | STM32 pinout PDF, FMUv6C system diagram, port pinout, pin order, dimensions, sample wiring diagram, PCB photos (RC09, RC12), case and PWM adapter STEP models |
| `holybro/pages/`       | docs.holybro.com, Pixhawk 6C             | Overview, technical specification, port pin tables, system diagram, PWM voltage mod and supported firmware pages as Markdown |
| `px4-fmu-v6c/`         | PX4-Autopilot v1.17.0                    | The complete `boards/px4/fmu-v6c` directory: all `.px4board` variants, `nuttx-config/`, `src/`, `init/`, `extras/` |
| `px4-docs/`            | PX4-Autopilot v1.17.0 and its linked sheet | Pixhawk 6C hardware page, quick start, and the FMUv6C pinout spreadsheet (pinout, sensor assignment, UART assignment, hardware revision IDs) |
| `ardupilot-pixhawk6c/` | ArduPilot Copter-4.7.1                   | `hwdef.dat`, `hwdef-bl.dat`, `defaults.parm`: a compact second statement of the pin assignments |
| `parts/`               | Bosch Sensortec, ti.com                  | BMI088, TPS65214 (PMIC), DP83867IR (Ethernet PHY), TPS51200 (DDR termination), TCAN1051 (CAN transceiver) datasheets |
| `ti/`                  | ti.com                                   | AM62L datasheet (SPRSPA1B), technical reference manual (SPRUJB4A), EVM user's guide (SPRUJG8B), DDR board design and layout (SPRAD06C), high-speed interface layout (SPRAAR7J), Sitara power distribution networks (SPRAC76H) |
| `st-pin-data/`         | STMicroelectronics/STM32_open_pin_data, pinned commit | Pin and alternate-function XML for the STM32H743VIH and STM32F103C8T; input to `tools/gen_stm32_pindef.py` |
| `px4-io-v2/`, `ardupilot-iomcu/` | PX4-Autopilot v1.17.0, ArduPilot Copter-4.7.1 | PX4IO board configuration and ArduPilot's IO MCU hardware definition |
| `linux-dts/`           | torvalds/linux v7.0                      | AM62L EVM device tree, the SoC `.dtsi` files and `k3-pinctrl.h` |

The full download is about 150 MB, most of it the AM62L technical reference
manual.

The Holybro pages and the pinout spreadsheet have no checksum recorded, because
they are regenerated on every download.

## Documents to add by hand

These could not be downloaded by script. Save them into `reference/` under the
given name.

| Document                              | Save as                           | Note                                          |
| ------------------------------------- | --------------------------------- | --------------------------------------------- |
| STM32H743 datasheet (DS12110)         | `st/stm32h743-datasheet.pdf`      | st.com does not respond to scripted downloads |
| STM32H7 reference manual (RM0433)     | `st/rm0433-reference-manual.pdf`  | st.com does not respond to scripted downloads |
| STM32F103 datasheet (IO processor)    | `st/stm32f103-datasheet.pdf`      | st.com does not respond to scripted downloads |
| ICM-42688-P datasheet                 | `parts/icm-42688-p-datasheet.pdf` | TDK serves it through a download page         |
| MS5611 datasheet                      | `parts/ms5611-datasheet.pdf`      | te.com refuses scripted downloads             |
| IST8310 datasheet                     | `parts/ist8310-datasheet.pdf`     | No working URL found                          |
| AM62L EVM design files (schematic, BOM) | `ti/am62l-evm-design-files/`    | Linked from the TMDS62LEVM page; no stable URL |
| AM62L Power Supply Implementation note | `ti/am62l-power-supply-implementation.pdf` | Referenced by the EVM guide; document number not known |
| DDR4 SDRAM, eMMC and Wi-Fi module datasheets | `parts/`                  | Once the parts are selected                   |

No FMUv6C schematic was found: Holybro's documentation and the Pixhawk standards
provide the pinout, system diagram and interface standard, but not the
schematic itself.
