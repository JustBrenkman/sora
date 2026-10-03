# AM62L32 pinout (ANB, U3)

| Pin | Pad | Function | Mux | Net | Config | Note |
|---|---|---|---|---|---|---|
| VSS_A1 | A1 | reserved |  | GND |  |  |
| VSS_A2 | A2 | reserved |  | GND |  |  |
| MMC0_DAT6 | A3 | MMC0.DAT6 | vendor(muxmode=0) | EMMC_DAT6 |  |  |
| VSS_A4 | A4 | reserved |  | GND |  |  |
| USB1_DRVVBUS | A5 | USB1.DRVVBUS | vendor(muxmode=0) | FMU_USB_VBUS_EN |  |  |
| I2C1_SDA | A6 | I2C1.SDA | vendor(muxmode=0) | SOC_I2C1_SDA | drive=open_drain |  |
| I2C0_SDA | A7 | I2C0.SDA | vendor(muxmode=0) | SOC_I2C0_SDA | drive=open_drain |  |
| MCASP0_AXR3 | A8 | UART1.CTSn | vendor(muxmode=2) | FMU_UART5_RTS_SOC |  |  |
| MCASP0_AXR1 | A9 |  |  |  |  |  |
| VSS_A10 | A10 | reserved |  | GND |  |  |
| MCASP0_ACLKX | A11 |  |  |  |  |  |
| MCASP0_ACLKR | A12 | UART1.TXD | vendor(muxmode=2) | FMU_UART5_RX_SOC |  |  |
| VSS_A13 | A13 | reserved |  | GND |  |  |
| DSI0_TXCLKP | A14 | reserved |  |  |  |  |
| DSI0_TXCLKN | A15 | reserved |  |  |  |  |
| VSS_A16 | A16 | reserved |  | GND |  |  |
| DSI0_TXP1 | A17 | reserved |  |  |  |  |
| DSI0_TXN1 | A18 | reserved |  |  |  |  |
| VSS_A19 | A19 | reserved |  | GND |  |  |
| DSI0_TXN2 | A20 | reserved |  |  |  |  |
| DSI0_TXP2 | A21 | reserved |  |  |  |  |
| VSS_A22 | A22 | reserved |  | GND |  |  |
| VSS_A23 | A23 | reserved |  | GND |  |  |
| VSS_B1 | B1 | reserved |  | GND |  |  |
| MMC0_CLK | B2 | MMC0.CLK | vendor(muxmode=0) | EMMC_CLK |  |  |
| MMC0_DAT5 | B3 | MMC0.DAT5 | vendor(muxmode=0) | EMMC_DAT5 |  |  |
| MMC0_DAT7 | B4 | MMC0.DAT7 | vendor(muxmode=0) | EMMC_DAT7 |  |  |
| VSS_B5 | B5 | reserved |  | GND |  |  |
| MMC1_SDCD | B6 | MMC1.SDCD | vendor(muxmode=0) | SD_CD |  |  |
| I2C0_SCL | B7 | I2C0.SCL | vendor(muxmode=0) | SOC_I2C0_SCL | drive=open_drain |  |
| I2C2_SCL | B8 |  |  |  |  |  |
| MCASP0_AXR0 | B9 |  |  |  |  |  |
| MCASP0_AXR2 | B10 | UART1.RTSn | vendor(muxmode=2) | FMU_UART5_CTS_SOC |  |  |
| MCASP0_AFSX | B11 |  |  |  |  |  |
| SPI0_D1 | B12 | gpio_in |  | N_SOC_USER_BTN | bias=pull_up | GPIO0_91, 3.3 V: user button. As the EVM. |
| UART0_RTSn | B13 |  |  |  |  |  |
| UART0_CTSn | B14 |  |  |  |  |  |
| MCAN0_RX | B15 | MCAN0.RX | vendor(muxmode=0) | SOC_CAN_RX |  |  |
| MCAN0_TX | B16 | MCAN0.TX | vendor(muxmode=0) | SOC_CAN_TX |  |  |
| VSS_B17 | B17 | reserved |  | GND |  |  |
| DSI0_TXP0 | B18 | reserved |  |  |  |  |
| DSI0_TXN0 | B19 | reserved |  |  |  |  |
| VSS_B20 | B20 | reserved |  | GND |  |  |
| DSI0_TXP3 | B21 | reserved |  |  |  |  |
| DSI0_TXN3 | B22 | reserved |  |  |  |  |
| VSS_B23 | B23 | reserved |  | GND |  |  |
| MMC0_DAT2 | C1 | MMC0.DAT2 | vendor(muxmode=0) | EMMC_DAT2 |  |  |
| MMC0_DAT3 | C2 | MMC0.DAT3 | vendor(muxmode=0) | EMMC_DAT3 |  |  |
| MMC0_DAT4 | C4 | MMC0.DAT4 | vendor(muxmode=0) | EMMC_DAT4 |  |  |
| USB0_DRVVBUS | C6 | USB0.DRVVBUS | vendor(muxmode=0) | USBC_VBUS_EN |  |  |
| EXTINTn | C8 | SYS.EXTINTn | vendor(muxmode=0) | N_PMIC_INT |  |  |
| MCASP0_AFSR | C11 | UART1.RXD | vendor(muxmode=2) | FMU_UART5_TX_SOC |  |  |
| VSS_C12 | C12 | reserved |  | GND |  |  |
| UART0_TXD | C13 | UART0.TXD | vendor(muxmode=0) | SOC_UART0_TX |  |  |
| RESETSTATz | C16 | SYS.RESETSTATz | vendor(muxmode=0) | SOC_RESETSTATZ |  |  |
| VSS_C18 | C18 | reserved |  | GND |  |  |
| OSPI0_CSn0 | C20 |  |  |  |  |  |
| OSPI0_D0 | C22 |  |  |  |  |  |
| OSPI0_CSn3 | C23 | UART5.TXD | vendor(muxmode=5) | BT_UART_RX |  |  |
| VSS_D1 | D1 | reserved |  | GND |  |  |
| MMC0_CMD | D2 | MMC0.CMD | vendor(muxmode=0) | EMMC_CMD |  |  |
| MMC0_DAT0 | D3 | MMC0.DAT0 | vendor(muxmode=0) | EMMC_DAT0 |  |  |
| MMC0_DAT1 | D4 | MMC0.DAT1 | vendor(muxmode=0) | EMMC_DAT1 |  |  |
| MMC1_SDWP | D6 | gpio_out |  | SD_PWR_EN | initial=high | GPIO0_123: microSD 3.3 V load switch enable, so the card can be power-cycled out of 1.8 V signalling. As the EVM. |
| I2C1_SCL | D7 | I2C1.SCL | vendor(muxmode=0) | SOC_I2C1_SCL | drive=open_drain |  |
| I2C2_SDA | D8 |  |  |  |  |  |
| SPI0_CS1 | D11 |  |  |  |  |  |
| UART0_RXD | D13 | UART0.RXD | vendor(muxmode=0) | SOC_UART0_RX |  |  |
| EXT_REFCLK1 | D16 |  |  |  |  |  |
| DSI0_TXRCALIB | D17 | reserved |  |  |  | DSI is not used: all DSI0 signal balls are left unconnected (datasheet section 5.4). The DSI supplies stay powered so boundary scan keeps working. |
| OSPI0_CSn2 | D18 | UART5.RXD | vendor(muxmode=5) | BT_UART_TX |  |  |
| OSPI0_CSn1 | D20 |  |  |  |  |  |
| OSPI0_D1 | D21 |  |  |  |  |  |
| OSPI0_CLK | D22 |  |  |  |  |  |
| OSPI0_D3 | D23 |  |  |  |  |  |
| DDR0_DQ3 | E1 | DDR0.DQ3 | fixed | DDR_DQ3 |  |  |
| VSS_E2 | E2 | reserved |  | GND |  |  |
| VSS_E6 | E6 | reserved |  | GND |  |  |
| VSS_E8 | E8 | reserved |  | GND |  |  |
| VSS_E9 | E9 | reserved |  | GND |  |  |
| VSS_E10 | E10 | reserved |  | GND |  |  |
| SPI0_CS0 | E11 | gpio_out |  | SOC_LED_STATUS | initial=low | GPIO0_87, 3.3 V: heartbeat LED. |
| SPI0_D0 | E12 |  |  |  |  |  |
| SPI0_CLK | E13 |  |  |  |  |  |
| VSS_E14 | E14 | reserved |  | GND |  |  |
| VSS_E15 | E15 | reserved |  | GND |  |  |
| RESETz | E16 | SYS.RESETz | vendor(muxmode=0) | SOC_RESETZ |  |  |
| OSPI0_LBCLKO | E18 | UART5.RTSn | vendor(muxmode=5) | BT_UART_CTS |  |  |
| OSPI0_DQS | E22 | UART5.CTSn | vendor(muxmode=5) | BT_UART_RTS |  |  |
| OSPI0_D2 | E23 |  |  |  |  |  |
| DDR0_DQ2 | F1 | DDR0.DQ2 | fixed | DDR_DQ2 |  |  |
| DDR0_DM0 | F2 | DDR0.DM0 | fixed | DDR_DM0 |  |  |
| DDR0_DQ1 | F3 | DDR0.DQ1 | fixed | DDR_DQ1 |  |  |
| DDR0_DQ0 | F4 | DDR0.DQ0 | fixed | DDR_DQ0 |  |  |
| VSS_F5 | F5 | reserved |  | GND |  |  |
| VSS_F6 | F6 | reserved |  | GND |  |  |
| VSS_F18 | F18 | reserved |  | GND |  |  |
| OSPI0_D5 | F19 |  |  |  |  |  |
| OSPI0_D7 | F20 |  |  |  |  |  |
| OSPI0_D4 | F21 | gpio_in |  | WLAN_IRQ |  | GPIO0_7, 1.8 V: Wi-Fi out-of-band interrupt / host wake. |
| GPMC0_AD14 | F22 | SYS.BOOTMODE14 | fixed | SOC_BOOTMODE14 |  |  |
| GPMC0_AD15 | F23 | SYS.BOOTMODE15 | fixed | SOC_BOOTMODE15 |  |  |
| DDR0_DQS0 | G1 | DDR0.DQS0 | fixed | DDR_DQS0 |  |  |
| DDR0_DQS0_n | G2 | DDR0.DQS0_n | fixed | DDR_DQS0_N |  |  |
| DDR0_DQ4 | G4 | DDR0.DQ4 | fixed | DDR_DQ4 |  |  |
| VSS_G7 | G7 | reserved |  | GND |  |  |
| VSS_G8 | G8 | reserved |  | GND |  |  |
| VSS_G9 | G9 | reserved |  | GND |  |  |
| VDDSHV1_G10 | G10 | reserved |  | SOC_DVDD_3V3 |  | 3.3 V: console, I2C0/1, CAN, FMU UART. |
| CAP_VDDS_GENERAL1 | G11 | reserved |  | SOC_CAP_VDDS_GENERAL1 |  |  |
| VSS_G12 | G12 | reserved |  | GND |  |  |
| VDDA_CORE_DSI | G13 | reserved |  | VDDA_CORE_0V75 |  |  |
| VDDA_1P8_DSI | G14 | reserved |  | VDDA_1V8 |  |  |
| VSS_G15 | G15 | reserved |  | GND |  |  |
| VSS_G16 | G16 | reserved |  | GND |  |  |
| VSS_G17 | G17 | reserved |  | GND |  |  |
| OSPI0_D6 | G20 |  |  |  |  |  |
| GPMC0_AD13 | G22 | SYS.BOOTMODE13 | fixed | SOC_BOOTMODE13 |  |  |
| GPMC0_AD12 | G23 | SYS.BOOTMODE12 | fixed | SOC_BOOTMODE12 |  |  |
| VSS_H1 | H1 | reserved |  | GND |  |  |
| DDR0_DQ6 | H2 | DDR0.DQ6 | fixed | DDR_DQ6 |  |  |
| DDR0_DQ7 | H3 | DDR0.DQ7 | fixed | DDR_DQ7 |  |  |
| DDR0_DQ5 | H4 | DDR0.DQ5 | fixed | DDR_DQ5 |  |  |
| DDR0_A5 | H5 | DDR0.A5 | fixed | DDR_A5 |  |  |
| DDR0_A1 | H6 | DDR0.A1 | fixed | DDR_A1 |  |  |
| VSS_H7 | H7 | reserved |  | GND |  |  |
| VDDSHV2 | H8 | reserved |  | SOC_DVDD_1V8 |  | 1.8 V: eMMC HS200. |
| VDDSHV1_H10 | H10 | reserved |  | SOC_DVDD_3V3 |  |  |
| VDDA_CORE_DSI_CLK | H12 | reserved |  | VDDA_CORE_0V75 |  |  |
| VSS_H14 | H14 | reserved |  | GND |  |  |
| VDDS1 | H16 | reserved |  | SOC_DVDD_1V8 |  |  |
| VSS_H17 | H17 | reserved |  | GND |  |  |
| GPMC0_AD11 | H18 | SYS.BOOTMODE11 | fixed | SOC_BOOTMODE11 |  |  |
| GPMC0_AD8 | H19 | SYS.BOOTMODE08 | fixed | SOC_BOOTMODE8 |  |  |
| GPMC0_AD9 | H20 | SYS.BOOTMODE09 | fixed | SOC_BOOTMODE9 |  |  |
| GPMC0_AD10 | H21 | SYS.BOOTMODE10 | fixed | SOC_BOOTMODE10 |  |  |
| GPMC0_AD5 | H22 | SYS.BOOTMODE05 | fixed | SOC_BOOTMODE5 |  |  |
| GPMC0_AD6 | H23 | SYS.BOOTMODE06 | fixed | SOC_BOOTMODE6 |  |  |
| DDR0_A4 | J1 | DDR0.A4 | fixed | DDR_A4 |  |  |
| DDR0_RESET0_n | J2 | DDR0.RESET0_n | fixed | DDR_RESET0_N |  |  |
| CAP_VDDS_MMC0 | J8 | reserved |  | SOC_CAP_VDDS_MMC0 |  |  |
| VDD_CORE_J9 | J9 | reserved |  | VDD_CORE_0V75 |  |  |
| VDD_CORE_J11 | J11 | reserved |  | VDD_CORE_0V75 |  |  |
| VDD_CORE_J13 | J13 | reserved |  | VDD_CORE_0V75 |  |  |
| VDD_CORE_J15 | J15 | reserved |  | VDD_CORE_0V75 |  |  |
| VDDSHV0_J16 | J16 | reserved |  | SOC_DVDD_3V3 |  | 3.3 V: boot-mode straps and spare GPIO. |
| GPMC0_AD7 | J22 | SYS.BOOTMODE07 | fixed | SOC_BOOTMODE7 |  |  |
| GPMC0_AD3 | J23 | SYS.BOOTMODE03 | fixed | SOC_BOOTMODE3 |  |  |
| DDR0_CKE0 | K1 | DDR0.CKE0 | fixed | DDR_CKE0 |  |  |
| DDR0_A3 | K2 | DDR0.A3 | fixed | DDR_A3 |  |  |
| VSS_K8 | K8 | reserved |  | GND |  |  |
| VSS_K9 | K9 | reserved |  | GND |  |  |
| VDD_CORE_K10 | K10 | reserved |  | VDD_CORE_0V75 |  |  |
| VDDA_PLL1 | K12 | reserved |  | VDDA_1V8 |  |  |
| VDD_CORE_K14 | K14 | reserved |  | VDD_CORE_0V75 |  |  |
| VSS_K15 | K15 | reserved |  | GND |  |  |
| CAP_VDDS_GPMC | K16 | reserved |  | SOC_CAP_VDDS_GPMC |  |  |
| GPMC0_AD2 | K22 | SYS.BOOTMODE02 | fixed | SOC_BOOTMODE2 |  |  |
| GPMC0_AD4 | K23 | SYS.BOOTMODE04 | fixed | SOC_BOOTMODE4 |  |  |
| DDR0_CAS_n | L1 | DDR0.CAS_n | fixed | DDR_CAS_N |  |  |
| DDR0_WE_n | L2 | DDR0.WE_n | fixed | DDR_WE_N |  |  |
| DDR0_CS0_n | L3 | DDR0.CS0_n | fixed | DDR_CS0_N |  |  |
| DDR0_ODT0 | L4 | DDR0.ODT0 | fixed | DDR_ODT0 |  |  |
| DDR0_A0 | L5 | DDR0.A0 | fixed | DDR_A0 |  |  |
| DDR0_A2 | L6 | DDR0.A2 | fixed | DDR_A2 |  |  |
| VSS_L7 | L7 | reserved |  | GND |  |  |
| VDDS_DDR_L8 | L8 | reserved |  | VDD_DDR_1V2 |  | 1.2 V for DDR4 (the EVM runs 1.1 V for LPDDR4). |
| VSS_L9 | L9 | reserved |  | GND |  |  |
| VDDA_PLL0 | L11 | reserved |  | VDDA_1V8 |  |  |
| VSS_L13 | L13 | reserved |  | GND |  |  |
| VDD_CORE_L15 | L15 | reserved |  | VDD_CORE_0V75 |  |  |
| VSS_L16 | L16 | reserved |  | GND |  |  |
| VDDSHV0_L17 | L17 | reserved |  | SOC_DVDD_3V3 |  |  |
| VSS_L18 | L18 | reserved |  | GND |  |  |
| GPMC0_CSn1 | L19 |  |  |  |  |  |
| GPMC0_CSn0 | L20 |  |  |  |  |  |
| GPMC0_CLK | L21 |  |  |  |  |  |
| GPMC0_AD0 | L22 | SYS.BOOTMODE00 | fixed | SOC_BOOTMODE0 |  |  |
| GPMC0_AD1 | L23 | SYS.BOOTMODE01 | fixed | SOC_BOOTMODE1 |  |  |
| VSS_M1 | M1 | reserved |  | GND |  |  |
| DDR0_ACT_n | M2 | DDR0.ACT_n | fixed | DDR_ACT_N |  |  |
| DDR0_CAL0 | M3 | DDR0.CAL0 | analog | DDR_CAL0 |  |  |
| DDR0_RAS_n | M5 | DDR0.RAS_n | fixed | DDR_RAS_N |  |  |
| VDDS_DDR_M7 | M7 | reserved |  | VDD_DDR_1V2 |  |  |
| VDDS_DDR_M8 | M8 | reserved |  | VDD_DDR_1V2 |  |  |
| VDDA_DDR_PLL0 | M10 | reserved |  | VDD_CORE_0V75 |  |  |
| VSS_M12 | M12 | reserved |  | GND |  |  |
| VDD_CORE_M14 | M14 | reserved |  | VDD_CORE_0V75 |  |  |
| CAP_VDDS_MMC2 | M16 | reserved |  | SOC_CAP_VDDS_MMC2 |  |  |
| VDDSHV4 | M17 | reserved |  | SOC_DVDD_1V8 |  | 1.8 V: Wi-Fi SDIO. |
| GPMC0_WEn | M19 |  |  |  |  |  |
| GPMC0_DIR | M21 |  |  |  |  |  |
| GPMC0_CSn3 | M22 |  |  |  |  |  |
| GPMC0_CSn2 | M23 |  |  |  |  |  |
| DDR0_A9 | N1 | DDR0.A9 | fixed | DDR_A9 |  |  |
| DDR0_BA1 | N2 | DDR0.BA1 | fixed | DDR_BA1 |  |  |
| DDR0_BA0 | N3 | DDR0.BA0 | fixed | DDR_BA0 |  |  |
| DDR0_BG1 | N4 |  |  |  |  |  |
| DDR0_BG0 | N5 | DDR0.BG0 | fixed | DDR_BG0 |  |  |
| DDR0_A7 | N6 | DDR0.A7 | fixed | DDR_A7 |  |  |
| VSS_N7 | N7 | reserved |  | GND |  |  |
| VDDS_DDR_N8 | N8 | reserved |  | VDD_DDR_1V2 |  |  |
| VSS_N9 | N9 | reserved |  | GND |  |  |
| VSS_N11 | N11 | reserved |  | GND |  |  |
| VSS_N13 | N13 | reserved |  | GND |  |  |
| VDD_CORE_N15 | N15 | reserved |  | VDD_CORE_0V75 |  |  |
| VSS_N16 | N16 | reserved |  | GND |  |  |
| VDDA_ADC | N17 | reserved |  | GND |  | ADC0 is not used: VDDA_ADC and ADC0_AIN[3:0] connect directly to VSS (datasheet section 5.4). |
| VPP | N18 | reserved |  | VPP_1V8 |  | eFuse programming supply: 1.8 V only while programming, otherwise off. As the EVM. |
| GPMC0_ADVn_ALE | N19 |  |  |  |  |  |
| GPMC0_OEn_REn | N20 |  |  |  |  |  |
| GPMC0_WPn | N21 |  |  |  |  |  |
| GPMC0_WAIT1 | N22 |  |  |  |  |  |
| GPMC0_WAIT0 | N23 |  |  |  |  |  |
| DDR0_CK0 | P1 | DDR0.CK0 | fixed | DDR_CK0 |  |  |
| DDR0_CK0_n | P2 | DDR0.CK0_n | fixed | DDR_CK0_N |  |  |
| VDDS_DDR_P8 | P8 | reserved |  | VDD_DDR_1V2 |  |  |
| VSS_P9 | P9 | reserved |  | GND |  |  |
| VDD_CORE_P10 | P10 | reserved |  | VDD_CORE_0V75 |  |  |
| VDD_CORE_P12 | P12 | reserved |  | VDD_CORE_0V75 |  |  |
| VDD_CORE_P14 | P14 | reserved |  | VDD_CORE_0V75 |  |  |
| VSS_P15 | P15 | reserved |  | GND |  |  |
| VDDS_WKUP | P16 | reserved |  | SOC_DVDD_1V8 |  |  |
| GPMC0_BE1n | P22 |  |  |  |  |  |
| GPMC0_BE0n_CLE | P23 |  |  |  |  |  |
| VSS_R1 | R1 | reserved |  | GND |  |  |
| DDR0_A6 | R2 | DDR0.A6 | fixed | DDR_A6 |  |  |
| VSS_R8 | R8 | reserved |  | GND |  |  |
| VDD_CORE_R9 | R9 | reserved |  | VDD_CORE_0V75 |  |  |
| VDD_CORE_R11 | R11 | reserved |  | VDD_CORE_0V75 |  |  |
| VSS_R13 | R13 | reserved |  | GND |  |  |
| VSS_R15 | R15 | reserved |  | GND |  |  |
| VDDS_OSC0 | R16 | reserved |  | VDDA_1V8 |  |  |
| MMC2_DAT3 | R22 | MMC2.DAT3 | vendor(muxmode=0) | WLAN_SDIO_D3 |  |  |
| MMC2_CLK | R23 | MMC2.CLK | vendor(muxmode=0) | WLAN_SDIO_CLK |  |  |
| DDR0_DQ10 | T1 | DDR0.DQ10 | fixed | DDR_DQ10 |  |  |
| VSS_T2 | T2 | reserved |  | GND |  |  |
| DDR0_DQ9 | T3 | DDR0.DQ9 | fixed | DDR_DQ9 |  |  |
| DDR0_A8 | T4 | DDR0.A8 | fixed | DDR_A8 |  |  |
| DDR0_A10 | T5 | DDR0.A10 | fixed | DDR_A10 |  |  |
| DDR0_A11 | T6 | DDR0.A11 | fixed | DDR_A11 |  |  |
| VSS_T7 | T7 | reserved |  | GND |  |  |
| VSS_T8 | T8 | reserved |  | GND |  |  |
| VDDSHV3 | T10 | reserved |  | VDDSHV_SD_IO |  | Fed by the internal SDIO LDO output, CAP_VDDSHV_MMC, with 3.3 uF to GND. |
| VDDA_1P8_USB | T12 | reserved |  | VDDA_1V8 |  |  |
| VDDS0 | T14 | reserved |  | SOC_DVDD_1V8 |  |  |
| CAP_VDDSHV_MMC | T16 | reserved |  | VDDSHV_SD_IO |  |  |
| VDD_RTC | T17 | reserved |  | SOC_VDD_RTC_0V75 |  |  |
| VDDS_RTC | T18 | reserved |  | SOC_VDDS_RTC_1V8 |  |  |
| VSS_T19 | T19 | reserved |  | GND |  |  |
| MMC2_SDCD | T20 | gpio_out |  | WLAN_EN | initial=low | GPIO0_51, 1.8 V: Wi-Fi enable. |
| MMC2_SDWP | T21 | gpio_out |  | BT_EN | initial=low | GPIO0_52, 1.8 V: Bluetooth enable. |
| MMC2_DAT1 | T22 | MMC2.DAT1 | vendor(muxmode=0) | WLAN_SDIO_D1 |  |  |
| MMC2_DAT2 | T23 | MMC2.DAT2 | vendor(muxmode=0) | WLAN_SDIO_D2 |  |  |
| DDR0_DQ11 | U1 | DDR0.DQ11 | fixed | DDR_DQ11 |  |  |
| DDR0_DQ14 | U2 | DDR0.DQ14 | fixed | DDR_DQ14 |  |  |
| DDR0_DQ12 | U4 | DDR0.DQ12 | fixed | DDR_DQ12 |  |  |
| VSS_U7 | U7 | reserved |  | GND |  |  |
| VSS_U8 | U8 | reserved |  | GND |  |  |
| CAP_VDDS_MMC1 | U9 | reserved |  | SOC_CAP_VDDS_MMC1 |  |  |
| VSS_U10 | U10 | reserved |  | GND |  |  |
| VDDA_CORE_USB | U11 | reserved |  | VDDA_CORE_0V75 |  |  |
| VDDA_3P3_USB | U12 | reserved |  | SOC_DVDD_3V3 |  |  |
| VSS_U13 | U13 | reserved |  | GND |  |  |
| VSS_U14 | U14 | reserved |  | GND |  |  |
| VSS_U15 | U15 | reserved |  | GND |  |  |
| VDDA_3P3_SDIO | U16 | reserved |  | SOC_DVDD_3V3 |  |  |
| VSS_U17 | U17 | reserved |  | GND |  |  |
| VSS_U20 | U20 | reserved |  | GND |  |  |
| MMC2_DAT0 | U22 | MMC2.DAT0 | vendor(muxmode=0) | WLAN_SDIO_D0 |  |  |
| MMC2_CMD | U23 | MMC2.CMD | vendor(muxmode=0) | WLAN_SDIO_CMD |  |  |
| DDR0_DQS1 | V1 | DDR0.DQS1 | fixed | DDR_DQS1 |  |  |
| DDR0_DQS1_n | V2 | DDR0.DQS1_n | fixed | DDR_DQS1_N |  |  |
| VSS_V3 | V3 | reserved |  | GND |  |  |
| DDR0_DQ8 | V4 | DDR0.DQ8 | fixed | DDR_DQ8 |  |  |
| DDR0_DQ13 | V5 | DDR0.DQ13 | fixed | DDR_DQ13 |  |  |
| DDR0_A13 | V6 | DDR0.A13 | fixed | DDR_A13 |  |  |
| VSS_V18 | V18 | reserved |  | GND |  |  |
| VSS_V19 | V19 | reserved |  | GND |  |  |
| ADC0_AIN0 | V20 | reserved |  | GND |  |  |
| ADC0_AIN3 | V21 | reserved |  | GND |  |  |
| ADC0_AIN1 | V22 | reserved |  | GND |  |  |
| ADC0_AIN2 | V23 | reserved |  | GND |  |  |
| DDR0_DQ15 | W1 | DDR0.DQ15 | fixed | DDR_DQ15 |  |  |
| DDR0_DM1 | W2 | DDR0.DM1 | fixed | DDR_DM1 |  |  |
| DDR0_A12 | W6 | DDR0.A12 | fixed | DDR_A12 |  |  |
| RGMII1_RD3 | W8 | RGMII1.RD3 | vendor(muxmode=0) | ETH_RD3 |  |  |
| VSS_W9 | W9 | reserved |  | GND |  |  |
| VSS_W10 | W10 | reserved |  | GND |  |  |
| RGMII1_TXC | W11 | RGMII1.TXC | vendor(muxmode=0) | ETH_TXC |  |  |
| VSS_W12 | W12 | reserved |  | GND |  |  |
| RGMII1_TD1 | W13 | RGMII1.TD1 | vendor(muxmode=0) | ETH_TD1 |  |  |
| VSS_W14 | W14 | reserved |  | GND |  |  |
| VSS_W15 | W15 | reserved |  | GND |  |  |
| VSS_W16 | W16 | reserved |  | GND |  |  |
| VSS_W18 | W18 | reserved |  | GND |  |  |
| WKUP_UART0_RTSn | W22 |  |  |  |  |  |
| WKUP_UART0_CTSn | W23 |  |  |  |  |  |
| VSS_Y1 | Y1 | reserved |  | GND |  |  |
| MMC1_CLK | Y2 | MMC1.CLK | vendor(muxmode=0) | SD_CLK |  |  |
| MMC1_CMD | Y3 | MMC1.CMD | vendor(muxmode=0) | SD_CMD |  |  |
| MMC1_DAT1 | Y4 | MMC1.DAT1 | vendor(muxmode=0) | SD_DAT1 |  |  |
| RGMII1_RX_CTL | Y6 | RGMII1.RX_CTL | vendor(muxmode=0) | ETH_RX_CTL |  |  |
| RGMII1_RXC | Y7 | RGMII1.RXC | vendor(muxmode=0) | ETH_RXC |  |  |
| RGMII1_RD0 | Y8 | RGMII1.RD0 | vendor(muxmode=0) | ETH_RD0 |  |  |
| RGMII1_TD2 | Y11 | RGMII1.TD2 | vendor(muxmode=0) | ETH_TD2 |  |  |
| RGMII2_TXC | Y13 |  |  |  |  |  |
| EMU0 | Y16 | SYS.EMU0 | vendor(muxmode=0) | SOC_JTAG_EMU0 |  |  |
| TMS | Y17 | SYS.TMS | vendor(muxmode=0) | SOC_JTAG_TMS |  |  |
| RTC_PORz | Y18 | RTC.PORz | fixed | SOC_RTC_PORZ |  |  |
| VSS_Y20 | Y20 | reserved |  | GND |  |  |
| VSS_Y21 | Y21 | reserved |  | GND |  |  |
| WKUP_UART0_RXD | Y22 | WKUP_UART0.RXD | vendor(muxmode=0) | SOC_WKUP_UART0_RX |  |  |
| WKUP_CLKOUT0 | Y23 | WKUP.CLKOUT0 | vendor(muxmode=0) | WLAN_SLOW_CLK |  |  |
| MMC1_DAT0 | AA1 | MMC1.DAT0 | vendor(muxmode=0) | SD_DAT0 |  |  |
| MMC1_DAT2 | AA2 | MMC1.DAT2 | vendor(muxmode=0) | SD_DAT2 |  |  |
| VSS_AA4 | AA4 | reserved |  | GND |  |  |
| RGMII1_RD1 | AA6 | RGMII1.RD1 | vendor(muxmode=0) | ETH_RD1 |  |  |
| RGMII1_RD2 | AA8 | RGMII1.RD2 | vendor(muxmode=0) | ETH_RD2 |  |  |
| RGMII1_TD3 | AA11 | RGMII1.TD3 | vendor(muxmode=0) | ETH_TD3 |  |  |
| RGMII2_TD2 | AA12 |  |  |  |  |  |
| RGMII2_TD3 | AA13 |  |  |  |  |  |
| EMU1 | AA16 | SYS.EMU1 | vendor(muxmode=0) | SOC_JTAG_EMU1 |  |  |
| PMIC_LPM_EN0 | AA18 | PMIC.LPM_EN0 | fixed | PMIC_LPM_EN0 |  |  |
| VSS_AA20 | AA20 | reserved |  | GND |  |  |
| WKUP_I2C0_SDA | AA22 | WKUP_I2C0.SDA | vendor(muxmode=0) | PMIC_I2C_SDA | drive=open_drain |  |
| WKUP_UART0_TXD | AA23 | WKUP_UART0.TXD | vendor(muxmode=0) | SOC_WKUP_UART0_TX |  |  |
| VSS_AB1 | AB1 | reserved |  | GND |  |  |
| MMC1_DAT3 | AB2 | MMC1.DAT3 | vendor(muxmode=0) | SD_DAT3 |  |  |
| USB0_RCALIB | AB3 | USB0.RCALIB | fixed | SOC_USB0_RCALIB |  |  |
| USB0_DP | AB4 | USB0.DP | fixed | USBC_DP |  |  |
| USB1_DP | AB5 | USB1.DP | fixed | FMU_USB_DP |  |  |
| USB1_VBUS | AB6 | USB1.VBUS | analog | SOC_USB1_VBUS |  |  |
| VSS_AB7 | AB7 | reserved |  | GND |  |  |
| RGMII2_RD3 | AB8 |  |  |  |  |  |
| RGMII2_RD0 | AB9 |  |  |  |  |  |
| RGMII2_RD2 | AB10 |  |  |  |  |  |
| RGMII1_TX_CTL | AB11 | RGMII1.TX_CTL | vendor(muxmode=0) | ETH_TX_CTL |  |  |
| RGMII2_TX_CTL | AB12 |  |  |  |  |  |
| RGMII2_TD1 | AB13 | gpio_in |  | N_ETH_INT |  | GPIO0_70, 1.8 V: PHY interrupt, active low. DEVIATION: the EVM uses an I2C port expander. |
| TCK | AB14 | SYS.TCK | vendor(muxmode=0) | SOC_JTAG_TCK |  |  |
| TDO | AB15 | SYS.TDO | vendor(muxmode=0) | SOC_JTAG_TDO |  |  |
| TRSTn | AB16 | SYS.TRSTn | vendor(muxmode=0) | SOC_JTAG_TRSTN |  |  |
| RSVD0 | AB17 | reserved |  |  |  | Reserved: must be left unconnected. |
| PORz | AB18 | SYS.PORz | vendor(muxmode=0) | SOC_PORZ |  |  |
| EXT_WAKEUP0 | AB19 | EXT.WAKEUP0 | fixed | SOC_EXT_WAKEUP0 |  |  |
| EXT_WAKEUP1 | AB20 | EXT.WAKEUP1 | fixed | SOC_EXT_WAKEUP1 |  |  |
| VSS_AB21 | AB21 | reserved |  | GND |  |  |
| WKUP_I2C0_SCL | AB22 | WKUP_I2C0.SCL | vendor(muxmode=0) | PMIC_I2C_SCL | drive=open_drain |  |
| VSS_AB23 | AB23 | reserved |  | GND |  |  |
| VSS_AC1 | AC1 | reserved |  | GND |  |  |
| VSS_AC2 | AC2 | reserved |  | GND |  |  |
| USB0_VBUS | AC3 | USB0.VBUS | analog | SOC_USB0_VBUS |  |  |
| USB0_DM | AC4 | USB0.DM | fixed | USBC_DM |  |  |
| USB1_DM | AC5 | USB1.DM | fixed | FMU_USB_DM |  |  |
| USB1_RCALIB | AC6 | USB1.RCALIB | fixed | SOC_USB1_RCALIB |  |  |
| RGMII2_RXC | AC7 |  |  |  |  |  |
| RGMII2_RX_CTL | AC8 |  |  |  |  |  |
| RGMII2_RD1 | AC9 |  |  |  |  |  |
| RGMII1_TD0 | AC10 | RGMII1.TD0 | vendor(muxmode=0) | ETH_TD0 |  |  |
| VSS_AC11 | AC11 | reserved |  | GND |  |  |
| RGMII2_TD0 | AC12 | gpio_out |  | N_ETH_RESET | initial=low | GPIO0_69, 1.8 V: PHY reset, active low. DEVIATION: the EVM uses an I2C port expander. |
| MDIO0_MDIO | AC13 | MDIO0.MDIO | vendor(muxmode=0) | ETH_MDIO |  |  |
| VSS_AC14 | AC14 | reserved |  | GND |  |  |
| MDIO0_MDC | AC15 | MDIO0.MDC | vendor(muxmode=0) | ETH_MDC |  |  |
| TDI | AC16 | SYS.TDI | vendor(muxmode=0) | SOC_JTAG_TDI |  |  |
| WKUP_OSC0_XO | AC17 | WKUP_OSC0.XO | fixed | SOC_OSC0_XO |  |  |
| WKUP_OSC0_XI | AC18 | WKUP_OSC0.XI | fixed | SOC_OSC0_XI |  |  |
| VSS_AC19 | AC19 | reserved |  | GND |  |  |
| LFOSC0_XO | AC20 | LFOSC0.XO | fixed | SOC_LFOSC0_XO |  |  |
| LFOSC0_XI | AC21 | LFOSC0.XI | fixed | SOC_LFOSC0_XI |  |  |
| VSS_AC22 | AC22 | reserved |  | GND |  |  |
| VSS_AC23 | AC23 | reserved |  | GND |  |  |

