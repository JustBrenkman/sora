<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# pinion design decisions

What pinion keeps from its two reference designs, what it changes, and what is
still open. The pin-level consequences are in [`../pinout/`](../pinout/); the
parts are in [`reference-inventory.md`](reference-inventory.md).

## Decided

| Topic | Decision |
|---|---|
| Flight controller | STM32H743VIH6, TFBGA100, following the Pixhawk FMUv6C pin for pin wherever nothing below says otherwise |
| IO processor | Kept: STM32F103 running PX4IO (8 MAIN PWM, PPM/S.BUS/DSM input, S.BUS output, safety switch) |
| Compute | AM62L32 (dual Cortex-A53), ANB 373-ball package |
| Memory | DDR4, one x16 device, point to point. The EVM uses LPDDR4 |
| AM62L storage | eMMC on MMC0 (primary boot) and microSD on MMC1 (backup boot) |
| AM62L network | One Gigabit Ethernet port (RGMII1); Wi-Fi/Bluetooth over SDIO (MMC2) and UART |
| AM62L display, audio, OSPI, second Ethernet, GPMC | Not fitted |
| FMU microSD | Not fitted; the AM62L has one |
| AM62L to FMU | UART, CAN, and the FMU's USB port |
| FMU debug | SWD and NRST on a JST-SH connector, as on the FMUv6C; not driven by the AM62L |
| Power input | As the FMUv6C: 5 V from a purchased power module on the POWER1/POWER2 ports, which also supply the analog battery voltage and current signals. No raw battery connector or on-board battery regulator |
| Stack mounting | FPV-style 30.5 x 30.5 mm M3 hole pattern centred on the board, for PDBs and 4-in-1 ESCs; see [`mechanical.md`](mechanical.md) |
| Pin data | [pinmap](https://github.com/JustBrenkman/pinmap) pindef and pinasg files in `specs/pinout/` |

## Deviations from the FMUv6C

| # | FMUv6C | pinion | Pins | Why |
|---|---|---|---|---|
| F1 | TELEM2 connector on UART5, with RTS/CTS | UART5 wired on-board to AM62L UART1; no TELEM2 connector | PC12, PD2, PC8, PC9 | Every other FMU UART is in use and UART4's pins are all taken on the 100-ball package. TELEM2 is PX4's usual companion port |
| F2 | USB-C and a 4-pin USB connector | OTG_FS wired on-board to AM62L USB1 (host); no external FMU USB | PA11, PA12, PA9 | Linux flashes the FMU through the PX4 bootloader and gets a second MAVLink link |
| F3 | microSD on SDMMC2 | Not fitted; six pins free | PD6, PD7, PB14, PB15, PB3, PB4 | The AM62L has storage |
| F4 | Power selector takes POWER1, POWER2 and the FMU's USB VBUS | Same selector; its USB input is the AM62L USB-C port's VBUS | PE15 | The FMU has no external USB (F2). Lets the board run from USB on the bench |
| F6 | CAN1 bus has one node on board | The AM62L's MCAN0 transceiver joins CAN1 | PD0, PD1 | Linux sees DroneCAN traffic |
| F7 | FM25V02A FRAM on SPI2 | Part undecided; SPI2 and its chip select stay as on the FMUv6C under neutral `_NVM` net names | PD3, PC2, PC3, PD4 | See open questions |
| F8 | IMU on a separate, vibration-isolated board with its own calibration EEPROM | Same: the two IMUs, the calibration EEPROM and the heater sit on `hardware/pinion-imu`, joined to the main board by a 22-way 0.5 mm FFC. The barometer and magnetometer stay on the main board | SPI1, I2C4, PB9 | Vibration isolation, as on the Pixhawk 6C |
| F9 | BMI088 as IMU 1: separate accel and gyro chip selects and interrupts | BMI270: one chip select and one interrupt (INT1) on the accel's pins; the gyro's two pins are free | PC15, PE4; PC14 and PE5 free | The BMI088 is not in stock anywhere |

Everything else on the FMU and the whole IO processor follows the reference:
`pinmap` notes ending in "FMUv6C." or "PX4 io-v2." mark those pins, and notes
starting with "DEVIATION:" mark the rows above.

### Firmware consequences, for the later PX4 board port

- No SD card: logging goes through the logger's MAVLink backend to the AM62L, and
  missions (dataman) need RAM or flash backing. `rc.board_*` cannot rely on
  `/fs/microsd`.
- The TELEM2 serial device is the on-board companion link.
- IMU 1 is a BMI270 (F9): `spi.cpp` lists one SPI1 device on PC15 with DRDY on PE4
  in place of the two BMI088 entries, the board enables PX4's `bmi270` driver, and
  `rc.board_sensors` starts it with a rotation taken from the layout.
- pinion is hardware version 1, revision 0, counted in its own PX4 target and
  with its own `manifest.c` entry. The numbers are not FMUv6C IDs: stock
  `px4_fmu-v6c` firmware would read version 1 as its "no PX4IO" variant.
  Dividers from `HW_VER_REV_DRIVE`, top over bottom: version 174k / 32.4k,
  revision 442k / 24.9k (configurations 2 and 1 of the "HW REV and VER ID" sheet
  in `specs/reference/px4-docs/fmuv6c-pinout.xlsx`).

## Deviations from the AM62L EVM

| # | EVM | pinion | Why |
|---|---|---|---|
| S1 | 2 GB LPDDR4 at 1.1 V, TPS6521401 PMIC | DDR4 at 1.2 V with a 2.5 V VPP rail; TPS6521402 (the DDR4 variant) | Decision above. Wiring follows SPRAD06 Figure 2-1, not the EVM |
| S2 | Two RGMII ports | RGMII1 only; RGMII2 balls are 1.8 V GPIO | One port is enough |
| S3 | PHY reset/interrupt, SD power and many enables through two TCA6424 I2C expanders | Direct SoC GPIO | Fewer parts; plenty of free balls |
| S4 | OSPI NOR and NAND | Not fitted; OSPI balls carry the Bluetooth UART (UART5, 1.8 V) and Wi-Fi interrupt | Boot is eMMC with SD, UART and USB DFU fallback |
| S5 | UART1 to the M.2 slot through buffers | UART1 (3.3 V) goes to the FMU | Bluetooth sits in a 1.8 V domain, so it needs no shifter |
| S6 | HDMI, DSI, audio codec, M.2 slot, FT4232 UART bridge, XDS110, INA228 monitors, USB PD controller | Not fitted. Console and JTAG go to connectors; Wi-Fi/BT is a soldered module | Size |
| S7 | USB1 on a Type-A host connector | USB1 wired to the FMU | Decision above |
| S8 | ADC0 on a header | ADC0 unused: `VDDA_ADC` and `ADC0_AIN[3:0]` tied to VSS, per datasheet section 5.4 | Not needed |
| S9 | Powered from USB-C PD, 5 to 12 V, with a buck-boost to 5 V | Powered from the 5 V rail chosen by the FMUv6C-style power selector | Decision above |

## Open questions

1. **Parameter storage (F7).** Options: (a) FM25V02A SPI FRAM as on the FMUv6C,
   no firmware change; (b) an SPI EEPROM on the same pins, needing a different
   PX4 MTD driver and limited by write endurance; (c) an I2C EEPROM on I2C4,
   which frees SPI2 and PD4 but shares the sensor bus.
2. **5 V budget.** The whole board now runs from the power module's 5 V output.
   Add up the AM62L section, Wi-Fi, Ethernet, the FMU and the two 1.5 A port
   rails, and pick a power module that covers it (the FMUv6C alone allows 6 V
   maximum input and two 1.5 A port limits).
3. **USB-C as a power source.** Assumed yes, as on the FMUv6C: VBUS is the
   selector's third input and drives `N_USB_VBUS_VALID`. A USB port cannot
   supply the whole board under load, so decide what stays off when USB is the
   source. The same port also has to source VBUS when it acts as a USB host.
4. **Spare FMU pins.** The six SDMMC2 pins are free, and so are PC14 and PE5 (F9). Candidates: an
   AM62L-driven BOOT0 or reset; a PPS line between the two processors.
5. **BOOT0.** Pull-down and test pad only, or also drivable from an AM62L GPIO
   so Linux can force the ROM DFU loader if the PX4 bootloader is ever erased.
6. *(closed)* **IMU isolation (F8).** Decided: a separate IMU board, `hardware/pinion-imu`.
7. **VTT termination.** SPRAD06 makes VTT optional on address/control for a
   single DDR4 package; without it VREFCA comes from a divider. Decide before
   the DDR sheet.
8. **Wi-Fi/BT module, Ethernet connector, and PMIC rail budget.** Part choices
   that the schematic TODO lists as "select".
9. **Connector set.** Which Pixhawk ports are populated (TELEM1, TELEM3, GPS1,
   GPS2, I2C, CAN1, CAN2, PWM, RC) is assumed complete here; drop any that the
   airframe does not need.
