#!/usr/bin/env bash
# Check out PX4-Autopilot at the tag in PX4_VERSION and link the sora board
# vendor folder into it. The checkout lives in the gitignored build/ folder.
set -euo pipefail

firmware=$(cd "$(dirname "$0")/.." && pwd)
version=$(<"$firmware/PX4_VERSION")
px4="$firmware/build/PX4-Autopilot"

if [[ ! -d $px4/.git ]]; then
	git clone --branch "$version" --recurse-submodules --shallow-submodules \
		https://github.com/PX4/PX4-Autopilot.git "$px4"
else
	git -C "$px4" fetch --tags origin
	git -C "$px4" checkout "$version"
	git -C "$px4" submodule update --init --recursive
fi

ln -sfn "$firmware/px4/boards/sora" "$px4/boards/sora"

echo "PX4 $version is ready in $px4"
echo "Build with: make -C $px4 sora_pinion_default"
