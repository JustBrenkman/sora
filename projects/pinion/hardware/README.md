# pinion hardware

KiCad projects, one folder per board.

| Board                        | Description                                  | Status      |
| ---------------------------- | -------------------------------------------- | ----------- |
| [pinion-main](pinion-main/)  | Main board: AM62L and STM32H743              | Schematic in progress |
| [pinion-imu](pinion-imu/)    | Isolated IMU board: two IMUs, calibration EEPROM, heater | Schematic drawn; no layout |

Accessory boards (debug adapter, breakouts, power modules) get their own folder
next to `pinion-main/` and a row in this table.

## Libraries

Symbols, footprints and 3D models come from the shared library submodule at
`lib/kicad` in the repo root. Reference it from each project's own
`sym-lib-table` and `fp-lib-table` with a path relative to the project:

```
${KIPRJMOD}/../../../../lib/kicad/symbols/<name>.kicad_sym
${KIPRJMOD}/../../../../lib/kicad/footprints/<name>.pretty
```

Parts needed only by pinion still go into the shared library, so every board in
the repo draws from one place.
