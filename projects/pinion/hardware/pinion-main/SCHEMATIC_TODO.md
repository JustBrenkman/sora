<!-- SPDX-License-Identifier: CERN-OHL-P-2.0 -->
# pinion-main schematic TODO

Everything that has to be drawn, one entry per part, grouped by schematic sheet.
The schematic is hierarchical, two levels below the root.
Tick an entry when the part is placed, wired, and its symbol and footprint are in
the library.

- Net names in `code font` are the labels in
  [`specs/pinout/`](../../specs/pinout/) (`fmu`, `io` and `soc` pinasg files). Use
  them unchanged so the schematic can be checked against the pin map.
- "ref" names where the requirement comes from. Abbreviations: **v6C** =
  FMUv6C sources in `specs/reference/` (PX4 board files, DS-018, Holybro pages);
  **EVM** = AM62L EVM user's guide SPRUJG8B; **DS** = AM62L datasheet;
  **DDR** = SPRAD06 DDR layout guide.
- *(select)* means the part is not chosen; *(open)* points to a question in
  [`specs/notes/decisions.md`](../../specs/notes/decisions.md).
- Passive values not given in the references are left for the part's datasheet;
  where a value is quoted it comes from the named reference.

## 0. Project and library

- [x] Create `pinion-main.kicad_pro` in this folder, in KiCad, with the sheet
      hierarchy below: the root sheet holds the shared parts and two sheets,
      `linux` and `fmu`, and each of those holds its own sub-sheets.
- [x] Reference designators: STM32H743 = **U1**, STM32F103 = **U2**, AM62L = **U3**
      (the pinasg files name them).
- [x] Add symbols and footprints to `lib/kicad` (JustBrenkman/kicad-lib) and bump
      the submodule. The library holds none of pinion's parts today, so every
      entry below needs one unless KiCad's stock libraries cover it (passives,
      JST-GH/SH/ZH, USB-C, crystals, STM32F103C8T6).
  - [x] AM62L32 ANB 373-ball, 0.5 mm pitch, 11.9 x 11.9 mm. Pin names and balls
        from `specs/pinout/am62l32.pindef.json`; split the symbol into units
        (DDR, MMC, RGMII, GPMC/boot, general, system, power, ground).
  - [x] STM32H743VIH6 TFBGA100, from `specs/pinout/stm32h743vih6.pindef.json`.
  - [ ] DDR4 x16 FBGA-96, eMMC FBGA-153, PMIC, PHY, sensors, FRAM/EEPROM, CAN
        transceiver, load switches, regulators, Wi-Fi module as they are selected.

### Sheet hierarchy

```
pinion-main (root)        R   shared parts, drawn on the root sheet itself
│                         R1  POWER1/POWER2, power selector, +5V
│                         R2  UART, USB and CAN between the processors
│                         R3  mounting holes
├── linux                 B   AM62L computer
│   ├── linux-power       B1
│   ├── soc               B2
│   ├── ddr4              B3
│   ├── storage           B4
│   ├── ethernet          B5
│   ├── wireless          B6
│   └── usb               B7
└── fmu                   C   flight controller
    ├── fmu-power         C1
    ├── fmu-mcu           C2
    ├── sensors           C3
    ├── nvm               C4
    ├── can               C5
    ├── fmu-connectors    C6
    ├── io-mcu            C7
    └── pwm               C8
```

Nets that cross between `linux` and `fmu` do so only through the root sheet, as
hierarchical pins on the two sheet symbols: `+5V`, `GND`, the four `FMU_UART5_*_SOC` nets,
`FMU_USB_DP`/`FMU_USB_DM`, `FMU_VBUS_SENSE`, `FMU_USB_VBUS_EN`, `CAN1_H`/`CAN1_L`,
and `USBC_VBUS` to the power selector.

## R. Root sheet

The parts both halves share are placed directly on the root sheet, next to the
`linux` and `fmu` sheet symbols.

### R1. Power input

