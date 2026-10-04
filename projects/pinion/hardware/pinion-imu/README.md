<!-- SPDX-License-Identifier: CERN-OHL-P-2.0 -->
# pinion-imu

Vibration-isolated sensor board for pinion, joined to the main board by a
flat cable. It carries what the Pixhawk 6C puts on its isolated IMU board:

- **U1** BMI270 (IMU 1) and **U2** ICM-42688-P (IMU 2), on the FMU's SPI1.
- **U3** 24LC64 calibration EEPROM, on I2C4 at address 0x51.
- **R1, Q1, U4, U5** IMU heater: a PCB trace of about 10 ohm under the IMUs, fed
  from +5V, with a constant-current sink (LM4040 reference, TLV9001, AO3400A,
  0.5 ohm sense) that draws 0.30 A while `FMU_HEATER` is high. The trace and Q1
  together dissipate about 1.5 W. The trace is drawn in layout.

The barometer and magnetometer stay on the main board.

## Connector

**J1** is a 22-way, 0.5 mm pitch FFC connector, the same part and the same pin
numbering as J4 on the sensors sheet of `pinion-main`. Net names are the main
board's, so the two schematics can be compared directly.

| Pin | Net | Pin | Net |
|---|---|---|---|
| 1 | GND | 12 | FMU_SPI1_DRDY1_BMI270 |
| 2, 3 | FMU_VDD_3V3_SENSORS | 13 | FMU_SPI1_DRDY3_ICM42688 |
| 4 | GND | 14 | GND |
| 5 | FMU_SPI1_SCK_SENSOR | 15 | FMU_I2C4_SCL |
| 6 | GND | 16 | FMU_I2C4_SDA |
| 7 | FMU_SPI1_MOSI_SENSOR | 17 | GND |
| 8 | FMU_SPI1_MISO_SENSOR | 18 | FMU_HEATER |
| 9 | GND | 19 | spare |
| 10 | FMU_SPI1_CS1_BMI270 | 20, 21 | +5V (heater) |
| 11 | FMU_SPI1_CS3_ICM42688 | 22 | GND |

Pin 1 connects to pin 1. Whether the cable needs contacts on the same side or on
opposite sides depends on how the two connectors face each other in layout.

The repo-wide KiCad rules in the root `AGENTS.md` apply.
