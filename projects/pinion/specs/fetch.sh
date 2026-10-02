#!/usr/bin/env bash
# Download the reference documents listed in sources.yaml into reference/.
#
#   ./fetch.sh          download missing files and verify checksums
#   ./fetch.sh --sums   print the sha256 of every downloaded file
set -euo pipefail

cd "$(dirname "$0")"
manifest=sources.yaml
dest=reference
mode=${1:-}
failed=0
missing=()

process() {
	local id=$1 file=$2 url=$3 sum=$4
	local path="$dest/$file"

	if [[ ! -f $path ]]; then
		mkdir -p "$(dirname "$path")"
		if ! curl -fsSL -A 'Mozilla/5.0' -o "$path.part" "$url"; then
			rm -f "$path.part"
			echo "FAIL  $id: download failed"
			missing+=("$path"$'\t'"$url")
			failed=1
			return
		fi
		mv "$path.part" "$path"
	fi

	local actual
	actual=$(shasum -a 256 "$path" | cut -d' ' -f1)

	if [[ $mode == --sums ]]; then
		echo "$actual  $id"
	elif [[ -z $sum ]]; then
		echo "ok    $id (no checksum recorded)"
	elif [[ $actual == "$sum" ]]; then
		echo "ok    $id"
	else
		echo "FAIL  $id: checksum mismatch, the upstream file may have been revised"
		echo "      expected $sum"
		echo "      actual   $actual"
		failed=1
	fi
}

id= file= url= sum=
while IFS= read -r line || [[ -n $line ]]; do
	case $line in
	"- id: "*)
		[[ -n $id ]] && process "$id" "$file" "$url" "$sum"
		id=${line#- id: } file= url= sum=
		;;
	"  file: "*) file=${line#  file: } ;;
	"  url: "*) url=${line#  url: } ;;
	"  sha256:"*) sum=${line#  sha256:} sum=${sum# } ;;
	esac
done <"$manifest"
[[ -n $id ]] && process "$id" "$file" "$url" "$sum"

if ((${#missing[@]})); then
	echo
	echo "${#missing[@]} file(s) could not be downloaded. Download each one manually and save it as:"
	for entry in "${missing[@]}"; do
		echo
		echo "  $(pwd)/${entry%%$'\t'*}"
		echo "    ${entry#*$'\t'}"
	done
fi

exit $failed
