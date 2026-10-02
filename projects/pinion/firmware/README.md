# pinion firmware

PX4 board support for the STM32H743 flight controller. Only the board files
live here; PX4 itself is checked out by a script.

| Path                       | Contents                                             |
| -------------------------- | ---------------------------------------------------- |
| `PX4_VERSION`              | Pinned PX4-Autopilot tag                             |
| `px4/boards/sora/pinion/`  | Board files, laid out exactly as in the PX4 tree     |
| `scripts/setup-px4.sh`     | Clones PX4 at the pinned tag and links `boards/sora` |
| `build/`                   | PX4 checkout and build output; gitignored            |

## Board files

`px4/boards/sora/pinion/` is empty. It will hold the same set of files as the
reference board `boards/px4/fmu-v6c`:

```
default.px4board        bootloader.px4board     firmware.prototype
nuttx-config/           # include/board.h, nsh/defconfig, bootloader/, scripts/
src/                    # board_config.h, spi.cpp, i2c.cpp, timer_config.cpp, ...
init/                   # rc.board_defaults, rc.board_sensors
```

The FMUv6C versions of the key files are downloaded by `../specs/fetch.sh` into
`../specs/reference/px4-fmu-v6c/`.

## Building

```sh
scripts/setup-px4.sh
make -C build/PX4-Autopilot sora_pinion_default
```

The build has not been run yet: there are no board files to build. Whether
PX4's board discovery accepts a symlinked vendor folder also needs confirming
on the first build; if it does not, the script should copy instead of link.
