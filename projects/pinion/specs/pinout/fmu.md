# STM32H743VIH6 pinout (TFBGA100, U1)

| Pin | Pad | Function | Mux | Net | Config | Note |
|---|---|---|---|---|---|---|
| PC14 | A1 | gpio_out |  | FMU_SPI1_CS2_BMI088_GYRO | initial=high | FMUv6C. |
| PC13 | A2 | gpio_out |  | FMU_SPI1_CS3_ICM42688 | initial=high | FMUv6C. |
| PE2 | A3 | gpio_out |  | N_VDD_5V_PERIPH_EN | initial=high | 5 V peripheral switch enable, active low. FMUv6C. |
| PB9 | A4 | TIM17.CH1 | AF1 | FMU_HEATER |  |  |
| PB7 | A5 | I2C1.SDA | AF4 | FMU_I2C1_SDA_GPS1 | drive=open_drain |  |
| PB4 | A6 |  |  |  |  |  |
| PB3 | A7 |  |  |  |  |  |
| PA15 | A8 | gpio_in |  | N_BRICK1_VALID | bias=pull_up | Power selector: POWER1 is the active 5 V source, active low. FMUv6C. |
| PA14 | A9 | DEBUG.JTCK-SWCLK | AF0 | FMU_SWCLK |  |  |
| PA13 | A10 | DEBUG.JTMS-SWDIO | AF0 | FMU_SWDIO |  |  |
| PC15 | B1 | gpio_out |  | FMU_SPI1_CS1_BMI088_ACC | initial=high | FMUv6C (BMI055 on early revisions). |
| VBAT | B2 | reserved |  | FMU_VBAT |  | RTC/backup supply. |
| PE3 | B3 | gpio_in |  | N_VDD_5V_PERIPH_OC |  | 5 V peripheral switch overcurrent flag, active low; needs a pull-up. FMUv6C. |
| PB8 | B4 | I2C1.SCL | AF4 | FMU_I2C1_SCL_GPS1 | drive=open_drain |  |
| PB6 | B5 | USART1.TX | AF7 | FMU_USART1_TX_GPS1 |  |  |
| PD5 | B6 | USART2.TX | AF7 | FMU_USART2_TX_TEL3 |  |  |
| PD2 | B7 | UART5.RX | AF8 | FMU_UART5_RX_SOC |  |  |
| PC11 | B8 | gpio_in |  | N_VDD_5V_HIPOWER_OC |  | 5 V high-power switch overcurrent flag, active low; needs a pull-up. FMUv6C. |
| PC10 | B9 | gpio_out |  | N_VDD_5V_HIPOWER_EN | initial=high | 5 V high-power (TELEM1 + GPS2) switch enable, active low. FMUv6C. |
| PA12 | B10 | USB_OTG_FS.DP | AF10 | FMU_USB_DP |  |  |
| PH0 | C1 | RCC.OSC_IN | fixed | FMU_OSC_IN |  |  |
| VSS_C2 | C2 | reserved |  | GND |  |  |
| PE4 | C3 | gpio_in |  | FMU_SPI1_DRDY1_BMI088_ACC |  | FMUv6C. |
| PE1 | C4 | UART8.TX | AF8 | FMU_UART8_TX_GPS2 |  |  |
| PB5 | C5 | FDCAN2.RX | AF9 | FMU_CAN2_RX |  |  |
| PD6 | C6 |  |  |  |  |  |
| PD3 | C7 | SPI2.SCK | AF5 | FMU_SPI2_SCK_NVM |  |  |
| PC12 | C8 | UART5.TX | AF8 | FMU_UART5_TX_SOC |  |  |
| PA9 | C9 | USB_OTG_FS.VBUS | fixed | FMU_VBUS_SENSE |  |  |
| PA11 | C10 | USB_OTG_FS.DM | AF10 | FMU_USB_DM |  |  |
| PH1 | D1 | RCC.OSC_OUT | fixed | FMU_OSC_OUT |  |  |
| VDD_D2 | D2 | reserved |  | FMU_VDD_3V3 |  |  |
| PE5 | D3 | gpio_in |  | FMU_SPI1_DRDY2_BMI088_GYRO |  | FMUv6C. |
| PE0 | D4 | UART8.RX | AF8 | FMU_UART8_RX_GPS2 |  |  |
| BOOT0 | D5 | reserved |  | FMU_BOOT0 |  | Pull-down, with a test pad for ROM DFU recovery. |
| PD7 | D6 |  |  |  |  |  |
| PD4 | D7 | gpio_out |  | FMU_SPI2_CS_NVM | initial=high | Parameter storage chip select. FMUv6C (FRAM). |
| PD0 | D8 | FDCAN1.RX | AF9 | FMU_CAN1_RX |  |  |
| PA8 | D9 | TIM1.CH1 | AF1 | FMU_CH1 |  |  |
| PA10 | D10 | USART1.RX | AF7 | FMU_USART1_RX_GPS1 |  |  |
| NRST | E1 | reserved |  | FMU_NRST |  | Reset: debug connector and reset supervisor. |
| PC2 | E2 | SPI2.MISO | AF5 | FMU_SPI2_MISO_NVM |  |  |
| PE6 | E3 | gpio_in |  | FMU_SPI1_DRDY3_ICM42688 |  | FMUv6C. |
| VSS_E4 | E4 | reserved |  | GND |  |  |
| VSS_E5 | E5 | reserved |  | GND |  |  |
| VSS_E6 | E6 | reserved |  | GND |  |  |
| VCAP_E7 | E7 | reserved |  | FMU_VCAP1 |  | Core regulator capacitor, 2.2 uF to GND. |
| PD1 | E8 | FDCAN1.TX | AF9 | FMU_CAN1_TX |  |  |
| PC9 | E9 | UART5.CTS | AF8 | FMU_UART5_CTS_SOC |  |  |
| PC7 | E10 | USART6.RX | AF7 | FMU_USART6_RX_FROM_IO |  |  |
| PC0 | F1 | ADC3.INP10 | analog | HW_REV_SENSE |  |  |
| PC1 | F2 | ADC3.INP11 | analog | HW_VER_SENSE |  |  |
| PC3 | F3 | SPI2.MOSI | AF5 | FMU_SPI2_MOSI_NVM |  |  |
| VDDLDO | F4 | reserved |  | FMU_VDD_3V3 |  | Internal core LDO input. |
| VDD_F5 | F5 | reserved |  | FMU_VDD_3V3 |  |  |
| VDD33_USB | F6 | reserved |  | FMU_VDD_3V3 |  |  |
| PDR_ON | F7 | reserved |  | FMU_VDD_3V3 |  | Tied high: internal power-on reset enabled. |
| VCAP_F8 | F8 | reserved |  | FMU_VCAP2 |  | Core regulator capacitor, 2.2 uF to GND. |
| PC8 | F9 | UART5.RTS | AF8 | FMU_UART5_RTS_SOC |  |  |
| PC6 | F10 | USART6.TX | AF7 | FMU_USART6_TX_TO_IO |  |  |
| VSSA | G1 | reserved |  | GND |  |  |
| PA0 | G2 | TIM5.CH1 | AF2 | FMU_CH7 |  |  |
| PA4 | G3 | ADC1.INP18 | analog | FMU_SCALED_V5 |  |  |
| PC4 | G4 | ADC1.INP4 | analog | FMU_BAT1_I |  |  |
| PB2 | G5 | gpio_out |  | VDD_3V3_SENSORS_EN | initial=low | Sensor rail load switch enable, active high. FMUv6C. |
| PE10 | G6 | UART7.CTS | AF7 | FMU_UART7_CTS_TEL1 |  |  |
| PE14 | G7 | TIM1.CH4 | AF1 | FMU_CH4 |  |  |
| PD15 | G8 | TIM4.CH4 | AF2 | FMU_CH6 |  |  |
| PD11 | G9 | gpio_out |  | N_FMU_LED_BLUE | initial=high | Status LED, active low, open drain. FMUv6C. |
| PB15 | G10 |  |  |  |  |  |
| VDDA | H1 | reserved |  | FMU_VDDA_3V3 |  | Analog supply, filtered from FMU_VDD_3V3. VREF+ is bonded to VDDA on TFBGA100. |
| PA1 | H2 | TIM5.CH2 | AF2 | FMU_CH8 |  |  |
| PA5 | H3 | SPI1.SCK | AF5 | FMU_SPI1_SCK_SENSOR | speed=very_high |  |
| PC5 | H4 | ADC1.INP8 | analog | FMU_BAT1_V |  |  |
| PE7 | H5 | UART7.RX | AF7 | FMU_UART7_RX_TEL1 |  |  |
| PE11 | H6 | TIM1.CH2 | AF1 | FMU_CH2 |  |  |
| PE15 | H7 | gpio_in |  | N_USB_VBUS_VALID | bias=pull_up | Power selector: USB VBUS is the active 5 V source, active low. FMUv6C; on pinion the VBUS is the AM62L's USB-C port. |
| PD14 | H8 | TIM4.CH3 | AF2 | FMU_CH5 |  |  |
| PD10 | H9 | gpio_out |  | N_FMU_LED_RED | initial=high | Status LED, active low, open drain. FMUv6C. |
| PB14 | H10 |  |  |  |  |  |
| VSS_J1 | J1 | reserved |  | GND |  |  |
| PA2 | J2 | ADC1.INP14 | analog | FMU_BAT2_I |  |  |
| PA6 | J3 | SPI1.MISO | AF5 | FMU_SPI1_MISO_SENSOR | speed=very_high |  |
| PB0 | J4 | TIM3.CH3 | AF2 | FMU_BUZZER |  |  |
| PE8 | J5 | UART7.TX | AF7 | FMU_UART7_TX_TEL1 |  |  |
| PE12 | J6 | gpio_out |  | HW_VER_REV_DRIVE | initial=high | Drives the version/revision dividers while they are sampled. FMUv6C. |
| PB10 | J7 | I2C2.SCL | AF4 | FMU_I2C2_SCL_GPS2 | drive=open_drain |  |
| PB13 | J8 | FDCAN2.TX | AF9 | FMU_CAN2_TX |  |  |
| PD9 | J9 | USART3.RX | AF7 | FMU_USART3_RX_DEBUG |  |  |
| PD13 | J10 | I2C4.SDA | AF4 | FMU_I2C4_SDA | drive=open_drain |  |
| VDD_K1 | K1 | reserved |  | FMU_VDD_3V3 |  |  |
| PA3 | K2 | USART2.RX | AF7 | FMU_USART2_RX_TEL3 |  |  |
| PA7 | K3 | SPI1.MOSI | AF5 | FMU_SPI1_MOSI_SENSOR | speed=very_high |  |
| PB1 | K4 | ADC1.INP5 | analog | FMU_BAT2_V |  |  |
| PE9 | K5 | UART7.RTS | AF7 | FMU_UART7_RTS_TEL1 |  |  |
| PE13 | K6 | TIM1.CH3 | AF1 | FMU_CH3 |  |  |
| PB11 | K7 | I2C2.SDA | AF4 | FMU_I2C2_SDA_GPS2 | drive=open_drain |  |
| PB12 | K8 | gpio_in |  | N_BRICK2_VALID | bias=pull_up | Power selector: POWER2 is the active 5 V source, active low. FMUv6C. |
| PD8 | K9 | USART3.TX | AF7 | FMU_USART3_TX_DEBUG |  |  |
| PD12 | K10 | I2C4.SCL | AF4 | FMU_I2C4_SCL | drive=open_drain |  |

