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
| Power input | On-board wide-input buck from the battery; no Pixhawk power-brick ports |
| Pin data | [pinmap](https://github.com/JustBrenkman/pinmap) pindef and pinasg files in `specs/pinout/` |

## Deviations from the FMUv6C

| # | FMUv6C | pinion | Pins | Why |
|---|---|---|---|---|
| F1 | TELEM2 connector on UART5, with RTS/CTS | UART5 wired on-board to AM62L UART1; no TELEM2 connector | PC12, PD2, PC8, PC9 | Every other FMU UART is in use and UART4's pins are all taken on the 100-ball package. TELEM2 is PX4's usual companion port |
| F2 | USB-C and a 4-pin USB connector | OTG_FS wired on-board to AM62L USB1 (host); no external FMU USB | PA11, PA12, PA9 | Linux flashes the FMU through the PX4 bootloader and gets a second MAVLink link |
| F3 | microSD on SDMMC2 | Not fitted; six pins free | PD6, PD7, PB14, PB15, PB3, PB4 | The AM62L has storage |
| F4 | Two power-brick inputs with analog voltage and current sense | One on-board battery sense (shunt amplifier and divider) on the BAT1 channels; BAT2 channels unused | PC4, PC5 used; PA2, PB1 free | Power comes from the on-board buck |
| F5 | `N_BRICK1_VALID`, `N_BRICK2_VALID`, `N_USB_VBUS_VALID` from the power selector | BRICK1 driven by the 5 V buck's power-good; the other two pulled up (invalid) | PA15, PB12, PE15 | There is no power selector. Keeping the nets lets PX4's power checks work unchanged |
| F6 | CAN1 bus has one node on board | The AM62L's MCAN0 transceiver joins CAN1 | PD0, PD1 | Linux sees DroneCAN traffic |
| F7 | FM25V02A FRAM on SPI2 | Part undecided; SPI2 and its chip select stay as on the FMUv6C under neutral `_NVM` net names | PD3, PC2, PC3, PD4 | See open questions |
| F8 | IMU on a separate, vibration-isolated board with its own calibration EEPROM | Same parts, same buses; whether they sit on a daughterboard is a mechanical decision | SPI1, I2C4 | See open questions |

Everything else on the FMU and the whole IO processor follows the reference:
`pinmap` notes ending in "FMUv6C." or "PX4 io-v2." mark those pins, and notes
starting with "DEVIATION:" mark the rows above.

### Firmware consequences, for the later PX4 board port

- No SD card: logging goes through the logger's MAVLink backend to the AM62L, and
  missions (dataman) need RAM or flash backing. `rc.board_*` cannot rely on
  `/fs/microsd`.
- `BOARD_NUMBER_BRICKS` becomes 1. `BOARD_ADC_USB_VALID` always reads false.
- The TELEM2 serial device is the on-board companion link.
- pinion needs its own `HW_VER`/`HW_REV` resistor pair and `manifest.c`, since it
  is not one of the V6C00..V6C22 variants.

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
| S9 | Powered from USB-C PD, 5 to 12 V | Powered from the on-board 5 V rail | Decision above |

## Open questions

1. **Parameter storage (F7).** Options: (a) FM25V02A SPI FRAM as on the FMUv6C,
   no firmware change; (b) an SPI EEPROM on the same pins, needing a different
   PX4 MTD driver and limited by write endurance; (c) an I2C EEPROM on I2C4,
   which frees SPI2 and PD4 but shares the sensor bus.
2. **Battery input range and current.** Sets the buck, the input protection,
   the shunt and the divider ratio. PX4's defaults assume 18.18 V/V and
   36.36 A/V scaling.
3. **Second supply and bench power.** Should USB-C VBUS be able to power the
   board on the bench (through an ideal diode into the 5 V rail)? If so,
   `N_USB_VBUS_VALID` gets a real source.
4. **Spare FMU pins.** PA2, PB1 (ADC), PB12, PE15 and the six SDMMC2 pins are
   free or strapped. Candidates: 5 V/3.3 V SoC rail monitoring on the two ADC
   inputs; an AM62L-driven BOOT0 or reset; a PPS line between the two processors.
5. **BOOT0.** Pull-down and test pad only, or also drivable from an AM62L GPIO
   so Linux can force the ROM DFU loader if the PX4 bootloader is ever erased.
6. **IMU isolation (F8).** Daughterboard with foam, as Holybro does, or on the
   main board.
7. **VTT termination.** SPRAD06 makes VTT optional on address/control for a
   single DDR4 package; without it VREFCA comes from a divider. Decide before
   the DDR sheet.
8. **Wi-Fi/BT module, Ethernet connector, and PMIC rail budget.** Part choices
   that the schematic TODO lists as "select".
9. **Connector set.** Which Pixhawk ports are populated (TELEM1, TELEM3, GPS1,
   GPS2, I2C, CAN1, CAN2, PWM, RC) is assumed complete here; drop any that the
   airframe does not need.
