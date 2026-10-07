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

- [x] **POWER1**, **POWER2** JST-GH 6 (ref: Holybro port table): 5 V, 5 V,
      CURRENT, VOLTAGE, GND, GND. A purchased power module supplies regulated
      5 V and the two analog signals; there is no battery connector or battery
      regulator on the board.
- [x] **Sense inputs**: RC filter and clamp on each, 3.3 V full scale →
      `FMU_PWR1_VOLTAGE` (U1 PC5), `FMU_PWR1_CURRENT` (PC4), `FMU_PWR2_VOLTAGE`
      (PB1), `FMU_PWR2_CURRENT` (PA2). Default scales 18.18 V/V and 36.36 A/V (ref: v6C `hwdef.dat`).
- [ ] **Power selector** (ideal diodes, one source at a time) →
      `+5V`. Reports `PWR1_VALID` (U1 PA15), `PWR2_VALID` (PB12),
      `N_USB_VBUS_VALID` (PE15), active low, pulled up to `FMU_VDD_3V3` (ref: v6C
      `board_config.h`). Parts: an LM73100 on each of POWER1 and POWER2 (5.5 A,
      overvoltage cutoff on OVLO) and an LM66100 on the USB input. The LM73100's
      PG is open-drain and high when valid, so the active-low valid signals
      need an inversion.
      Its USB input is `USBC_VBUS` from the AM62L's USB-C port *(open 3)*.
- [x] **Input protection**: TVS and overvoltage protection on each 5 V input
      (FMUv6C maximum input is 6 V).
- [ ] **5 V monitor divider** 2:1 → `FMU_SCALED_V5` (U1 PA4) (ref: v6C, `SCALE(2)`).
- [x] **5 V budget** *(open 2)*: confirm the power module covers the AM62L
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

- [x] **Stack mounting holes** (ref: `specs/notes/mechanical.md`): four
      non-plated Ø3.2 mm holes on a 30.5 x 30.5 mm square centred on the board.
      Place them as
      mounting-hole symbols so they reach the PCB with their keep-outs.
- [ ] Airframe mounting holes, fiducials and test points, once the outline is set.

## B. Linux computer

### B1. Power

Follow TI's "AM62L Power Supply Implementation" note (to be added to
`specs/reference/ti/` by hand) and the sequencing in DS section 6.11.2.

- [ ] **3.3 V buck** (SY8120IABC, as on the FMU side) from `+5V` → `+3V3`, the
      Linux side's general 3.3 V rail.
- [ ] **PMIC TPS6521402** (the AM62L variant listed for DDR4; the EVM's
      TPS6521401 is LPDDR4 only), input from `+5V`: Buck1 → `VDD_CORE_0V75`; Buck2 → `SOC_DVDD_1V8`;
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

- [x] **3.3 V regulator** (SY8120IABC buck, SOT-23-6, 2 A, LCSC C479076) from
      `+5V` → `FMU_VDD_3V3`. Supplies U1, U2's
      rail, the sensor switch, CAN transceivers, parameter storage.
- [x] **Analog filter** (ferrite + capacitors) → `FMU_VDDA_3V3` (U1 VDDA; VREF+ is
      bonded to VDDA in this package).
- [x] **Sensor rail switch** (SY6288AAAC, 0.6 A, LCSC C111829) → `FMU_VDD_3V3_SENSORS`,
      enable `FMU_VDD_3V3_SENSORS_EN` (U1 PB2, active high, pull-down so it is off by
      default). PX4 power-cycles the sensors with it (ref: v6C). The switch's fault
      flag is pulled up and leaves the sheet as `FMU_VDD_3V3_SENSORS_FLT` (active low),
      but is not connected to the FMU: the FMUv6C has no sensor-rail overcurrent input.
- [x] **`FMU_VDD_5V_PERIPH` switch** (SY6288CAAC, 2 A, LCSC C111830; limits between
      2.1 A and 3.7 A): enable `FMU_VDD_5V_PERIPH_EN` (U1 PE2, active high, pull-down;
      active low on the FMUv6C), fault `FMU_VDD_5V_PERIPH_FLT` (U1 PE3, pull-up to
      `FMU_VDD_3V3`). Feeds TELEM3, GPS1, I2C, CAN1, CAN2, RC (ref: v6C, Holybro spec).
- [x] **`FMU_VDD_5V_HIPWR` switch** (SY6288CAAC): enable `FMU_VDD_5V_HIPWR_EN`
      (U1 PC10, active high, pull-down), fault `FMU_VDD_5V_HIPWR_FLT` (U1 PC11,
      pull-up). Feeds TELEM1 and GPS2 (ref: v6C, Holybro spec).
