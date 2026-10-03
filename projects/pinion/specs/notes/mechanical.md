<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# pinion mechanical specification

## Stack mounting holes

pinion carries the 30.5 mm square hole pattern used by FPV flight-controller
stacks, centred on the board, so that off-the-shelf power distribution boards and 4-in-1
ESCs bolt straight onto it. pinion is not itself an FPV-sized board; the
pattern sits inside a larger outline.

There is no formal standard for these patterns. They are a convention that
every vendor follows, and the numbers below are taken from vendor product
specifications (listed under Sources).

### The patterns in use

| Pattern (hole centres) | Screw | Hole in the mounted board | Typical board | Used for |
|---|---|---|---|---|
| 30.5 x 30.5 mm | M3 | Ø4 mm with a silicone grommet (flight controllers, most 4-in-1 ESCs); Ø3 mm bare (PDBs) | 36 x 36 mm FC; about 41 x 45 mm ESC | 5 inch and larger; the widest choice of ESCs and PDBs |
| 20 x 20 mm | M2 or M3 | Ø2 mm bare, or Ø3 to 4 mm with a grommet; some are "M2 expandable to M3" | about 30 x 30 mm | Smaller ESCs and "mini" stacks |
| 25.5 x 25.5 mm | M2 | Ø2 to 3 mm | whoop / AIO boards | Tiny builds; no stand-alone ESCs or PDBs worth supporting |

### What pinion provides

Only the 30.5 x 30.5 mm pattern. The 20 x 20 mm pattern is not fitted.

| | |
|---|---|
| Pattern | 30.5 x 30.5 mm square, 4 holes |
| Position | Centred on the board centre, sides parallel to the board edges |
| Hole coordinates from the centre | (±15.25, ±15.25) mm |
| Screw | M3 |
| Finished hole diameter | 3.2 mm (M3 clearance) |
| Plating | Non-plated |
| Position tolerance | ±0.1 mm |
| Keep-out, both sides | Ø7.0 mm around each hole: no copper, components or silkscreen |

Why these values:

- pinion is the host, so its holes fit the screw, not a grommet. The vibration
  grommets belong to the boards that mount on it, whose Ø4 mm holes take an
  M3 screw through a grommet and whose Ø3 mm holes take it directly.
- 3.2 mm is the normal clearance hole for M3.
- The Ø7 mm keep-out clears an M3 hex standoff (5.5 mm across flats, 6.4 mm
  across corners) and an M3 nut or screw head.
- Non-plated holes keep stack hardware from tying another board's ground or
  battery negative to pinion's ground through a screw. If a grounded hole is
  wanted for shielding, make that a deliberate, single-point choice.

### Consequences for the layout

- The holes pass through the middle of the board. The four holes box in a
  23.5 x 23.5 mm area between their keep-outs. Neither BGA has to sit there, but the AM62L, its DDR4 routing and the STM32H743 must be placed
  around the pattern, not across it.
- A stacked ESC or PDB covers roughly 45 x 46 mm over the centre. Keep tall
  parts, connectors that need access, the barometer and antennas out from under
  it, and leave room for its battery leads and motor wires.
- Stack spacing is set by standoffs. Check the height of pinion's tallest centre-area part against
  the standoff chosen.
- The IMUs do not need to be at the hole pattern's centre, but if they are on
  the main board, keep them away from the ESC's switching currents.
- Board outline, corner mounting holes for the airframe, and total thickness
  are not specified yet.

### Sources

- HAKRC F4530D flight controller, 36 x 36 mm board, 30.5 x 30.5 mm, Ø4 mm:
  <https://www.getfpv.com/hakrc-f4530d-3-6s-flight-controller.html>
- SpeedyBee 45A 4-in-1 ESC, 30.5 x 30.5 mm, 4 mm holes, 41 x 45 mm:
  <https://www.getfpv.com/discontinued/speedybee-45a-3-6s-blheli-32-4-in-1-esc.html>
- T-Motor F45A V2 4-in-1 ESC, 45 x 41 mm:
  <https://www.getfpv.com/t-motor-f45a-v2-3-6s-blheli-32-4-in-1-esc.html>
- HGLRC Forward 65A 4-in-1 ESC, 46 x 45 mm:
  <https://www.getfpv.com/hglrc-forward-65a-l431-3-6s-blheli-32-4-in-1-esc.html>
- Matek FCHUB-A5 PDB, 30.5 mm and 20 mm patterns, Ø3 mm:
  <https://www.getfpv.com/matek-fchub-a5-w-current-sensor-184a-bec-5v-2a.html>
- Matek FCHUB-6S PDB, 30.5 mm, Ø3 mm:
  <https://www.getfpv.com/drone-brands/maytek-systems/matek-fchub-6s-pdb.html>
- FETtec 35A 20 x 20 ESC, "M2 expandable to M3":
  <https://www.getfpv.com/electronics/electronic-speed-controllers-esc/4-in-1-esc-s/fettec-35a-20x20-4-in-1-esc.html>
- HGLRC Zeus 28A 20 x 20 ESC, M3:
  <https://www.getfpv.com/hglrc-zeus-28a-3-6s-4-in-1-blheli-s-esc.html>
- Diatone Mamba F30 Mini 20 x 20 ESC, M2:
  <https://www.racedayquads.com/products/diatone-mamba-f30-mini-30a-20x20-4in1-esc>
- Whoop boards at 25.5 x 25.5 mm:
  <https://intofpv.com/t-beta85x-frame-fc-mounting-pattern-and-cheap-fc-choise>
