# STM32F103C8T6 pinout (LQFP48, U2)

| Pin | Pad | Function | Mux | Net | Config | Note |
|---|---|---|---|---|---|---|
| VBAT | 1 | reserved |  | FMU_VDD_3V3 |  |  |
| PC13 | 2 | gpio_out |  | IO_VDD_3V3_SPEKTRUM_EN | initial=high | 3.3 V switch for the DSM satellite receiver. PX4 io-v2. |
| PC14 | 3 | gpio_in |  | IO_HW_DETECT1 | bias=pull_down | Board-type sense, left floating (reads low). PX4 io-v2. |
| PC15 | 4 | gpio_in |  | IO_HW_DETECT2 | bias=pull_up | Board-type sense, left floating (reads high). PX4 io-v2. |
| PD0 | 5 | RCC.OSC_IN | fixed | IO_OSC_IN |  |  |
| PD1 | 6 | RCC.OSC_OUT | fixed | IO_OSC_OUT |  |  |
| NRST | 7 | reserved |  | IO_NRST |  | IO debug connector; FMU does not control it. |
| VSSA | 8 | reserved |  | GND |  |  |
| VDDA | 9 | reserved |  | FMU_VDD_3V3 |  | Through a ferrite bead. |
| PA0 | 10 | TIM2.CH1 | vendor(remap=0) | IO_CH1 |  |  |
| PA1 | 11 | TIM2.CH2 | vendor(remap=0) | IO_CH2 |  |  |
| PA2 | 12 | USART2.TX | vendor(remap=0) | FMU_USART6_RX_FROM_IO |  |  |
| PA3 | 13 | USART2.RX | vendor(remap=0) | FMU_USART6_TX_TO_IO |  |  |
| PA4 | 14 | ADC1.IN4 | analog | IO_VSERVO_SENSE |  |  |
| PA5 | 15 | ADC1.IN5 | analog | IO_RSSI_ADC |  |  |
| PA6 | 16 | TIM3.CH1 | vendor(remap=0) | IO_CH5 |  |  |
| PA7 | 17 | TIM3.CH2 | vendor(remap=0) | IO_CH6 |  |  |
| PB0 | 18 | TIM3.CH3 | vendor(remap=0) | IO_CH7 |  |  |
| PB1 | 19 | TIM3.CH4 | vendor(remap=0) | IO_CH8 |  |  |
| PB2 | 20 | reserved |  | GND |  | BOOT1, tied low through a resistor. |
| PB10 | 21 | USART3.TX | vendor(remap=0) | IO_USART3_TX_SBUS_OUT |  |  |
| PB11 | 22 | USART3.RX | vendor(remap=0) | IO_USART3_RX_SBUS_IN |  |  |
| VSS_23 | 23 | reserved |  | GND |  |  |
| VDD_24 | 24 | reserved |  | FMU_VDD_3V3 |  |  |
| PB12 | 25 |  |  |  |  |  |
| PB13 | 26 | gpio_out |  | N_IO_LED_SAFETY | initial=high | Safety switch LED on the GPS1 connector, active low, open drain. PX4 io-v2. |
| PB14 | 27 | gpio_out |  | N_IO_LED_BLUE | initial=high | IO status LED, active low, open drain. PX4 io-v2. |
| PB15 | 28 | gpio_out |  | N_IO_LED_AMBER | initial=high | IO status LED, active low, open drain. PX4 io-v2. |
| PA8 | 29 | TIM1.CH1 | vendor(remap=0) | IO_PPM_IN |  |  |
| PA9 | 30 | USART1.TX | vendor(remap=0) | IO_USART1_TX_DEBUG |  |  |
| PA10 | 31 | USART1.RX | vendor(remap=0) | IO_USART1_RX_DSM |  |  |
| PA11 | 32 | gpio_out |  | IO_LED_GREEN | initial=low | IO power/breathing LED. PX4 io-v2. |
| PA12 | 33 | gpio_in |  | IO_RSSI_PWM |  | PWM RSSI input. PX4 io-v2 (GPIO_TIM_RSSI). |
| PA13 | 34 | SYS.JTMS-SWDIO | fixed | IO_SWDIO |  |  |
| VSS_35 | 35 | reserved |  | GND |  |  |
| VDD_36 | 36 | reserved |  | FMU_VDD_3V3 |  |  |
| PA14 | 37 | SYS.JTCK-SWCLK | fixed | IO_SWCLK |  |  |
| PA15 | 38 | gpio_in |  | N_IO_SERVO_FAULT | bias=pull_up | Servo rail fault detect, active low. PX4 io-v2. |
| PB3 | 39 | SYS.JTDO-TRACESWO | fixed | IO_SWO |  |  |
| PB4 | 40 | gpio_out |  | N_IO_SBUS_OUT_EN | initial=high | S.BUS output driver enable, active low. PX4 io-v2. |
| PB5 | 41 | gpio_in |  | IO_SAFETY_SWITCH |  | Safety switch on the GPS1 connector; external pull-down. PX4 io-v2. |
| PB6 | 42 |  |  |  |  |  |
| PB7 | 43 |  |  |  |  |  |
| BOOT0 | 44 | reserved |  | GND |  | Tied low through a resistor: PX4IO is updated over USART2 by its own bootloader. |
| PB8 | 45 | TIM4.CH3 | vendor(remap=0) | IO_CH3 |  |  |
| PB9 | 46 | TIM4.CH4 | vendor(remap=0) | IO_CH4 |  |  |
| VSS_47 | 47 | reserved |  | GND |  |  |
| VDD_48 | 48 | reserved |  | FMU_VDD_3V3 |  |  |