## DDR0

DDR4, one x16 device (EVM: LPDDR4, so this section follows SPRAD06 Figure 2-1, not the EVM). WE_n/CAS_n/RAS_n are A14/A15/A16. BG1 is unused with an x16 device. CAL0 takes 240R 1% to GND. Data bits may be swapped within a byte lane, and byte lanes swapped, during layout; update the nets here when they are.

| Signal | Pin | Net |
|---|---|---|
| A0 | DDR0_A0 | DDR_A0 |
| A1 | DDR0_A1 | DDR_A1 |
| A2 | DDR0_A2 | DDR_A2 |
| A3 | DDR0_A3 | DDR_A3 |
| A4 | DDR0_A4 | DDR_A4 |
| A5 | DDR0_A5 | DDR_A5 |
| A6 | DDR0_A6 | DDR_A6 |
| A7 | DDR0_A7 | DDR_A7 |
| A8 | DDR0_A8 | DDR_A8 |
| A9 | DDR0_A9 | DDR_A9 |
| A10 | DDR0_A10 | DDR_A10 |
| A11 | DDR0_A11 | DDR_A11 |
| A12 | DDR0_A12 | DDR_A12 |
| A13 | DDR0_A13 | DDR_A13 |
| ACT_n | DDR0_ACT_n | DDR_ACT_N |
| BA0 | DDR0_BA0 | DDR_BA0 |
| BA1 | DDR0_BA1 | DDR_BA1 |
| BG0 | DDR0_BG0 | DDR_BG0 |
| CAS_n | DDR0_CAS_n | DDR_CAS_N |
| CK0 | DDR0_CK0 | DDR_CK0 |
| CK0_n | DDR0_CK0_n | DDR_CK0_N |
| CKE0 | DDR0_CKE0 | DDR_CKE0 |
| CS0_n | DDR0_CS0_n | DDR_CS0_N |
| DM0 | DDR0_DM0 | DDR_DM0 |
| DM1 | DDR0_DM1 | DDR_DM1 |
| DQ0 | DDR0_DQ0 | DDR_DQ0 |
| DQ1 | DDR0_DQ1 | DDR_DQ1 |
| DQ2 | DDR0_DQ2 | DDR_DQ2 |
| DQ3 | DDR0_DQ3 | DDR_DQ3 |
| DQ4 | DDR0_DQ4 | DDR_DQ4 |
| DQ5 | DDR0_DQ5 | DDR_DQ5 |
| DQ6 | DDR0_DQ6 | DDR_DQ6 |
| DQ7 | DDR0_DQ7 | DDR_DQ7 |
| DQ8 | DDR0_DQ8 | DDR_DQ8 |
| DQ9 | DDR0_DQ9 | DDR_DQ9 |
| DQ10 | DDR0_DQ10 | DDR_DQ10 |
| DQ11 | DDR0_DQ11 | DDR_DQ11 |
| DQ12 | DDR0_DQ12 | DDR_DQ12 |
| DQ13 | DDR0_DQ13 | DDR_DQ13 |
| DQ14 | DDR0_DQ14 | DDR_DQ14 |
| DQ15 | DDR0_DQ15 | DDR_DQ15 |
| DQS0 | DDR0_DQS0 | DDR_DQS0 |
| DQS0_n | DDR0_DQS0_n | DDR_DQS0_N |
| DQS1 | DDR0_DQS1 | DDR_DQS1 |
| DQS1_n | DDR0_DQS1_n | DDR_DQS1_N |
| ODT0 | DDR0_ODT0 | DDR_ODT0 |
| RAS_n | DDR0_RAS_n | DDR_RAS_N |
| RESET0_n | DDR0_RESET0_n | DDR_RESET0_N |
| WE_n | DDR0_WE_n | DDR_WE_N |
| CAL0 | DDR0_CAL0 | DDR_CAL0 |