- [x] **IO rail**: U2 and the GPS1 connector pin 8 run from `FMU_VDD_3V3`; there
      is no separate IO rail.
- [x] **Spektrum switch** (SY6288AAAC) → `IO_VDD_3V3_SPEKTRUM`, enable
      `IO_VDD_3V3_SPEKTRUM_EN` (U2 PC13, active high).
- [ ] **`FMU_VBAT`** (U1 VBAT): backup supply; tie to `FMU_VDD_3V3` or a backup
      cell. DS-018 lists a battery-backed RTC, but the FMUv6C pinout has no LSE
      crystal (PC14/PC15 are chip selects).

### C2. MCU (U1, STM32H743VIH6)

- [x] **U1**. All 100 balls are in `specs/pinout/fmu.md`; 8 I/O are free
      (PB3, PB4, PB14, PB15, PC14, PD6, PD7, PE5).
- [x] **Decoupling**: per VDD ball plus bulk; `FMU_VCAP1`, `FMU_VCAP2` capacitors
      to GND; `VDDLDO`, `VDD33_USB`, `PDR_ON` to `FMU_VDD_3V3`. Take values from
      the STM32H743 datasheet (DS12110, to be added to `specs/reference/st/` by hand).
- [x] **16 MHz crystal** + load capacitors on `FMU_OSC_IN`/`FMU_OSC_OUT`
      (PH0/PH1) (ref: v6C `board.h`, `STM32_BOARD_XTAL`).
- [x] **Reset**: `FMU_NRST` with capacitor and push button (SW1), to the debug
      connector.
- [x] **FMU debug** JST-SH 10 (J3, on the MCU sheet; the connectors sheet holds
      only the Pixhawk-standard external connectors): `FMU_VDD_3V3`,
      `FMU_USART3_TX_DEBUG`, `FMU_USART3_RX_DEBUG`, `FMU_SWDIO`, `FMU_SWCLK`, NC, NC,
      NC, `FMU_NRST`, GND. The 10-pin connector is kept over the 6-pin Debug Mini
      because the Mini has no reset pin.
- [ ] **Jig test points** (1.5 mm pads): SWDIO (TP13), SWCLK (TP14),
      `FMU_USART3_TX_DEBUG` (TP15), `FMU_USART3_RX_DEBUG` (TP16), `FMU_NRST` (TP17),
      GND (TP18); `FMU_BOOT0` already has TP12.
- [x] **`FMU_BOOT0`**: pull-down and test pad *(open 5)*.
- [x] **Hardware version/revision dividers**: `HW_VER_REV_DRIVE` (PE12) feeds two
      resistor pairs sensed on `HW_VER_SENSE` (PC1) and `HW_REV_SENSE` (PC0).
      Resistor pairs per ID are in the "HW REV and VER ID" sheet of
      `specs/reference/px4-docs/fmuv6c-pinout.xlsx`. pinion is version 1,
      revision 0: 174k over 32.4k on `HW_VER_SENSE`, 442k over 24.9k on
      `HW_REV_SENSE` (recorded in `specs/notes/decisions.md`).
- [x] **Status LEDs**: red `N_FMU_LED_RED` (PD10, D9 with 1k), blue
      `N_FMU_LED_BLUE` (PD11, D10 with 330R), active low, to `FMU_VDD_3V3`.
- [x] **Pull-ups** on I2C1, I2C2 (2.2k to `FMU_VDD_3V3`) and I2C4 (4.7k to
      `FMU_VDD_3V3_SENSORS`).

### C3. Sensors

The two IMUs, the calibration EEPROM and the heater are on the isolated IMU
board, `hardware/pinion-imu` (deviation F8), joined by a 22-way 0.5 mm FFC. The
barometer and magnetometer stay on this board. Everything runs from
`FMU_VDD_3V3_SENSORS` (ref: v6C sensor table, DS-018).

Main board, sensors sheet:

- [x] **IMU board connector** (J4, FFC 22): SPI1 (`FMU_SPI1_SCK_SENSOR`, `_MOSI_`,
      `_MISO_`), `FMU_SPI1_CS1_BMI270`, `FMU_SPI1_CS3_ICM42688`,
      `FMU_SPI1_DRDY1_BMI270`, `FMU_SPI1_DRDY3_ICM42688`, I2C4, `FMU_HEATER`,
      `FMU_VDD_3V3_SENSORS`, `+5V` for the heater. Pin order is in
      `specs/diagrams/block-diagram.md` section 6 and `hardware/pinion-imu/README.md`.
