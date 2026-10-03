<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Reference design inventory

Every major part, connector and sensor of the two reference designs, and what
pinion does with each: **keep** (same part or function), **change**, or
**drop**. Reasons for changes are in [`decisions.md`](decisions.md).

Neither reference comes with a schematic in `reference/`. The FMUv6C side is
reconstructed from the PX4 board files, the Pixhawk DS-018 standard and
Holybro's documentation; the EVM side from its user's guide (SPRUJG8B). Where a
part number is not stated in those sources the table says so.

## Pixhawk FMUv6C (Holybro Pixhawk 6C)

Sources: `reference/px4-fmu-v6c/`, `reference/pixhawk/DS-018`,
`reference/holybro/`, `reference/ardupilot-pixhawk6c/hwdef.dat`,
`reference/px4-io-v2/`.

### Processors, sensors and memory

| Part | Function | Connection | pinion |
|---|---|---|---|
| STM32H743 (100-pin) | FMU, PX4 | – | keep: STM32H743VIH6, TFBGA100 |
| STM32F103 (48-pin) | PX4IO | USART2 to FMU USART6, 1.5 Mbaud | keep |
| ICM-42688-P | IMU 2 | SPI1, CS3 PC13, DRDY3 PE6 | keep |
| BMI088 (BMI055 before rev 2) | IMU 1, accel + gyro | SPI1, CS1 PC15 / CS2 PC14, DRDY1 PE4 / DRDY2 PE5 | keep: BMI088 |
| IST8310 | Magnetometer | I2C4, 0x0C | keep |
| MS5611 | Barometer | I2C4, 0x77 | keep |
| 24LC64 EEPROM | IMU calibration | I2C4, 0x51 | keep |
| FM25V02A FRAM | Parameters | SPI2, CS PD4 | undecided: FRAM or EEPROM |
| microSD socket | Logs, missions | SDMMC2 | drop |
| IMU heater (resistor + MOSFET) | Holds the IMU near 45 °C | PB9 | keep |
| 16 MHz crystal | FMU HSE | PH0, PH1 | keep |
| 24 MHz crystal | IO HSE | PD0, PD1 of the F103 | keep |

The IMUs, magnetometer, calibration EEPROM and heater sit on a separate,
vibration-isolated IMU board on the Pixhawk 6C; the barometer and FRAM are on
the main board.

### Interface and power parts

| Part | Function | Connection | pinion |
|---|---|---|---|
| TJA1051 x2 | CAN transceivers | FDCAN1 PD0/PD1, FDCAN2 PB5/PB13 | keep (TJA1051-class; TCAN1051 datasheet is in `reference/parts/`) |
| 5 V load switch, 1.5 A limit | `VDD_5V_PERIPH`: all ports except TELEM1 and GPS2 | EN PE2, OC PE3 (both active low) | keep (part not named in the sources) |
| 5 V load switch, 1.5 A limit | `VDD_5V_HIPOWER`: TELEM1 and GPS2 | EN PC10, OC PC11 (both active low) | keep (part not named) |
| 3.3 V sensor rail switch | `VDD_3V3_SENSORS` | EN PB2 | keep |
| 3.3 V Spektrum switch | Satellite receiver power and bind | EN PC13 of the F103 | keep |
| Power selector (2 bricks + USB) | Picks the 5 V source, reports `N_BRICKx_VALID`, `N_USB_VBUS_VALID` | PA15, PB12, PE15 | keep; the USB input is the AM62L USB-C port's VBUS |
| 5 V rail divider | `FMU_SCALED_V5` | PA4 | keep |
| Battery sense inputs | Voltage and current from the power bricks | PC5/PC4 (BAT1), PB1/PA2 (BAT2) | keep |
| Version/revision dividers | Two resistor pairs read at boot | drive PE12, sense PC0/PC1 | keep, with pinion's own values |
| PWM level buffers | 3.3 V or 5 V PWM signal level (solder option) | FMU_CH1..8, IO_CH1..8 | keep (buffer with selectable VCC) |
| S.BUS inverters | Invert S.BUS in and out | F103 PB11, PB10, enable PB4 | keep |
| Servo rail sense | `VDD_SERVO` divider, 0 to 36 V rail | F103 PA4 | keep |
| LEDs | FMU red PD10, blue PD11; IO blue PB14, amber PB15, green PA11; safety LED PB13 | GPIO, active low | keep |
| Buzzer drive | Tone alarm to the GPS1 connector | PB0 (TIM3_CH3) | keep |
| Safety switch input | From the GPS1 connector | F103 PB5 | keep |

