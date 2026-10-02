# pinion linux

Linux board support for the AM62L. Distro-independent pieces are kept once and
each build system gets a thin folder that consumes them.

| Folder      | Contents                                                          |
| ----------- | ----------------------------------------------------------------- |
| `dts/`      | Device tree sources: `k3-am62l-sora-pinion.dts` and its includes  |
| `kernel/`   | Defconfig fragments and kernel patches                            |
| `u-boot/`   | U-Boot defconfig and patches                                      |
| `armbian/`  | Armbian board config, userpatches and `customize-image.sh`        |
| `build/`    | Upstream checkouts and images; gitignored                         |

Another distro (Yocto, Buildroot, plain Debian) is added as a folder next to
`armbian/` and reuses `dts/`, `kernel/` and `u-boot/`.

## Pinned versions

| Component      | Version      |
| -------------- | ------------ |
| Linux kernel   | Not chosen   |
| U-Boot         | Not chosen   |
| Armbian build  | Not chosen   |

Record the version here when a component is first built, so the patches in
this folder are tied to a known base.
