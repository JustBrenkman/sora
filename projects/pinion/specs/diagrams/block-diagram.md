<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# pinion block diagrams

How every block on the board connects. Net names and pins are those in
[`../pinout/`](../pinout/); if a diagram and a pinasg file disagree, the pinasg
file is right. Dashed lines are power or control, solid lines are data.

Parts marked *(select)* are not chosen yet; see
[`../notes/decisions.md`](../notes/decisions.md).

## 1. System

```mermaid
%%{init: {"flowchart": {"curve": "step"}}}%%
flowchart LR
    BAT([POWER1, POWER2<br/>power modules]) --> PWR[Power selector,<br/>rails]
    PWR -.-> SOC
    PWR -.-> FMU
    PWR -.-> IO

    subgraph SBC[Linux computer]
        SOC[AM62L32<br/>U3]
        DDR[DDR4 x16]
        EMMC[eMMC]
        SD[microSD]
        PHY[GbE PHY]
        WL[Wi-Fi / BT module]
        SOC --- DDR
        SOC --- EMMC
        SOC --- SD
        SOC --- PHY
        SOC --- WL
    end

    subgraph FC[Flight controller]
        FMU[STM32H743VIH6<br/>U1, PX4]
        IO[STM32F103<br/>U2, PX4IO]
        SENS[IMUs, mag, baro]
        NVM[Parameter storage]
        FMU --- SENS
        FMU --- NVM
        FMU <-->|USART6 / USART2<br/>1.5 Mbaud| IO
    end

    SOC <-->|UART1 / UART5, RTS/CTS<br/>MAVLink, uXRCE-DDS| FMU
    SOC <-->|USB1 host / OTG_FS device<br/>firmware upload, MAVLink| FMU
    SOC <-->|MCAN0 + transceiver<br/>on the CAN1 bus| FMU

    SOC --- USBC([USB-C])
    PHY --- ETH([Ethernet])
    WL --- ANT([Antenna])
    SOC --- CON([Console, JTAG])
    FMU --- PORTS([TELEM1, TELEM3, GPS1, GPS2,<br/>I2C, CAN1, CAN2, PWM, debug])
    IO --- RC([PWM, RC in, S.BUS out, debug])
```

## 2. Flight controller