## TIM2

IO PWM 1-2 (MAIN). PX4 io-v2.

| Signal | Pin | Net |
|---|---|---|
| CH1 | PA0 | IO_CH1 |
| CH2 | PA1 | IO_CH2 |

## TIM4

IO PWM 3-4 (MAIN). PX4 io-v2.

| Signal | Pin | Net |
|---|---|---|
| CH3 | PB8 | IO_CH3 |
| CH4 | PB9 | IO_CH4 |

## TIM3

IO PWM 5-8 (MAIN). PX4 io-v2.

| Signal | Pin | Net |
|---|---|---|
| CH1 | PA6 | IO_CH5 |
| CH2 | PA7 | IO_CH6 |
| CH3 | PB0 | IO_CH7 |
| CH4 | PB1 | IO_CH8 |

## TIM1

PPM input capture, shared with the inverted S.BUS input path at the RC IN connector. PX4 io-v2 (HRT timer 1).

| Signal | Pin | Net |
|---|---|---|
| CH1 | PA8 | IO_PPM_IN |

## USART2

PX4IO link to the FMU (USART6), 1.5 Mbaud. PX4 io-v2.

| Signal | Pin | Net |
|---|---|---|
| TX | PA2 | FMU_USART6_RX_FROM_IO |
| RX | PA3 | FMU_USART6_TX_TO_IO |

## USART1

TX is the IO debug console; RX is the DSM/Spektrum input and is driven as a GPIO during satellite binding. PX4 io-v2.

| Signal | Pin | Net |
|---|---|---|
| TX | PA9 | IO_USART1_TX_DEBUG |
| RX | PA10 | IO_USART1_RX_DSM |

## USART3

S.BUS output (gated by IO_SBUS_OUT_EN) and S.BUS input, both through external inverters. PX4 io-v2.

| Signal | Pin | Net |
|---|---|---|
| TX | PB10 | IO_USART3_TX_SBUS_OUT |
| RX | PB11 | IO_USART3_RX_SBUS_IN |

## ADC1

Servo rail voltage (divider) and analog RSSI. PX4 io-v2.

| Signal | Pin | Net |
|---|---|---|
| IN4 | PA4 | IO_VSERVO_SENSE |
| IN5 | PA5 | IO_RSSI_ADC |

## SYS

SWD and SWO on the IO debug connector.

| Signal | Pin | Net |
|---|---|---|
| JTMS-SWDIO | PA13 | IO_SWDIO |
| JTCK-SWCLK | PA14 | IO_SWCLK |
| JTDO-TRACESWO | PB3 | IO_SWO |

## RCC

24 MHz crystal, as px4_io-v2 expects.

| Signal | Pin | Net |
|---|---|---|
| OSC_IN | PD0 | IO_OSC_IN |
| OSC_OUT | PD1 | IO_OSC_OUT |