## MMC0

eMMC, 8-bit HS200, VDDSHV2 at 1.8 V. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| CLK | MMC0_CLK | EMMC_CLK |
| CMD | MMC0_CMD | EMMC_CMD |
| DAT0 | MMC0_DAT0 | EMMC_DAT0 |
| DAT1 | MMC0_DAT1 | EMMC_DAT1 |
| DAT2 | MMC0_DAT2 | EMMC_DAT2 |
| DAT3 | MMC0_DAT3 | EMMC_DAT3 |
| DAT4 | MMC0_DAT4 | EMMC_DAT4 |
| DAT5 | MMC0_DAT5 | EMMC_DAT5 |
| DAT6 | MMC0_DAT6 | EMMC_DAT6 |
| DAT7 | MMC0_DAT7 | EMMC_DAT7 |

## MMC1

microSD, UHS-I. VDDSHV3 comes from the SoC's internal SDIO LDO (CAP_VDDSHV_MMC), which switches 3.3 V / 1.8 V. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| CLK | MMC1_CLK | SD_CLK |
| CMD | MMC1_CMD | SD_CMD |
| DAT0 | MMC1_DAT0 | SD_DAT0 |
| DAT1 | MMC1_DAT1 | SD_DAT1 |
| DAT2 | MMC1_DAT2 | SD_DAT2 |
| DAT3 | MMC1_DAT3 | SD_DAT3 |
| SDCD | MMC1_SDCD | SD_CD |