### Connectors

JST-GH 1.25 mm unless noted; pin 1 first.

| Port | Pins | Signals | pinion |
|---|---|---|---|
| POWER1, POWER2 | 6 | 5 V, 5 V, CURRENT, VOLTAGE, GND, GND | keep |
| TELEM1 | 6 | 5 V (HIPOWER), UART7 TX, RX, CTS, RTS, GND | keep |
| TELEM2 | 6 | 5 V, UART5 TX, RX, CTS, RTS, GND | drop: UART5 goes to the AM62L |
| TELEM3 | 6 | 5 V, USART2 TX, RX, NC, NC, GND | keep |
| GPS1 | 10 | 5 V, USART1 TX, RX, I2C1 SCL, SDA, SAFETY_SWITCH, SAFETY_LED, 3V3, BUZZER, GND | keep |
| GPS2 | 6 | 5 V (HIPOWER), UART8 TX, RX, I2C2 SCL, SDA, GND | keep |
| I2C | 4 | 5 V, I2C2 SCL, SDA, GND | keep |
| CAN1, CAN2 | 4 each | 5 V, CAN_H, CAN_L, GND | keep |
| USB | USB-C and a 4-pin JST-GH | VBUS, DM, DP, GND | drop: USB goes to the AM62L |
| FMU PWM OUT (AUX) | 10 | VDD_SERVO, FMU_CH1..8, GND | keep |
| IO PWM OUT (MAIN) | 10 | VDD_SERVO, IO_CH1..8, GND | keep |
| DSM RC | 3, JST-ZH 1.5 mm | 3V3_SPEKTRUM, GND, DSM IN | keep |
| PPM/SBUS RC | 5 | 5 V, PPM/SBUS IN, RSSI IN, NC, GND | keep |
| SBUS OUT | 3 | NC, SBUS OUT, GND | keep |
| FMU debug | 10, JST-SH 1.0 mm | 3V3, USART3 TX, RX, SWDIO, SWCLK, 3 spare, NRST, GND | keep; the three spare pins are not connected (their FMUv6C signals do not exist on this package) |
| IO debug | 10, JST-SH 1.0 mm | 3V3, USART1 TX, NC, SWDIO, SWCLK, SWO, 2 spare, NRST, GND | keep |
| microSD | – | SDMMC2 | drop |

## TI AM62L EVM (TMDS62LEVM, PROC181)

Sources: `reference/ti/sprujg8b-am62l-evm-users-guide.pdf` (Table 2-21 and
sections 2.6 to 2.12), `reference/linux-dts/k3-am62l3-evm.dts`.

### Processor, memory and storage

| Part | Function | SoC port | pinion |
|---|---|---|---|
| AM62L32 (ANB, 373 balls) | SoC | – | keep |
| MT53E1G16D1ZW-046 | 2 GB LPDDR4 | DDR0 | change: DDR4 x16 (part to select) |
| MTFC32GBCAQTC-IT | 32 GB eMMC, HS200 | MMC0, 1.8 V | keep (size to select) |
| MEM2051-00-195-00-A | microSD socket, UHS-I | MMC1 | keep |
| S28HS512T | 512 Mbit OSPI NOR | OSPI0 | drop |
| W25N01JW | 1 Gbit QSPI NAND | OSPI0 | drop |
| AT24C512C | Board ID EEPROM | I2C0, 0x51 | keep |

### Interfaces