- [ ] **POWER1**, **POWER2** JST-GH 6 (ref: Holybro port table): 5 V, 5 V,
      CURRENT, VOLTAGE, GND, GND. A purchased power module supplies regulated
      5 V and the two analog signals; there is no battery connector or battery
      regulator on the board.
- [ ] **Sense inputs**: RC filter and clamp on each, 3.3 V full scale →
      `FMU_BAT1_V` (U1 PC5), `FMU_BAT1_I` (PC4), `FMU_BAT2_V` (PB1), `FMU_BAT2_I`
      (PA2). Default scales 18.18 V/V and 36.36 A/V (ref: v6C `hwdef.dat`).
- [ ] **Power selector** (ideal diodes, one source at a time) →
      `+5V`. Reports `PWR1_VALID` (U1 PA15), `PWR2_VALID` (PB12),
      `N_USB_VBUS_VALID` (PE15), active low, pulled up to `FMU_VDD_3V3` (ref: v6C
      `board_config.h`). Parts: an LM73100 on each of POWER1 and POWER2 (5.5 A,
      overvoltage cutoff on OVLO) and an LM66100 on the USB input. The LM73100's
      PG is open-drain and high when valid, so the active-low valid signals
      need an inversion.
      Its USB input is `USBC_VBUS` from the AM62L's USB-C port *(open 3)*.
- [ ] **Input protection**: TVS and overvoltage protection on each 5 V input
      (FMUv6C maximum input is 6 V).
- [ ] **5 V monitor divider** 2:1 → `FMU_SCALED_V5` (U1 PA4) (ref: v6C, `SCALE(2)`).
- [ ] **5 V budget** *(open 2)*: confirm the power module covers the AM62L
      section, the FMU and both 1.5 A port rails.

### R2. Processor interconnect

- [ ] **UART**: `FMU_UART5_TX_SOC`, `FMU_UART5_RX_SOC`, `FMU_UART5_RTS_SOC`,
      `FMU_UART5_CTS_SOC`, direct, both sides 3.3 V. Add series resistors and
      check that neither processor back-powers the other when only one rail is up.
- [ ] **FMU USB link**: `FMU_USB_DP`, `FMU_USB_DM` from U3 USB1 to U1 PA12/PA11,
      routed as a 90 Ω pair; no connector.
- [ ] **FMU VBUS switch**: 5 V switched by `FMU_USB_VBUS_EN` (U3 USB1_DRVVBUS),
      divided to a 3.3 V-safe level → `FMU_VBUS_SENSE` (U1 PA9), and to
      `SOC_USB1_VBUS`.
- [ ] **CAN**: the AM62L transceiver (B2) joins `CAN1_H`/`CAN1_L` from sheet C5
      with a short stub.
- [ ] *(open 4, 5)* optional GPIOs between the processors (BOOT0, reset, PPS).

### R3. Mechanical

- [ ] **Stack mounting holes** (ref: `specs/notes/mechanical.md`): four
      non-plated Ø3.2 mm holes on a 30.5 x 30.5 mm square centred on the board.
      Place them as
      mounting-hole symbols so they reach the PCB with their keep-outs.
- [ ] Airframe mounting holes, fiducials and test points, once the outline is set.

## B. Linux computer

### B1. Power

Follow TI's "AM62L Power Supply Implementation" note (to be added to
`specs/reference/ti/` by hand) and the sequencing in DS section 6.11.2.

- [ ] **3.3 V buck** from `+5V` → `VCC_3V3_SYS` *(select)*.
- [ ] **PMIC TPS6521402** (the AM62L variant listed for DDR4; the EVM's
      TPS6521401 is LPDDR4 only): Buck1 → `VDD_CORE_0V75`; Buck2 → `SOC_DVDD_1V8`;
      Buck3 → `VDD_DDR_1V2`; LDO1 → `VDDA_1V8`; LDO2 → `SOC_DVDD_3V3`. I2C
      `PMIC_I2C_SCL`/`PMIC_I2C_SDA` (address 0x30), interrupt → `N_PMIC_INT`, reset
      output → `SOC_PORZ`, `PMIC_LPM_EN0` from the SoC. Confirm the rail order and
      voltages of the -02 NVM against the TPS65214 datasheet (`reference/parts/`).