## RGMII1

Gigabit Ethernet PHY (EVM: DP83867), 1.8 V I/O on VDDS0. As the EVM's first port; the second port is dropped.

| Signal | Pin | Net |
|---|---|---|
| TXC | RGMII1_TXC | ETH_TXC |
| TX_CTL | RGMII1_TX_CTL | ETH_TX_CTL |
| TD0 | RGMII1_TD0 | ETH_TD0 |
| TD1 | RGMII1_TD1 | ETH_TD1 |
| TD2 | RGMII1_TD2 | ETH_TD2 |
| TD3 | RGMII1_TD3 | ETH_TD3 |
| RXC | RGMII1_RXC | ETH_RXC |
| RX_CTL | RGMII1_RX_CTL | ETH_RX_CTL |
| RD0 | RGMII1_RD0 | ETH_RD0 |
| RD1 | RGMII1_RD1 | ETH_RD1 |
| RD2 | RGMII1_RD2 | ETH_RD2 |
| RD3 | RGMII1_RD3 | ETH_RD3 |

## MDIO0

PHY management, 1.8 V. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| MDC | MDIO0_MDC | ETH_MDC |
| MDIO | MDIO0_MDIO | ETH_MDIO |

## MMC2

Wi-Fi SDIO, VDDSHV4 at 1.8 V. As the EVM's M.2 Key E slot; the module is not chosen yet.