## TIM1

FMU PWM 1-4 (AUX). FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| CH1 | PA8 | FMU_CH1 |
| CH2 | PE11 | FMU_CH2 |
| CH3 | PE13 | FMU_CH3 |
| CH4 | PE14 | FMU_CH4 |

## TIM4

FMU PWM 5-6. FMUv6C. PD14 doubles as PWM input capture in PX4.

| Signal | Pin | Net |
|---|---|---|
| CH3 | PD14 | FMU_CH5 |
| CH4 | PD15 | FMU_CH6 |

## TIM5

FMU PWM 7-8. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| CH1 | PA0 | FMU_CH7 |
| CH2 | PA1 | FMU_CH8 |

## TIM3

Tone alarm, to the GPS1 connector buzzer pin. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| CH3 | PB0 | FMU_BUZZER |

## TIM17

IMU heater MOSFET gate. FMUv6C; PX4 drives it as a GPIO.

| Signal | Pin | Net |
|---|---|---|
| CH1 | PB9 | FMU_HEATER |

## ADC1

Power module 1 and 2 current and voltage from the POWER1/POWER2 connectors, and the 5 V rail (divider 2:1). FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| INP4 | PC4 | FMU_BAT1_I |
| INP8 | PC5 | FMU_BAT1_V |
| INP18 | PA4 | FMU_SCALED_V5 |
| INP14 | PA2 | FMU_BAT2_I |
| INP5 | PB1 | FMU_BAT2_V |