- [ ] **`VDDA_CORE_0V75`** filter from `VDD_CORE_0V75` for the USB and DSI core
      supplies (DS: they must share VDD_CORE's source).
- [ ] **DDR4 VPP**: 2.5 V LDO → `VPP_DDR_2V5`.
- [ ] **VTT/VREF** *(open 7)*: TPS51200 → `VTT_DDR`, `VREF_DDR`; or a VREFCA divider.
- [ ] **RTC rails**: `SOC_VDD_RTC_0V75`, `SOC_VDDS_RTC_1V8`. Separate LDOs as on
      the EVM only if RTC-only low-power mode is wanted; otherwise from the main rails.
- [ ] **`VPP_1V8`** eFuse LDO, unpopulated by default (ref: EVM, DS section 6.8).
- [ ] **Ethernet PHY rails**: 2.5 V and 1.0 V (ref: EVM), 1.8 V I/O from
      `SOC_DVDD_1V8`.
- [ ] **microSD supply switch**: 3.3 V, enable `SD_PWR_EN` (U3 GPIO0_123).
- [ ] **Wi-Fi/BT module supply** per the module *(select)*.
- [ ] Test points on every rail.

### B2. SoC (U3, AM62L32)

All 373 balls are in `specs/pinout/soc.md`; I/O supply per ball is in
`specs/notes/am62l-io-domains.md`.

- [ ] **U3** symbol units placed; every supply ball on its rail net as assigned.
- [ ] **Decoupling** per rail, following SPRAC76 and the EVM; the six
      `SOC_CAP_VDDS_*`/`VDDSHV_SD_IO` capacitor balls each get their capacitor
      (DS Table 5-46 notes; `CAP_VDDSHV_MMC`: 3.3 µF).
- [ ] **25 MHz** crystal or oscillator on `SOC_OSC0_XI`/`SOC_OSC0_XO`
      (`BOOTMODE[2:0]` must match the frequency).
- [ ] **32.768 kHz** crystal on `SOC_LFOSC0_XI`/`SOC_LFOSC0_XO`.
- [ ] **Reset**: `SOC_PORZ` from the PMIC; `SOC_RESETZ` button with pull-up;
      `SOC_RESETSTATZ` to eMMC, PHY and module resets; `SOC_RTC_PORZ`.
- [ ] **Boot-mode straps** on `SOC_BOOTMODE0`..`15` (GPMC0_AD[15:0], 3.3 V): a
      pull-up or pull-down each (DS section 5.4), with a selector for at least
      eMMC + SD backup (EVM switch value 0x344B), SD + UART backup (0x0E43) and a
      USB DFU option (ref: EVM section 2.4.2).
- [ ] **JTAG header** *(select)*: `SOC_JTAG_TCK`, `_TMS`, `_TDI`, `_TDO`, `_TRSTN`,
      `_EMU0`, `_EMU1`, 1.8 V. Pull-down on TRSTn, pull-ups on TCK, TMS, TDI,
      EMU0, EMU1 (DS section 5.4).
- [ ] **Console connector**: `SOC_UART0_TX`, `SOC_UART0_RX`, GND, 3.3 V logic.
      Test pads for `SOC_WKUP_UART0_TX`/`_RX` (1.8 V).
- [ ] **Board ID EEPROM** (AT24C512C-class), I2C0, 0x51; pull-ups to `SOC_DVDD_3V3`.
- [ ] **I2C1** pull-ups and a test point; **WKUP_I2C0** pull-ups to `SOC_DVDD_1V8`.
- [ ] **Wake inputs** `SOC_EXT_WAKEUP0`/`1`: pull to the inactive level (DS section 5.4).
- [ ] **Unused**: `VDDA_ADC` and `ADC0_AIN[3:0]` to GND; DSI signal balls and
      `RSVD0` unconnected (DS section 5.4).
- [ ] **LED** `SOC_LED_STATUS`, **button** `N_SOC_USER_BTN`.
- [ ] 49 free balls (GPMC, RGMII2, McASP0, SPI0, OSPI, I2C2): bring a useful
      subset to test pads or an expansion header if space allows.
- [ ] **CAN transceiver** for the FMU's CAN1 bus: `SOC_CAN_TX`/`SOC_CAN_RX`
      (U3 MCAN0, 3.3 V). Short stub to the CAN1 pair.

### B3. DDR4

- [ ] **DDR4 SDRAM x16**, FBGA-96 *(select density)*: nets `DDR_*` from the
      `DDR0` peripheral. Wire as SPRAD06 Figure 2-1: `DDR_WE_N`/`DDR_CAS_N`/
      `DDR_RAS_N` are A14/A15/A16; `DDR_BG0` to BG0; DDR0_BG1 unused.
- [ ] Memory pins with no SoC signal (PAR, ALERT_n, TEN): terminate as SPRAD06
      and the memory datasheet require.
- [ ] `DDR_CAL0`: 240 Ω 1 % to GND at the SoC; ZQ: 240 Ω 1 % at the memory (ref: DDR).
- [ ] `DDR_RESET0_N` and `DDR_CKE0`: pull resistors as SPRAD06 specifies for DDR4.
- [ ] `VDD_DDR_1V2` (VDD/VDDQ), `VPP_DDR_2V5`, VREFCA, VTT *(open 7)*.
- [ ] Record any bit or byte-lane swaps made in layout back into `soc.pinasg.ron`.

### B4. Storage

- [ ] **eMMC**, FBGA-153 *(select size)*: `EMMC_CLK` (series resistor at the SoC),
      `EMMC_CMD`, `EMMC_DAT0`..`7`, pull-ups per the EVM, reset from
      `SOC_RESETSTATZ`; VCC 3.3 V, VCCQ `SOC_DVDD_1V8` (ref: EVM section 2.6.11.3.1).
- [ ] **microSD socket**: `SD_CLK`, `SD_CMD`, `SD_DAT0`..`3`, `SD_CD`; card supply
      from the switch; I/O on `VDDSHV_SD_IO` (SoC's internal LDO); ESD array.

### B5. Ethernet

- [ ] **Gigabit PHY** (EVM: DP83867IRRGZ, RGMII, 48-pin): `ETH_TXC`, `ETH_TX_CTL`,
      `ETH_TD0`..`3`, `ETH_RXC`, `ETH_RX_CTL`, `ETH_RD0`..`3`, `ETH_MDC`, `ETH_MDIO`,
      `N_ETH_RESET`, `N_ETH_INT`. 1.8 V I/O. Strap resistors for address, RGMII
      delay and advertised speed (ref: EVM section 2.6.12.1, DP83867 datasheet).
- [ ] **25 MHz** reference for the PHY (own crystal, or buffered from the SoC's).
- [ ] **Magnetics and connector** *(select)*: RJ45 with integrated magnetics, or
      discrete magnetics and a small locking connector; link/activity LEDs.

### B6. Wi-Fi and Bluetooth

- [ ] **Module** *(select)*, 1.8 V I/O: `WLAN_SDIO_CLK`, `_CMD`, `_D0`..`_D3`;
      `BT_UART_TX`, `BT_UART_RX`, `BT_UART_RTS`, `BT_UART_CTS`; `WLAN_EN`, `BT_EN`,
      `WLAN_IRQ`; `WLAN_SLOW_CLK` (32.768 kHz). Pull-downs on the two enables.
- [ ] **Antenna**: U.FL or chip antenna with matching network *(select)*.

### B7. USB

- [ ] **USB-C receptacle** (USB 2.0): `USBC_DP`, `USBC_DM`; CC resistors or a
      CC controller for dual role; VBUS switch enabled by `USBC_VBUS_EN`; `USBC_VBUS` also goes to
      the power selector (R1); ESD.
- [ ] **VBUS dividers**: `SOC_USB0_VBUS` and `SOC_USB1_VBUS`, as DS section 8.2.3.
- [ ] **`SOC_USB0_RCALIB`**, **`SOC_USB1_RCALIB`**: 499 Ω 1 % each to GND (DS Table 5-64/5-65).

## C. Flight controller

### C1. Power

- [ ] **3.3 V regulator** from `+5V` → `FMU_VDD_3V3`. Supplies U1, U2's
      rail, the sensor switch, CAN transceivers, parameter storage.
- [ ] **Analog filter** (ferrite + capacitors) → `FMU_VDDA_3V3` (U1 VDDA; VREF+ is
      bonded to VDDA in this package).
- [ ] **Sensor rail switch** → `VDD_3V3_SENSORS`, enable `VDD_3V3_SENSORS_EN`
      (U1 PB2, active high, default off). PX4 power-cycles the sensors with it (ref: v6C).
- [ ] **`VDD_5V_PERIPH` switch**, 1.5 A current limit: enable
      `N_VDD_5V_PERIPH_EN` (U1 PE2), fault `N_VDD_5V_PERIPH_OC` (U1 PE3, pull-up to
      `FMU_VDD_3V3`). Feeds TELEM3, GPS1, I2C, CAN1, CAN2, RC (ref: v6C, Holybro spec).
- [ ] **`VDD_5V_HIPOWER` switch**, 1.5 A current limit: enable
      `N_VDD_5V_HIPOWER_EN` (U1 PC10), fault `N_VDD_5V_HIPOWER_OC` (U1 PC11,
      pull-up). Feeds TELEM1 and GPS2 (ref: v6C, Holybro spec).
- [ ] **IO rail** `IO_VDD_3V3` for U2 and the GPS1 connector pin 8.
- [ ] **Spektrum switch** → `VDD_3V3_SPEKTRUM`, enable `IO_SPEKTRUM_PWR_EN` (U2 PC13).
- [ ] **`FMU_VBAT`** (U1 VBAT): backup supply; tie to `FMU_VDD_3V3` or a backup
      cell. DS-018 lists a battery-backed RTC, but the FMUv6C pinout has no LSE
      crystal (PC14/PC15 are chip selects).

### C2. MCU (U1, STM32H743VIH6)

- [ ] **U1**. All 100 balls are in `specs/pinout/fmu.md`; 8 I/O are free
      (PB3, PB4, PB14, PB15, PC14, PD6, PD7, PE5).
- [ ] **Decoupling**: per VDD ball plus bulk; `FMU_VCAP1`, `FMU_VCAP2` capacitors
      to GND; `VDDLDO`, `VDD33_USB`, `PDR_ON` to `FMU_VDD_3V3`. Take values from
      the STM32H743 datasheet (DS12110, to be added to `specs/reference/st/` by hand).
- [ ] **16 MHz crystal** + load capacitors on `FMU_OSC_IN`/`FMU_OSC_OUT`
      (PH0/PH1) (ref: v6C `board.h`, `STM32_BOARD_XTAL`).
- [ ] **Reset**: `FMU_NRST` with capacitor, to the debug connector.
- [ ] **`FMU_BOOT0`**: pull-down and test pad *(open 5)*.
- [ ] **Hardware version/revision dividers**: `HW_VER_REV_DRIVE` (PE12) feeds two
      resistor pairs sensed on `HW_VER_SENSE` (PC1) and `HW_REV_SENSE` (PC0).
      Resistor pairs per ID are in the "HW REV and VER ID" sheet of
      `specs/reference/px4-docs/fmuv6c-pinout.xlsx`. Choose IDs that are not a
      V6C variant and record them in `specs/notes/decisions.md`.
- [ ] **Status LEDs**: red `N_FMU_LED_RED` (PD10), blue `N_FMU_LED_BLUE` (PD11),
      active low, to `FMU_VDD_3V3`.
- [ ] **Pull-ups** on I2C1, I2C2 (to `FMU_VDD_3V3`) and I2C4 (to `VDD_3V3_SENSORS`).

### C3. Sensors

All on `VDD_3V3_SENSORS` (ref: v6C sensor table, DS-018). Decide first whether
they go on an isolated daughterboard *(open 6)*; if so this sheet becomes a
board-to-board connector carrying SPI1, I2C4, two CS, two DRDY, the heater
and the rail.

- [ ] **ICM-42688-P** (IMU 2): SPI1 (`FMU_SPI1_SCK_SENSOR`, `_MISO_`, `_MOSI_`),
      CS `FMU_SPI1_CS3_ICM42688`, INT → `FMU_SPI1_DRDY3_ICM42688`.
- [ ] **BMI270** (IMU 1, replaces the FMUv6C's BMI088, deviation F9): SPI1, CS
      `FMU_SPI1_CS1_BMI270`, INT1 → `FMU_SPI1_DRDY1_BMI270`; INT2 and the
      auxiliary interface pins unconnected; VDD and VDDIO on `VDD_3V3_SENSORS`
      (ref: BMI270 datasheet section 7 in `reference/parts/`).
- [ ] **IST8310** magnetometer: I2C4, address 0x0C.
- [ ] **MS5611** barometer: I2C4, address 0x77. Keep it away from heat and
      shield it from light and airflow.
- [ ] **24LC64** calibration EEPROM: I2C4, address 0x51.
- [ ] **IMU heater**: resistor(s) next to the IMUs, low-side MOSFET driven by
      `FMU_HEATER` (PB9), gate pull-down.
- [ ] Orientation: note each sensor's axes on the sheet. The FMUv6C rotations
      (`rc.board_sensors`: ICM-42688-P `-R 6`) only hold if the part is placed
      as on the Pixhawk 6C; the BMI270 has no reference rotation.

### C4. Parameter storage

- [ ] **FRAM or EEPROM** *(open 1)*: SPI2 (`FMU_SPI2_SCK_NVM`, `_MISO_`, `_MOSI_`),
      CS `FMU_SPI2_CS_NVM` (PD4) with pull-up, on `FMU_VDD_3V3`. FMUv6C part:
      FM25V02A (ref: DS-018).

### C5. CAN

- [ ] **CAN1 transceiver** (TCAN1044V, VSON-8 DRB; replaces the FMUv6C's
      TJA1051): `FMU_CAN1_TX`/`FMU_CAN1_RX` (U1 PD1/PD0) → `CAN1_H`/`CAN1_L`.
      VCC on `+5V`, VIO on `FMU_VDD_3V3`, STB low for normal mode.
- [ ] **CAN2 transceiver** (TCAN1044V): `FMU_CAN2_TX`/`FMU_CAN2_RX` (U1 PB13/PB5)
      → `CAN2_H`/`CAN2_L`.
- [ ] Termination: decide whether each bus has an on-board 120 Ω (fixed or
      jumpered); ESD protection at both connectors.

### C6. Connectors

Pin order as in `specs/diagrams/block-diagram.md` section 6 (ref: Holybro port
tables, DS-009). ESD protection and series resistors on every external signal.

- [ ] **TELEM1** JST-GH 6: `VDD_5V_HIPOWER`, UART7 `FMU_UART7_*_TEL1`.
- [ ] **TELEM3** JST-GH 6: `VDD_5V_PERIPH`, USART2 `FMU_USART2_*_TEL3`.
- [ ] **GPS1** JST-GH 10: `VDD_5V_PERIPH`, USART1, I2C1, `IO_SAFETY_SWITCH`,
      `N_IO_LED_SAFETY`, `IO_VDD_3V3`, buzzer (driver from `FMU_BUZZER`, PB0), GND.
- [ ] **GPS2** JST-GH 6: `VDD_5V_HIPOWER`, UART8, I2C2.
- [ ] **I2C** JST-GH 4: `VDD_5V_PERIPH`, I2C2.
- [ ] **CAN1**, **CAN2** JST-GH 4 each.
- [ ] **FMU debug** JST-SH 10: `FMU_VDD_3V3`, `FMU_USART3_TX_DEBUG`,
      `FMU_USART3_RX_DEBUG`, `FMU_SWDIO`, `FMU_SWCLK`, NC, NC, NC, `FMU_NRST`, GND.

### C7. IO processor and RC (U2, STM32F103C8T6)

All pins in `specs/pinout/io.md` (ref: PX4 `boards/px4/io-v2`).

- [ ] **U2** with decoupling; `IO_VDD_3V3`; VDDA through a ferrite.
- [ ] **24 MHz crystal** on `IO_OSC_IN`/`IO_OSC_OUT`.
- [ ] **BOOT0** and **BOOT1** (PB2) pulled low; `IO_NRST` to the IO debug connector.
- [ ] **FMU link**: `FMU_USART6_TX_TO_IO`, `FMU_USART6_RX_FROM_IO`, direct.
- [ ] **PPM/S.BUS input**: connector pin → `IO_PPM_IN` (PA8), and through an
      inverter → `IO_USART3_RX_SBUS_IN` (PB11).
- [ ] **S.BUS output**: `IO_USART3_TX_SBUS_OUT` (PB10) through an inverter gated
      by `N_IO_SBUS_OUT_EN` (PB4).
- [ ] **RSSI input**: connector pin → `IO_RSSI_ADC` (PA5) and `IO_RSSI_PWM` (PA12),
      with protection for 3.3 V.
- [ ] **DSM**: `IO_USART1_RX_DSM` (PA10) to the JST-ZH connector, powered from
      `VDD_3V3_SPEKTRUM`.
- [ ] **Servo rail sense**: divider from `VDD_SERVO` (0 to 36 V) → `IO_VSERVO_SENSE`
      (PA4); `N_IO_SERVO_FAULT` (PA15) pull-up.
- [ ] **Safety switch**: `IO_SAFETY_SWITCH` (PB5) pull-down; `N_IO_LED_SAFETY` (PB13).
- [ ] **LEDs**: `N_IO_LED_BLUE` (PB14), `N_IO_LED_AMBER` (PB15), `IO_LED_GREEN` (PA11).
- [ ] **Board sense**: `IO_HW_DETECT1` (PC14) and `IO_HW_DETECT2` (PC15) left open.
- [ ] **Connectors**: DSM (JST-ZH 3), PPM/SBUS RC (JST-GH 5), SBUS OUT (JST-GH 3),
      IO debug (JST-SH 10: `IO_VDD_3V3`, `IO_USART1_TX_DEBUG`, NC, `IO_SWDIO`,
      `IO_SWCLK`, `IO_SWO`, NC, NC, `IO_NRST`, GND).

### C8. PWM outputs

- [ ] **FMU PWM buffer**: `FMU_CH1`..`FMU_CH8` → JST-GH 10 (FMU PWM / AUX).
- [ ] **IO PWM buffer**: `IO_CH1`..`IO_CH8` → JST-GH 10 (IO PWM / MAIN).
- [ ] Buffer supply selectable 3.3 V / 5 V by a solder jumper (ref: Holybro
      "PWM signal voltage mod"). `VDD_SERVO` on pin 1 of both connectors is the
      externally powered servo rail; it is sensed, never driven by the board.

## After capture

- [ ] `pinmap check --project specs/pinout/{fmu,io,soc}.pinasg.ron` clean and
      `specs/tools/check_nets.py` passing after any pin change.
- [ ] Every net label on U1, U2 and U3 matches its pinasg net.
- [ ] ERC clean; BOM exported; open questions in `decisions.md` closed or carried.