| Signal | Pin | Net |
|---|---|---|
| CLK | MMC2_CLK | WLAN_SDIO_CLK |
| CMD | MMC2_CMD | WLAN_SDIO_CMD |
| DAT0 | MMC2_DAT0 | WLAN_SDIO_D0 |
| DAT1 | MMC2_DAT1 | WLAN_SDIO_D1 |
| DAT2 | MMC2_DAT2 | WLAN_SDIO_D2 |
| DAT3 | MMC2_DAT3 | WLAN_SDIO_D3 |

## UART5

Bluetooth HCI, 1.8 V on VDDS1. Nets are named from the module's side. DEVIATION: the EVM runs HCI on UART1 through buffers; pinion puts it on the unused OSPI balls, in a 1.8 V domain, and UART1 goes to the FMU.

| Signal | Pin | Net |
|---|---|---|
| RXD | OSPI0_CSn2 | BT_UART_TX |
| TXD | OSPI0_CSn3 | BT_UART_RX |
| RTSn | OSPI0_LBCLKO | BT_UART_CTS |
| CTSn | OSPI0_DQS | BT_UART_RTS |

## WKUP

32.768 kHz slow clock to the Wi-Fi/BT module, 1.8 V. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| CLKOUT0 | WKUP_CLKOUT0 | WLAN_SLOW_CLK |