```mermaid
%%{init: {"flowchart": {"curve": "step"}}}%%
flowchart LR
    FMU[STM32H743VIH6]

    subgraph IMU[Sensors, VDD_3V3_SENSORS]
        ICM[ICM-42688-P]
        BMI[BMI088 accel + gyro]
        MAG[IST8310<br/>0x0C]
        CAL[24LC64<br/>0x51]
        HTR[Heater]
    end
    BARO[MS5611<br/>0x77]
    NVM[FRAM or EEPROM<br/>undecided]

    FMU <-->|SPI1 PA5/PA6/PA7<br/>CS3 PC13, DRDY3 PE6| ICM
    FMU <-->|SPI1<br/>CS1 PC15, CS2 PC14<br/>DRDY1 PE4, DRDY2 PE5| BMI
    FMU <-->|I2C4 PD12/PD13| MAG
    FMU <-->|I2C4| CAL
    FMU <-->|I2C4| BARO
    FMU -.->|PB9| HTR
    FMU <-->|SPI2 PD3/PC2/PC3<br/>CS PD4| NVM

    FMU <-->|FDCAN1 PD0/PD1| X1[CAN transceiver] <--> CAN1([CAN1])
    FMU <-->|FDCAN2 PB5/PB13| X2[CAN transceiver] <--> CAN2([CAN2])
    SOCX[CAN transceiver<br/>AM62L MCAN0] <--> CAN1

    FMU <-->|UART7 + RTS/CTS| T1([TELEM1])
    FMU <-->|USART2| T3([TELEM3])
    FMU <-->|USART1, I2C1<br/>buzzer PB0| G1([GPS1])
    FMU <-->|UART8, I2C2| G2([GPS2])
    FMU <-->|I2C2| I2C([I2C])
    FMU <-->|USART3, SWD, NRST| DBG([FMU debug])
    FMU -->|TIM1 CH1-4, TIM4 CH3-4,<br/>TIM5 CH1-2| BUF1[Level buffer] --> AUX([FMU PWM 1-8])

    FMU <-->|UART5 + RTS/CTS| SOC[AM62L UART1]
    FMU <-->|OTG_FS PA11/PA12<br/>VBUS sense PA9| SOCU[AM62L USB1]

    FMU <-->|USART6 PC6/PC7| IO[STM32F103]
    IO -->|TIM2 CH1-2, TIM4 CH3-4,<br/>TIM3 CH1-4| BUF2[Level buffer] --> MAIN([IO PWM 1-8])
    RCIN([PPM / S.BUS in, RSSI]) -->|PA8, PB11 via inverter,<br/>PA5, PA12| IO
    IO -->|PB10 via inverter,<br/>enable PB4| SBO([S.BUS out])
    DSM([DSM]) -->|PA10<br/>power PC13| IO
    IO <-->|safety switch PB5,<br/>LED PB13| G1
    IO <-->|USART1 TX, SWD, SWO, NRST| IODBG([IO debug])

    ADC[Battery 1 and 2 V/I, 5 V,<br/>HW version] -->|PC5, PC4, PB1, PA2,<br/>PA4, PC0, PC1| FMU
    SEL[Power selector] -.->|valid: PA15, PB12, PE15| FMU
    FMU -.->|PE2, PC10 enable<br/>PE3, PC11 fault| SW[5 V port switches]
    FMU -.->|PB2| SSW[Sensor rail switch]
```

## 3. Linux computer

```mermaid
%%{init: {"flowchart": {"curve": "step"}}}%%
flowchart LR
    SOC[AM62L32]

    SOC <-->|DDR0, 1.2 V| DDR[DDR4 x16]
    SOC <-->|MMC0, 8 bit, 1.8 V| EMMC[eMMC]
    SOC <-->|MMC1, 4 bit, 3.3/1.8 V<br/>CD, power enable| SD([microSD])
    SOC <-->|RGMII1 + MDIO0, 1.8 V<br/>reset, interrupt| PHY[GbE PHY] <--> MAG[Magnetics] <--> ETH([Ethernet])
    SOC <-->|MMC2 SDIO, 1.8 V| WL[Wi-Fi / BT module]
    SOC <-->|UART5 + RTS/CTS, 1.8 V| WL
    SOC -.->|WLAN_EN, BT_EN,<br/>32 kHz WKUP_CLKOUT0| WL
    WL -.->|WLAN_IRQ| SOC
    WL --- ANT([Antenna])

    SOC <-->|USB0, DRVVBUS| USBC([USB-C])
    SOC <-->|USB1| FMUU[FMU OTG_FS]
    SOC <-->|UART1 + RTS/CTS, 3.3 V| FMUS[FMU UART5]
    SOC <-->|MCAN0, 3.3 V| XCVR[CAN transceiver] <--> CAN1([FMU CAN1 bus])

    SOC <-->|UART0, 3.3 V| CON([Console])
    SOC <-->|JTAG, 1.8 V| JTAG([JTAG])
    SOC <-->|I2C0, 3.3 V| ID[Board ID EEPROM<br/>0x51]
    SOC <-->|WKUP_I2C0, 1.8 V| PMIC[PMIC<br/>0x30]
    PMIC -.->|PORz| SOC
    PMIC -.->|interrupt to EXTINTn| SOC
    SOC -.->|PMIC_LPM_EN0| PMIC
    SOC -.->|RESETSTATz| RST[eMMC, PHY and<br/>module resets]
    BOOT[Boot-mode straps<br/>BOOTMODE 15:0] -.-> SOC
    X25[25 MHz] --- SOC
    X32[32.768 kHz] --- SOC
    SOC -.-> LED([LED])
    BTN([Button]) -.-> SOC
```

