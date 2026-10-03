#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Check the nets that join pinion's three processors.

    check_nets.py        exit 0 if every inter-chip net is consistent

`pinmap check` validates each pinasg against its own pindef. This script adds
the checks that span chips: a net shared by two processors must pair
compatible signals (TX with RX, RTS with CTS, DP with DP), and an AM62L pin
wired to an STM32 must sit in a 3.3 V I/O supply group.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

PINOUT = Path(__file__).resolve().parent.parent / "pinout"
DOMAINS = PINOUT.parent / "notes" / "am62l-io-domains.md"
PROJECTS = {"fmu": "fmu.pinasg.ron", "io": "io.pinasg.ron", "soc": "soc.pinasg.ron"}
SUPPLY_NETS = re.compile(r"^(GND|.*VDD.*|VPP.*|.*_CAP_.*|.*VCAP.*|.*VBAT)$")
# Signal names that may share a net, after stripping a trailing "D" or "n".
PAIRS = [{"TX", "RX"}, {"RTS", "CTS"}, {"DP"}, {"DM"}]
# Nets every build must carry on both sides: (net, chip, chip).
REQUIRED = [
    ("FMU_USART6_TX_TO_IO", "fmu", "io"), ("FMU_USART6_RX_FROM_IO", "fmu", "io"),
    ("FMU_UART5_TX_SOC", "fmu", "soc"), ("FMU_UART5_RX_SOC", "fmu", "soc"),
    ("FMU_UART5_RTS_SOC", "fmu", "soc"), ("FMU_UART5_CTS_SOC", "fmu", "soc"),
    ("FMU_USB_DP", "fmu", "soc"), ("FMU_USB_DM", "fmu", "soc"),
]


def table(project):
    out = subprocess.run(["pinmap", "emit", "--to", "json", "--project", project],
                         cwd=PINOUT, check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def soc_supplies():
    """pin -> I/O supply group, and supply group -> rail net, for the AM62L."""
    group, supply = {}, None
    for line in DOMAINS.read_text().splitlines():
        m = re.match(r"## (\S+)", line)
        if m:
            supply = m.group(1)
        m = re.match(r"\| \S+ \| (\S+) \|", line)
        if m and supply and m.group(1) != "Pin":
            group[m.group(1)] = supply
    return group


def role(function):
    name = function.rsplit(".", 1)[-1]
    return re.sub(r"(D|n)$", "", name) if re.search(r"(TXD|RXD|RTSn|CTSn)$", name) else name


def main():
    rows = {chip: table(project) for chip, project in PROJECTS.items()}
    nets = {}
    for chip, pins in rows.items():
        for row in pins:
            if row.get("net") and not SUPPLY_NETS.match(row["net"]):
                nets.setdefault(row["net"], []).append((chip, row))
    group = soc_supplies()
    rail = {}
    for row in rows["soc"]:
        base = re.sub(r"_A?[A-Y]\d+$", "", row["pin"])
        if row.get("net") and base.startswith(("VDDS", "VDDA")):
            rail[base] = row["net"]

    errors = []
    for net, chip_a, chip_b in REQUIRED:
        chips = {chip for chip, _ in nets.get(net, [])}
        if chips != {chip_a, chip_b}:
            errors.append(f"{net}: expected on {chip_a} and {chip_b}, found on {sorted(chips) or 'nothing'}")
    shared = {n: uses for n, uses in nets.items() if len({c for c, _ in uses}) > 1}
    for net, uses in sorted(shared.items()):
        roles = {role(row["function"]) for _, row in uses}
        if not any(roles == pair for pair in PAIRS):
            errors.append(f"{net}: incompatible signals {sorted(row['function'] for _, row in uses)}")
        for chip, row in uses:
            if chip == "soc" and row["pin"] in group:
                net_of_rail = rail.get(group[row["pin"]], "?")
                if "3V3" not in net_of_rail:
                    errors.append(f"{net}: {row['pin']} is powered from {group[row['pin']]} "
                                  f"({net_of_rail}) but connects to a 3.3 V STM32 pin")
        print(f"ok    {net}: " + ", ".join(f"{c}:{r['pin']} {r['function']}" for c, r in uses))
    for error in errors:
        print(f"FAIL  {error}")
    print(f"{len(shared)} inter-chip nets, {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