## UART1

MAVLink / uXRCE-DDS link to the FMU's UART5, 3.3 V on VDDSHV1, direct connection. Not on the EVM.

| Signal | Pin | Net |
|---|---|---|
| TXD | MCASP0_ACLKR | FMU_UART5_RX_SOC |
| RXD | MCASP0_AFSR | FMU_UART5_TX_SOC |
| RTSn | MCASP0_AXR2 | FMU_UART5_CTS_SOC |
| CTSn | MCASP0_AXR3 | FMU_UART5_RTS_SOC |

## MCAN0

Own transceiver on the FMU CAN1 bus, 3.3 V. EVM: MCAN header.

| Signal | Pin | Net |
|---|---|---|
| TX | MCAN0_TX | SOC_CAN_TX |
| RX | MCAN0_RX | SOC_CAN_RX |

## USB1

Host port wired on-board to the FMU's USB (PX4 bootloader upload, MAVLink). DRVVBUS enables the 5 V that feeds FMU_VBUS_SENSE and, divided, USB1_VBUS. RCALIB takes 499R 1% to GND. EVM: Type-A host port.

| Signal | Pin | Net |
|---|---|---|
| DP | USB1_DP | FMU_USB_DP |
| DM | USB1_DM | FMU_USB_DM |
| DRVVBUS | USB1_DRVVBUS | FMU_USB_VBUS_EN |
| VBUS | USB1_VBUS | SOC_USB1_VBUS |
| RCALIB | USB1_RCALIB | SOC_USB1_RCALIB |