## 4. Power tree

The input side follows the FMUv6C. The Linux side is proposed; the 5 V budget
is open (see the decisions note).

```mermaid
%%{init: {"flowchart": {"curve": "step"}}}%%
flowchart LR
    PM1([POWER1<br/>5 V, FMU_BAT1_V, FMU_BAT1_I]) --> SEL[Power selector<br/>ideal diodes]
    PM2([POWER2<br/>5 V, FMU_BAT2_V, FMU_BAT2_I]) --> SEL
    USBV([USB-C VBUS]) --> SEL
    SEL --> BUCK5[VDD_5V]
    SEL -.->|N_BRICK1_VALID, N_BRICK2_VALID,<br/>N_USB_VBUS_VALID| VAL[FMU]

    BUCK5 --> P5[Switch, 1.5 A<br/>VDD_5V_PERIPH]
    BUCK5 --> H5[Switch, 1.5 A<br/>VDD_5V_HIPOWER]
    BUCK5 --> U5[Switch<br/>USB-C VBUS out]
    BUCK5 --> F5[Switch<br/>FMU_VBUS_SENSE]
    BUCK5 --> SCAL[Divider<br/>FMU_SCALED_V5]

    BUCK5 --> F33[3.3 V regulator<br/>FMU_VDD_3V3]
    F33 --> FA[Filter<br/>FMU_VDDA_3V3]
    F33 --> S33[Switch<br/>VDD_3V3_SENSORS]
    F33 --> I33[IO_VDD_3V3]
    I33 --> SPK[Switch<br/>VDD_3V3_SPEKTRUM]

    BUCK5 --> B33[3.3 V buck<br/>VCC_3V3_SYS]
    B33 --> PMIC[TPS6521402]
    PMIC --> C[Buck1 0.75 V<br/>VDD_CORE_0V75, VDDA_CORE_0V75]
    PMIC --> D18[Buck2 1.8 V<br/>SOC_DVDD_1V8]
    PMIC --> DDR[Buck3 1.2 V<br/>VDD_DDR_1V2]
    PMIC --> A18[LDO1 1.8 V<br/>VDDA_1V8]
    PMIC --> D33[LDO2 3.3 V<br/>SOC_DVDD_3V3]
    D33 --> SDL[SoC internal SDIO LDO<br/>VDDSHV_SD_IO]
    B33 --> SDP[Switch<br/>microSD 3.3 V]
    B33 --> VPP[2.5 V LDO<br/>DDR4 VPP]
    DDR --> VTT[VTT / VREF 0.6 V<br/>optional]
    B33 --> RTC[RTC LDOs<br/>0.75 V, 1.8 V]
    B33 --> PHYR[PHY rails<br/>2.5 V, 1.0 V]
    B33 --> WLR[Wi-Fi / BT supply]
```

## 5. Buses