- [x] **IST8310** magnetometer: I2C4, address 0x0C.
- [x] **MS5611** barometer: I2C4, address 0x77. Keep it away from heat and
      shield it from light and airflow.

IMU board (`hardware/pinion-imu`):

- [x] **ICM-42688-P** (IMU 2): SPI1, CS `FMU_SPI1_CS3_ICM42688`, INT →
      `FMU_SPI1_DRDY3_ICM42688`. Pins 7, 9 and 11 to GND; 10 nF on VDDIO (ref: TDK
      datasheet section 4, `reference/parts/`).
- [x] **BMI270** (IMU 1, replaces the FMUv6C's BMI088, deviation F9): SPI1, CS
      `FMU_SPI1_CS1_BMI270`, INT1 → `FMU_SPI1_DRDY1_BMI270`; INT2 and the
      auxiliary interface pins unconnected (ref: BMI270 datasheet section 7).
- [x] **24LC64** calibration EEPROM: I2C4, address 0x51.
- [x] **IMU heater**: a PCB trace under the IMUs (R1, about 10R, drawn in layout
      and needing a footprint) from `+5V` to a constant-current sink on the same
      board, enabled by `FMU_HEATER` (PB9). The GPIO biases an LM4040-2.5 (U4)
      through 1.5k; 47k/3k sets 0.15 V at the TLV9001 (U5), which drives an
      AO3400A (Q1) so that 0.15 V appears across the 0.5R sense resistor:
      0.30 A. Trace and Q1 together dissipate about 1.5 W whatever the trace
      resistance. 100k pull-down on `FMU_HEATER`; 1k and 1 nF around the op-amp.
      Place Q1 away from, or centred between, the two IMUs.
- [ ] Orientation, noted on both sheets and kept as on the FMUv6C so its
      `rc.board_sensors` rotations carry over. All parts on the top side; seen from
      above:
      - ICM-42688-P: +X to port, +Y aft, pin 1 at the aft-starboard corner
        (`icm42688p -R 6`).
      - BMI270: +X aft, +Y to starboard, pin 1 at the aft-starboard corner
        (`bmi270 -R 4`, the rotation the FMUv6C gives its BMI088).
      - IST8310: +X forward, +Y to starboard (no rotation). Its pin 1 corner is
        not in the brief datasheet; take it from the full one before layout.
      Check each against the PX4 driver's own axis convention before layout.

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

Drawn on the sheet: the seven connectors (J5 TELEM1, J6 TELEM3, J7 GPS1, J8 GPS2,
J9 I2C, J10 CAN1, J11 CAN2) and their protection. Each entry stays open until
the `fmu` sheet has the matching sheet pins and the source sheets export the
nets: `mcu` (UART7, USART2, USART1, UART8, `FMU_BUZZER`; it has the I2C labels
already), `io-mcu` (`IO_SAFETY_SWITCH`, `N_IO_LED_SAFETY`) and `can` (the two
bus pairs).

Common to the sheet:

- **Connectors**: JST-GH side entry, `SM04B-GHS-TB`, `SM06B-GHS-TB`,
  `SM10B-GHS-TB`; symbol `Connector_Generic_MountingPin:Conn_01xNN_MountingPin`
  as J4, mounting pin to GND. Top entry is `BMxxB-GHS-TBT` (`..._Vertical`
  footprints) if the layout wants it; POWER1/POWER2 (J1, J2) still have no
  footprint and take the same choice.
- **Rails** are the renamed power symbols already used on `fmu-power`.
- **Signal path**: connector pin, ESD array line, series resistor, processor.
  The net between connector and resistor carries the port's name (`TELEM1_TX`,
  `GPS1_SCL`, ...). Resistors are 0402: 100R on UART lines, 22R on I2C lines
  (the 2.2k pull-ups stay on the `mcu` sheet, processor side).
- **ESD**: TPD4E05U06DQA (TI, USON-10 2.5 x 1 mm, four lines, 0.5 pF, LCSC
  C138714), U19 to U23. It has no supply pin, which matters here: PX4 switches
  the port rails off, and an array with a rail pin (SRV05-4 with VP on the
  rail) would feed the dead rail from any signal driven high. CAN pairs use
  NUP2105L (SOT-23, LCSC C14486), D11 and D12.
- **Rail clamps**: one SMF6.0A (SOD-123FL, LCSC C2857264) and 1 µF on each
  switched 5 V rail, D14/C56 on `FMU_VDD_5V_PERIPH` and D15/C57 on
  `FMU_VDD_5V_HIPWR`. 6 V stand-off as on the POWER inputs, because DS-009
  allows a 5.3 V supply.