## USB0

External USB-C, dual role; also the USB DFU boot port. VBUS through the datasheet divider. EVM: Type-C with a TPS65988 PD controller, which pinion does not need for power.

| Signal | Pin | Net |
|---|---|---|
| DP | USB0_DP | USBC_DP |
| DM | USB0_DM | USBC_DM |
| DRVVBUS | USB0_DRVVBUS | USBC_VBUS_EN |
| VBUS | USB0_VBUS | SOC_USB0_VBUS |
| RCALIB | USB0_RCALIB | SOC_USB0_RCALIB |

## UART0

Linux and bootloader console on a debug connector, 3.3 V; also the UART boot port. EVM: FT4232 bridge.

| Signal | Pin | Net |
|---|---|---|
| TXD | UART0_TXD | SOC_UART0_TX |
| RXD | UART0_RXD | SOC_UART0_RX |

## WKUP_UART0

WKUP-domain UART, 1.8 V, on test pads. EVM: FT4232 bridge.

| Signal | Pin | Net |
|---|---|---|
| TXD | WKUP_UART0_TXD | SOC_WKUP_UART0_TX |
| RXD | WKUP_UART0_RXD | SOC_WKUP_UART0_RX |

## I2C0

3.3 V: board ID EEPROM 0x51. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| SCL | I2C0_SCL | SOC_I2C0_SCL |
| SDA | I2C0_SDA | SOC_I2C0_SDA |