## ADC3

Hardware revision and version resistor dividers, driven by HW_VER_REV_DRIVE. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| INP10 | PC0 | HW_REV_SENSE |
| INP11 | PC1 | HW_VER_SENSE |

## SPI1

IMU bus: BMI088 accel (CS1 PC15, DRDY1 PE4), BMI088 gyro (CS2 PC14, DRDY2 PE5), ICM-42688-P (CS3 PC13, DRDY3 PE6). FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| SCK | PA5 | FMU_SPI1_SCK_SENSOR |
| MISO | PA6 | FMU_SPI1_MISO_SENSOR |
| MOSI | PA7 | FMU_SPI1_MOSI_SENSOR |

## SPI2

Parameter storage, CS on PD4. FMUv6C fits an FM25V02A FRAM; the part is undecided on pinion (FRAM or EEPROM). PC2/PC3 are the PC2_C/PC3_C balls on TFBGA100.

| Signal | Pin | Net |
|---|---|---|
| SCK | PD3 | FMU_SPI2_SCK_NVM |
| MISO | PC2 | FMU_SPI2_MISO_NVM |
| MOSI | PC3 | FMU_SPI2_MOSI_NVM |

## I2C4

Internal sensor bus: IST8310 mag 0x0C, MS5611 baro 0x77, calibration EEPROM 0x51. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| SCL | PD12 | FMU_I2C4_SCL |
| SDA | PD13 | FMU_I2C4_SDA |