- [x] **TELEM1** (J5): 1 `FMU_VDD_5V_HIPWR`, 2 `FMU_UART7_TX_TEL1`,
      3 `FMU_UART7_RX_TEL1`, 4 `FMU_UART7_CTS_TEL1`, 5 `FMU_UART7_RTS_TEL1`, 6 GND.
      R50 to R53, U19.
- [x] **TELEM3** (J6): 1 `FMU_VDD_5V_PERIPH`, 2 `FMU_USART2_TX_TEL3`,
      3 `FMU_USART2_RX_TEL3`, 4 NC, 5 NC, 6 GND. R54, R55, half of U20.
- [x] **GPS1** (J7): 1 `FMU_VDD_5V_PERIPH`, 2 `FMU_USART1_TX_GPS1`,
      3 `FMU_USART1_RX_GPS1`, 4 `FMU_I2C1_SCL_GPS1`, 5 `FMU_I2C1_SDA_GPS1`,
      6 `IO_SAFETY_SWITCH`, 7 `N_IO_LED_SAFETY`, 8 `FMU_VDD_3V3`, 9 buzzer, 10 GND.
      R56 to R59; 1k (R60) in series with the switch input (its pull-down is on
      the IO sheet, C7) and 220R (R61) with the LED; U21 and U22, one line spare.
  - [x] **Pin 8 supply**: 0603 polyfuse, 100 mA hold (F1, part to select), and
        100 nF (C55), since pinion feeds this pin from the processors' own
        `FMU_VDD_3V3` and a shorted cable would otherwise take U1 and U2 down.
        On the FMUv6C the pin is on the separate `IO_VDD_3V3`.
  - [x] **Buzzer driver**: pin 9 (`GPS1_BUZZER`) is the buzzer's low side
        (Holybro: "BUZZER-", 0 to 5 V; DS-009: 5 to 24 V); the buzzer's other
        terminal is the 5 V on pin 1, inside the GPS module. AO3400A (Q5, LCSC
        C20917), gate from `FMU_BUZZER` through 100R (R68) with 100k to GND
        (R69); 1N5819WS (D13, LCSC C191023) from the drain to
        `FMU_VDD_5V_PERIPH` as the flyback path for a magnetic buzzer.
- [x] **GPS2** (J8): 1 `FMU_VDD_5V_HIPWR`, 2 `FMU_UART8_TX_GPS2`,
      3 `FMU_UART8_RX_GPS2`, 4 `FMU_I2C2_SCL_GPS2`, 5 `FMU_I2C2_SDA_GPS2`, 6 GND.
      R62 to R65, U23.
- [x] **I2C** (J9): 1 `FMU_VDD_5V_PERIPH`, 2 `FMU_I2C2_SCL_GPS2`,
      3 `FMU_I2C2_SDA_GPS2`, 4 GND. Its own pair of 22R (R66, R67), so a fault on
      one I2C2 connector is not hard across the other; ESD on the other half of
      U20, which puts J6 and J9 side by side in layout.
- [x] **CAN1** (J10), **CAN2** (J11): 1 `FMU_VDD_5V_PERIPH`, 2 `CANx_H`,
      3 `CANx_L`, 4 GND. D11, D12; no series resistors. This is the connector
      ESD that C5 asks for.

### C7. IO processor and RC (U2, STM32F103C8T6)

All pins in `specs/pinout/io.md` (ref: PX4 `boards/px4/io-v2`).

- [ ] **U2** with decoupling; `FMU_VDD_3V3`; VDDA through a ferrite.
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
      `IO_VDD_3V3_SPEKTRUM`.
- [ ] **Servo rail sense**: divider from `VDD_SERVO` (0 to 36 V) → `IO_VSERVO_SENSE`
      (PA4); `N_IO_SERVO_FAULT` (PA15) pull-up.
- [ ] **Safety switch**: `IO_SAFETY_SWITCH` (PB5) pull-down; `N_IO_LED_SAFETY` (PB13).
- [ ] **LEDs**: `N_IO_LED_BLUE` (PB14), `N_IO_LED_AMBER` (PB15), `IO_LED_GREEN` (PA11).
- [ ] **Board sense**: `IO_HW_DETECT1` (PC14) and `IO_HW_DETECT2` (PC15) left open.
- [ ] **Connectors**: DSM (JST-ZH 3), PPM/SBUS RC (JST-GH 5), SBUS OUT (JST-GH 3),
      IO debug (JST-SH 10: `FMU_VDD_3V3`, `IO_USART1_TX_DEBUG`, NC, `IO_SWDIO`,
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
