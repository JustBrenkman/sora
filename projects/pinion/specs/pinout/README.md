<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# pinion pin maps

The source of truth for pin assignments. Firmware board files, the device tree
and the schematic follow these files.

They are [pinmap](https://github.com/JustBrenkman/pinmap) documents: a **pindef**
says what a chip's pins can do, a **pinasg** says what pinion uses them for.

| Processor | Refdes | Definition (pindef) | Assignment (pinasg) | Generated pinout |
|---|---|---|---|---|
| STM32H743VIH6, TFBGA100 (flight controller) | U1 | `stm32h743vih6.pindef.json` | `fmu.pinasg.ron` | [`fmu.md`](fmu.md) |
| STM32F103C8T6, LQFP48 (PX4IO) | U2 | `stm32f103c8t6.pindef.json` | `io.pinasg.ron` | [`io.md`](io.md) |
| AM62L32, ANB 373-ball (Linux) | U3 | `am62l32.pindef.json` | `soc.pinasg.ron` | [`soc.md`](soc.md) |

## Reading

Open the generated `.md` files, or ask pinmap. The folder holds three projects,
so every command names one with `--project`:

```sh
pinmap pin list --project fmu.pinasg.ron            # every pin: pad, use, net
pinmap pin list --project soc.pinasg.ron --free     # unused pins
pinmap pin show PA5 --project fmu.pinasg.ron        # what a pin can do and does
pinmap pin list --project soc.pinasg.ron --can UART4.RXD   # where a signal can go
pinmap periph show UART5 --project fmu.pinasg.ron
```

## Changing

Edit through pinmap, never by hand, then regenerate the Markdown:

```sh
pinmap assign periph UART4 RXD=GPMC0_CSn2:EXP_UART_RX --project soc.pinasg.ron
pinmap assign pin PB12 --mode gpio-out --net FMU_SPARE --project fmu.pinasg.ron
pinmap note PB12 "what it is for" --project fmu.pinasg.ron
pinmap unassign PB12 --project fmu.pinasg.ron

for p in fmu io soc; do
  pinmap check --project $p.pinasg.ron
  pinmap emit --project $p.pinasg.ron --to markdown -O free-pins=true -o $p.md
done
../tools/check_nets.py
```

pinmap refuses an edit that would put a signal on a pin that cannot carry it or
use a pin twice. `check_nets.py` adds what pinmap cannot see across chips: nets
shared by two processors must pair TX with RX and RTS with CTS, and an AM62L
pin wired to an STM32 must be in a 3.3 V I/O group.

`pinmap check` reports `PM0110` notes for nets that sit on several pins. Those
are the supply and ground balls and are expected.

## Conventions

- **Pin names.** STM32: port pins (`PA5`). AM62L: the ball name from the
  datasheet (`GPMC0_AD12`), which is also its PADCONFIG name. Supply names that
  cover several balls carry the ball (`VSS_A1`, `VDD_CORE_J11`).
- **Net names** are the schematic labels. Flight-controller nets keep the
  FMUv6C names (`FMU_SPI1_SCK_SENSOR`); `N_` marks active-low; a net between two
  processors is named from the FMU's side (`FMU_UART5_TX_SOC` is the FMU's
  transmit and the AM62L's receive).
- **Notes** end with their origin: "FMUv6C." or "PX4 io-v2." for a pin copied
  from the reference, "As the EVM." for the AM62L, and "DEVIATION:" where pinion
  differs. The reasons are in [`../notes/decisions.md`](../notes/decisions.md).
- **Mux values.** STM32H7: alternate function number. STM32F1: the remap
  setting of the peripheral (0 is the default mapping). AM62L: PADCONFIG
  MUXMODE. Functions with no mux setting (crystal, USB, DDR, boot straps) are
  `fixed`; ADC inputs are `analog`.
- **TFBGA100 quirks.** PC2 and PC3 are the `PC2_C`/`PC3_C` balls. There is no
  VREF+ ball; it is bonded to VDDA.

## What is not in these files

pinmap has no field for these, so they live elsewhere:

- The AM62L I/O supply group and PADCONFIG address of each ball:
  [`../notes/am62l-io-domains.md`](../notes/am62l-io-domains.md).
- Pull resistors, reset state and drive strength beyond pinmap's `bias`,
  `drive` and `speed`: in the note text.

## Regenerating the definitions

pinmap has no importers yet, so the pindef files are produced by scripts in
[`../tools/`](../tools/) from the fetched reference data:

```sh
../fetch.sh
../tools/gen_stm32_pindef.py     # from ST's STM32_open_pin_data XML
../tools/gen_am62l_pindef.py     # from the AM62L datasheet, Table 5-1
```

`gen_am62l_pindef.py` needs `pdftotext` (poppler). It checks every signal's
balls against the datasheet's Signal Descriptions tables and stops if they
disagree or the ball count is not 373. The datasheet URL always serves the
latest revision; after a new revision, rerun the script and review the diff.