| Bus | Controller pins | Devices | Level |
|---|---|---|---|
| FMU SPI1 | PA5 SCK, PA6 MISO, PA7 MOSI | BMI088 accel (CS PC15, DRDY PE4), BMI088 gyro (CS PC14, DRDY PE5), ICM-42688-P (CS PC13, DRDY PE6) | 3.3 V, sensor rail |
| FMU SPI2 | PD3 SCK, PC2 MISO, PC3 MOSI | Parameter storage (CS PD4) | 3.3 V |
| FMU I2C4 | PD12 SCL, PD13 SDA | IST8310 0x0C, MS5611 0x77, calibration EEPROM 0x51 | 3.3 V, sensor rail |
| FMU I2C1 | PB8 SCL, PB7 SDA | GPS1 connector | 3.3 V |
| FMU I2C2 | PB10 SCL, PB11 SDA | GPS2 and I2C connectors | 3.3 V |
| FMU CAN1 | PD0 RX, PD1 TX | CAN1 connector; AM62L MCAN0 (B15 RX, B16 TX) | bus |
| FMU CAN2 | PB5 RX, PB13 TX | CAN2 connector | bus |
| FMU USART6 | PC6 TX, PC7 RX | IO MCU USART2 (PA3 RX, PA2 TX) | 3.3 V |
| FMU UART5 | PC12 TX, PD2 RX, PC8 RTS, PC9 CTS | AM62L UART1 (C11 RXD, A12 TXD, A8 CTSn, B10 RTSn) | 3.3 V |
| FMU OTG_FS | PA11 DM, PA12 DP | AM62L USB1 (AC5 DM, AB5 DP) | USB |
| SoC I2C0 | B7 SCL, A7 SDA | Board ID EEPROM 0x51 | 3.3 V |
| SoC I2C1 | D7 SCL, A6 SDA | Spare | 3.3 V |
| SoC WKUP_I2C0 | AB22 SCL, AA22 SDA | PMIC 0x30 | 1.8 V |
| SoC MDIO0 | AC15 MDC, AC13 MDIO | Ethernet PHY | 1.8 V |
| SoC UART5 | D18 RXD, C23 TXD, E18 RTSn, E22 CTSn | Bluetooth HCI | 1.8 V |
| SoC MMC2 | R23 CLK, U23 CMD, U22/T22/T23/R22 DAT0-3 | Wi-Fi SDIO | 1.8 V |

## 6. Connectors

| Connector | Type | Signals |
|---|---|---|
| POWER1, POWER2 | JST-GH 6 | 5 V, 5 V, CURRENT, VOLTAGE, GND, GND |
| TELEM1 | JST-GH 6 | VDD_5V_HIPOWER, UART7 TX, RX, CTS, RTS, GND |
| TELEM3 | JST-GH 6 | VDD_5V_PERIPH, USART2 TX, RX, NC, NC, GND |
| GPS1 | JST-GH 10 | VDD_5V_PERIPH, USART1 TX, RX, I2C1 SCL, SDA, safety switch, safety LED, 3V3, buzzer, GND |
| GPS2 | JST-GH 6 | VDD_5V_HIPOWER, UART8 TX, RX, I2C2 SCL, SDA, GND |
| I2C | JST-GH 4 | VDD_5V_PERIPH, I2C2 SCL, SDA, GND |
| CAN1, CAN2 | JST-GH 4 | VDD_5V_PERIPH, CAN_H, CAN_L, GND |
| FMU PWM | JST-GH 10 | VDD_SERVO, FMU_CH1..8, GND |
| IO PWM | JST-GH 10 | VDD_SERVO, IO_CH1..8, GND |
| DSM | JST-ZH 3 | VDD_3V3_SPEKTRUM, GND, DSM in |
| PPM/SBUS RC | JST-GH 5 | 5 V, PPM/S.BUS in, RSSI in, NC, GND |
| SBUS OUT | JST-GH 3 | NC, S.BUS out, GND |
| FMU debug | JST-SH 10 | 3V3, USART3 TX, RX, SWDIO, SWCLK, NC, NC, NC, NRST, GND |
| IO debug | JST-SH 10 | 3V3, USART1 TX, NC, SWDIO, SWCLK, SWO, NC, NC, NRST, GND |
| USB-C | USB 2.0 Type-C | AM62L USB0 |
| Ethernet | *(select)* | 4 pairs from the PHY magnetics |
| microSD | push-push socket | AM62L MMC1 |
| SoC console | *(select)* | UART0 TX, RX, GND |
| SoC JTAG | *(select)* | TCK, TMS, TDI, TDO, TRSTn, EMU0, EMU1, 1.8 V reference, GND |
| Antenna | U.FL or chip antenna *(select)* | Wi-Fi / BT |