## I2C1

GPS1 connector: external mag and LED. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| SCL | PB8 | FMU_I2C1_SCL_GPS1 |
| SDA | PB7 | FMU_I2C1_SDA_GPS1 |

## I2C2

GPS2 and I2C connectors. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| SCL | PB10 | FMU_I2C2_SCL_GPS2 |
| SDA | PB11 | FMU_I2C2_SDA_GPS2 |

## USART1

GPS1. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| TX | PB6 | FMU_USART1_TX_GPS1 |
| RX | PA10 | FMU_USART1_RX_GPS1 |

## USART2

TELEM3, no flow control. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| TX | PD5 | FMU_USART2_TX_TEL3 |
| RX | PA3 | FMU_USART2_RX_TEL3 |

## USART3

NSH console on the FMU debug connector. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| TX | PD8 | FMU_USART3_TX_DEBUG |
| RX | PD9 | FMU_USART3_RX_DEBUG |

## UART5

DEVIATION: TELEM2 on the FMUv6C; on pinion it is the on-board MAVLink / uXRCE-DDS link to the AM62L. No external connector.

| Signal | Pin | Net |
|---|---|---|
| TX | PC12 | FMU_UART5_TX_SOC |
| RX | PD2 | FMU_UART5_RX_SOC |
| RTS | PC8 | FMU_UART5_RTS_SOC |
| CTS | PC9 | FMU_UART5_CTS_SOC |

## USART6

PX4IO link to the STM32F103, 1.5 Mbaud. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| TX | PC6 | FMU_USART6_TX_TO_IO |
| RX | PC7 | FMU_USART6_RX_FROM_IO |

## UART7

TELEM1 with flow control. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| TX | PE8 | FMU_UART7_TX_TEL1 |
| RX | PE7 | FMU_UART7_RX_TEL1 |
| RTS | PE9 | FMU_UART7_RTS_TEL1 |
| CTS | PE10 | FMU_UART7_CTS_TEL1 |

## UART8

GPS2. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| TX | PE1 | FMU_UART8_TX_GPS2 |
| RX | PE0 | FMU_UART8_RX_GPS2 |

## FDCAN1

CAN1 transceiver. DEVIATION: the AM62L MCAN0 transceiver sits on the same CAN1 bus.

| Signal | Pin | Net |
|---|---|---|
| RX | PD0 | FMU_CAN1_RX |
| TX | PD1 | FMU_CAN1_TX |

## FDCAN2

CAN2 transceiver. FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| RX | PB5 | FMU_CAN2_RX |
| TX | PB13 | FMU_CAN2_TX |

## USB_OTG_FS

DEVIATION: wired on-board to AM62L USB1 (host) for firmware upload and MAVLink; no external FMU USB connector. VBUS sense is fed from the USB1 VBUS switch.

| Signal | Pin | Net |
|---|---|---|
| DM | PA11 | FMU_USB_DM |
| DP | PA12 | FMU_USB_DP |
| VBUS | PA9 | FMU_VBUS_SENSE |

## DEBUG

SWD on the FMU debug connector (JST-SH 10). FMUv6C.

| Signal | Pin | Net |
|---|---|---|
| JTMS-SWDIO | PA13 | FMU_SWDIO |
| JTCK-SWCLK | PA14 | FMU_SWCLK |

## RCC

16 MHz crystal. FMUv6C. No 32.768 kHz crystal: PC14/PC15 are chip selects.

| Signal | Pin | Net |
|---|---|---|
| OSC_IN | PH0 | FMU_OSC_IN |
| OSC_OUT | PH1 | FMU_OSC_OUT |