| Part | Function | SoC port | pinion |
|---|---|---|---|
| DP83867IRRGZ x2 + RJ45 with magnetics | Gigabit Ethernet | RGMII1, RGMII2, shared MDIO0 | change: one port; connector type to select |
| M.2 Key E slot | Wi-Fi SDIO + Bluetooth UART/PCM | MMC2, UART1, McASP0 | change: soldered module, HCI on UART5 at 1.8 V |
| USB Type-C | USB 2.0 dual role | USB0 | keep |
| USB Type-A | USB 2.0 host | USB1 | change: wired to the FMU |
| TPS65988 | Dual USB PD controller | I2C2 | drop |
| FT4232HL + micro-B | Four UARTs to USB | UART0, UART1, UART4, WKUP_UART0 | drop: UART0 console on a connector |
| XDS110 + 20-pin cTI header | JTAG | TCK, TMS, TDI, TDO, TRSTn, EMU0/1 | change: header only |
| TSM-104 headers x3 | CAN, no transceiver on the EVM | MCAN0, MCAN1, MCAN2 | change: MCAN0 with a transceiver on the FMU's CAN1 bus |
| SiI9022A + TPD12S016 | DPI to HDMI | VOUT0, McASP0, I2C1 | drop |
| DSI connector | Display | DSI0 | drop |
| TLV320AIC3106 | Audio codec | McASP0, I2C1 | drop |
| TCA6424A x2 | 24-bit I2C GPIO expanders | I2C1, 0x22 / 0x23 | drop: direct GPIO |
| TCA6424A + buffers | Boot-mode switch reader and strap buffers | BOOTMODE[15:0] | change: strap resistors with a small selector |
| INA228 x8, TMP100 x2 | Rail current and temperature monitors | I2C1 | drop |
| 2x5 and 2x15 headers, ADC header | Expansion | SPI1, SPI3, UART4, I2C3, GPIO, ADC0 | drop (free balls remain for a later header) |
| User LEDs, button | – | GPIO | keep: one LED, one button |

### Power, clock and reset

| Part | Function | pinion |
|---|---|---|
| TPS630702 buck-boost | 5 V from the PD output | drop: 5 V comes from the power module |
| LM5141 buck | 3.3 V main, feeds the PMIC | change: 3.3 V buck from 5 V (part to select) |
| TPS6521401 PMIC | Buck1 0.75 V core, Buck2 1.8 V I/O, Buck3 1.1 V DDR, LDO1 1.8 V analog, LDO2 3.3 V I/O; I2C 0x30 on WKUP_I2C0 | change: TPS6521402, Buck3 at 1.2 V |
| TPS74501 LDO x2 | `VDD_RTC` 0.75 V and `VDDS_RTC` 1.8 V | keep if RTC-only low-power mode is wanted, else fed from the PMIC rails |
| TLV75518 LDO | `VPP` 1.8 V for eFuse programming | keep as an unpopulated option |
| TPS62824 buck, TLV75510 LDO | 2.5 V and 1.0 V for the Ethernet PHYs | keep (one PHY) |
| TLV75512 LDO | 1.2 V for the HDMI framer | drop |
| Load switch on the SD supply | Lets the card be power-cycled | keep |
| 25 MHz oscillator + LMK1C1103 1:3 buffer | SoC `WKUP_OSC0` and both PHYs | change: a crystal each, or one oscillator and a 1:2 buffer |
| 32.768 kHz crystal | `LFOSC0`, RTC domain | keep |
| `WKUP_CLKOUT0` | 32.768 kHz to the Wi-Fi module | keep |
| Reset: PMIC to `PORz`, button to `RESETz`, `RESETSTATz` to peripherals, `RTC_PORz` | – | keep |

Not on the EVM but needed for DDR4: a 2.5 V `VPP` supply for the memory and,
optionally, a VTT/VREF regulator (TPS51200 datasheet is in `reference/parts/`).

EVM supply groups, from Table 2-29, with pinion's voltage where it differs:

| Rail | SoC supplies | Voltage |
|---|---|---|
| VDD_CORE | VDD_CORE, VDDA_DDR_PLL0 | 0.75 V |
| VDDA_CORE | VDDA_CORE_USB, VDDA_CORE_DSI, VDDA_CORE_DSI_CLK | 0.75 V |
| SoC_VDD_RTC | VDD_RTC | 0.75 V |
| SoC_VDDS_RTC_1V8 | VDDS_RTC | 1.8 V |
| VDDA_1V8 | VDDA_1P8_DSI, VDDA_ADC, VDDS_OSC0, VDDA_PLL0/1, VDDA_1P8_USB | 1.8 V (pinion ties VDDA_ADC to VSS) |
| VDD_LPDDR4 | VDDS_DDR | 1.1 V (pinion: 1.2 V) |
| VPP_1V8 | VPP | 1.8 V, programming only |
| VDDSHV_SD_IO | VDDSHV3 | 3.3 V / 1.8 V from the internal SDIO LDO |
| SOC_DVDD1V8 | VDDSHV2, VDDSHV4, VDDS_WKUP, VDDS0, VDDS1 | 1.8 V |
| SOC_DVDD3V3 | VDDSHV0, VDDSHV1, VDDA_3P3_USB | 3.3 V |
| VDD_MMC1_SD | VDDA_3P3_SDIO | 3.3 V |