## I2C1

3.3 V: expansion / on-board monitors. The EVM hangs its port expanders, INA228s and temperature sensors here.

| Signal | Pin | Net |
|---|---|---|
| SCL | I2C1_SCL | SOC_I2C1_SCL |
| SDA | I2C1_SDA | SOC_I2C1_SDA |

## WKUP_I2C0

1.8 V: PMIC at 0x30. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| SCL | WKUP_I2C0_SCL | PMIC_I2C_SCL |
| SDA | WKUP_I2C0_SDA | PMIC_I2C_SDA |

## SYS

PORz from the PMIC reset output; RESETz from a button; RESETSTATz resets the eMMC, PHY and Wi-Fi module; EXTINTn is the PMIC interrupt (3.3 V, open drain). JTAG is 1.8 V on a cTI-20 or Tag-Connect header (EVM: on-board XDS110, dropped). BOOTMODE[15:0] are sampled at PORz from pull-up/pull-down resistors on GPMC0_AD[15:0], 3.3 V; primary eMMC with SD backup is 0x344B on the EVM, and a DIP switch or solder jumpers select SD, UART and USB DFU.

| Signal | Pin | Net |
|---|---|---|
| PORz | PORz | SOC_PORZ |
| RESETz | RESETz | SOC_RESETZ |
| RESETSTATz | RESETSTATz | SOC_RESETSTATZ |
| EXTINTn | EXTINTn | N_PMIC_INT |
| TCK | TCK | SOC_JTAG_TCK |
| TMS | TMS | SOC_JTAG_TMS |
| TDI | TDI | SOC_JTAG_TDI |
| TDO | TDO | SOC_JTAG_TDO |
| TRSTn | TRSTn | SOC_JTAG_TRSTN |
| EMU0 | EMU0 | SOC_JTAG_EMU0 |
| EMU1 | EMU1 | SOC_JTAG_EMU1 |
| BOOTMODE00 | GPMC0_AD0 | SOC_BOOTMODE0 |
| BOOTMODE01 | GPMC0_AD1 | SOC_BOOTMODE1 |
| BOOTMODE02 | GPMC0_AD2 | SOC_BOOTMODE2 |
| BOOTMODE03 | GPMC0_AD3 | SOC_BOOTMODE3 |
| BOOTMODE04 | GPMC0_AD4 | SOC_BOOTMODE4 |
| BOOTMODE05 | GPMC0_AD5 | SOC_BOOTMODE5 |
| BOOTMODE06 | GPMC0_AD6 | SOC_BOOTMODE6 |
| BOOTMODE07 | GPMC0_AD7 | SOC_BOOTMODE7 |
| BOOTMODE08 | GPMC0_AD8 | SOC_BOOTMODE8 |
| BOOTMODE09 | GPMC0_AD9 | SOC_BOOTMODE9 |
| BOOTMODE10 | GPMC0_AD10 | SOC_BOOTMODE10 |
| BOOTMODE11 | GPMC0_AD11 | SOC_BOOTMODE11 |
| BOOTMODE12 | GPMC0_AD12 | SOC_BOOTMODE12 |
| BOOTMODE13 | GPMC0_AD13 | SOC_BOOTMODE13 |
| BOOTMODE14 | GPMC0_AD14 | SOC_BOOTMODE14 |
| BOOTMODE15 | GPMC0_AD15 | SOC_BOOTMODE15 |

## WKUP_OSC0

25 MHz crystal or oscillator. As the EVM (which buffers one oscillator to the SoC and PHYs).

| Signal | Pin | Net |
|---|---|---|
| XI | WKUP_OSC0_XI | SOC_OSC0_XI |
| XO | WKUP_OSC0_XO | SOC_OSC0_XO |

## LFOSC0

32.768 kHz crystal for the RTC domain. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| XI | LFOSC0_XI | SOC_LFOSC0_XI |
| XO | LFOSC0_XO | SOC_LFOSC0_XO |

## RTC

RTC domain power-on reset, 1.8 V (VDDS_RTC).

| Signal | Pin | Net |
|---|---|---|
| PORz | RTC_PORz | SOC_RTC_PORZ |

## PMIC

Low-power-mode request to the PMIC, 1.8 V. As the EVM.

| Signal | Pin | Net |
|---|---|---|
| LPM_EN0 | PMIC_LPM_EN0 | PMIC_LPM_EN0 |

## EXT

RTC-domain wake inputs; pulled to their inactive level if unused (datasheet section 5.4).

| Signal | Pin | Net |
|---|---|---|
| WAKEUP0 | EXT_WAKEUP0 | SOC_EXT_WAKEUP0 |
| WAKEUP1 | EXT_WAKEUP1 | SOC_EXT_WAKEUP1 |
