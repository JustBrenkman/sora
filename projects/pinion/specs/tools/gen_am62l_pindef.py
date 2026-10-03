#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Generate the AM62L pinmap pindef from the datasheet (SPRSPA1).

    gen_am62l_pindef.py          write ../pinout/am62l32.pindef.json and
                                 ../notes/am62l-io-domains.md

Stands in for a pinmap importer. Reads Table 5-1 (Pin Attributes, ANB package)
from `pdftotext -layout` output of ../reference/ti/am62l-datasheet.pdf, takes
the supply balls from Table 5-46, and cross-checks every signal against the
ball lists of the Signal Descriptions tables (section 5.3). Exits non-zero if
the two disagree or the ball count is not 373.
"""
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PDF = HERE.parent / "reference" / "ti" / "am62l-datasheet.pdf"
OUT = HERE.parent / "pinout" / "am62l32.pindef.json"
DOMAINS = HERE.parent / "notes" / "am62l-io-domains.md"
BALLS = 373

BALL = r"\bA?[A-HJ-NPRT-WY](?:1\d|2[0-3]|[1-9])\b"
TYPES = r"IOZ|IOD|IO|OZ|OD|I|O|A|CAP|PWR|GND|N/A"
MUX_ROW = re.compile(rf"(\S+)\s+(\d{{1,2}}|Bootstrap)\s+({TYPES})\b")
FIXED_ROW = re.compile(rf"^\s+({BALL})\s+(\S+)\s+(\S+)\s+({TYPES})\b")
BALL_ROW = re.compile(rf"^\s{{1,8}}({BALL})\s+(\S.*)$")
VOLTAGE = re.compile(r"(\d\.\dV(?: / \d\.\dV)?)\s+(VDD\S+)")
PADCONFIG = re.compile(r"(0x[0-9A-Fa-f]{8})")
BALL_LIST = re.compile(rf"((?:{BALL},\s*)*{BALL},?)\s*$")
DESC_ROW = re.compile(rf"^ (\S+)(?: \(\d+\))*\s{{2,}}({TYPES})\s{{2,}}")


def text():
    return subprocess.run(["pdftotext", "-layout", str(PDF), "-"], check=True,
                          capture_output=True, text=True).stdout.splitlines()


def section(lines, start, end):
    a = next(i for i, l in enumerate(lines) if l.strip() == start and i > 300)
    b = next(i for i, l in enumerate(lines) if l.strip() == end and i > a)
    return lines[a:b]


def split_signal(signal):
    """UART0_RXD -> (UART0, RXD); WKUP_UART0_RXD -> (WKUP_UART0, RXD)."""
    tokens = signal.split("_")
    if len(tokens) == 1:
        return "SYS", signal
    for i, tok in enumerate(tokens[:-1]):
        if tok[-1].isdigit():
            return "_".join(tokens[:i + 1]), "_".join(tokens[i + 1:])
    return tokens[0], "_".join(tokens[1:])


def parse_attributes(lines):
    """Table 5-1 -> {ball: {name, signals: [(signal, mux, type)], volt, supply, addr}}."""
    balls = {}
    groups, ball_rows = [], []
    for n, line in enumerate(lines):
        if "Table 5-1" in line or "PADCONFIG Register" in line:
            continue
        m = FIXED_ROW.match(line)
        if m and not MUX_ROW.search(line):
            v = VOLTAGE.search(line)
            balls[m.group(1)] = {
                "name": m.group(2), "signals": [(m.group(3), None, m.group(4))],
                "volt": v.group(1) if v else "", "supply": v.group(2) if v else "",
                "addr": ""}
            continue
        m = MUX_ROW.search(line)
        if m:
            signal, mode, kind = m.groups()
            mode = None if mode == "Bootstrap" else int(mode)
            last = groups[-1] if groups else None
            new = (last is None or last["closed"] or
                   (mode is not None and mode <= last["mode"]))
            if new:
                groups.append({"first": n, "last": n, "signals": [],
                               "mode": -1, "closed": False})
            g = groups[-1]
            g["signals"].append((signal, mode, kind))
            g["last"] = n
            if mode is None:
                g["closed"] = True
            else:
                g["mode"] = mode
        b = BALL_ROW.match(line)
        if b and "PADCONFIG" in line:
            ball_rows.append((n, b.group(1), line))
    names = {}
    for n, line in enumerate(lines):
        # The ball name sits in the second column, one to three lines above "PADCONFIG:".
        m = re.match(r"^\s{8,14}([A-Z][A-Za-z0-9_]+)\b", line)
        if m and not m.group(1).startswith("PADCONFIG"):
            names[n] = m.group(1)
    for n, ball, line in ball_rows:
        group = next((g for g in groups if g["first"] - 1 <= n <= g["last"] + 1), None)
        if group is None:
            sys.exit(f"no signal group for ball {ball} (line {n})")
        v = VOLTAGE.search(line)
        addr = ""
        for k in range(n, min(n + 4, len(lines))):
            a = PADCONFIG.search(lines[k])
            if a:
                addr = a.group(1)
                break
        balls[ball] = {
            "name": group["signals"][0][0] if group["signals"][0][1] == 0 else None,
            "signals": group["signals"],
            "volt": v.group(1) if v else "", "supply": v.group(2) if v else "",
            "addr": addr}
        group["ball"] = ball
    orphans = [g for g in groups if "ball" not in g]
    if orphans:
        sys.exit(f"{len(orphans)} signal group(s) without a ball, first: {orphans[0]['signals']}")
    for ball, info in balls.items():
        if info["name"] is None:
            sys.exit(f"ball {ball} has no MUXMODE 0 signal: {info['signals']}")
    return balls


def parse_descriptions(lines):
    """Section 5.3 -> {signal: {balls}}. Ball lists may wrap above and below the row."""
    result = defaultdict(set)
    run, anchor = [], None

    def flush():
        nonlocal run, anchor
        if run and anchor:
            result[anchor].update(run)
        run, anchor = [], None

    open_list = False
    for line in lines:
        if "Signal Descriptions" in line or "SIGNAL NAME" in line:
            flush()
            open_list = False
            continue
        name = DESC_ROW.match(line)
        tail = BALL_LIST.search(line)
        found = re.findall(BALL, tail.group(1)) if tail else []
        if name and not open_list and not (run and anchor is None):
            flush()
        if name:
            anchor = name.group(1)
        if found:
            run += found
            open_list = tail.group(1).rstrip().endswith(",")
            if not open_list and anchor:
                flush()
    flush()
    return result


def main():
    lines = text()
    attrs = parse_attributes(section(lines, "5.2 Pin Attributes", "5.3 Signal Descriptions"))
    desc = parse_descriptions(section(lines, "5.3 Signal Descriptions",
                                      "5.4 Pin Connectivity Requirements"))

    # Supplies, ground and reserved balls: one pin per ball, from section 5.3.
    for signal, pads in desc.items():
        for pad in pads:
            if pad not in attrs:
                attrs[pad] = {"name": signal, "signals": [(signal, None, "PWR")],
                              "volt": "", "supply": "", "addr": ""}

    errors = []
    by_signal = defaultdict(set)
    for pad, info in attrs.items():
        for signal, _, _ in info["signals"]:
            by_signal[signal].add(pad)
    for signal, pads in desc.items():
        if by_signal.get(signal) != pads:
            errors.append(f"{signal}: Table 5-1 {sorted(by_signal.get(signal, []))} "
                          f"vs section 5.3 {sorted(pads)}")
    if len(attrs) != BALLS:
        errors.append(f"{len(attrs)} balls, expected {BALLS}")
    if errors:
        sys.exit("\n".join(errors))

    count = defaultdict(int)
    for info in attrs.values():
        count[info["name"]] += 1
    pins, pads_map = {}, {}
    for pad in sorted(attrs, key=lambda b: (len(re.match(r"[A-Z]+", b).group()), b[:-1 if b[-2].isalpha() else -2], int(re.search(r"\d+", b).group()))):
        info = attrs[pad]
        key = info["name"] if count[info["name"]] == 1 else f"{info['name']}_{pad}"
        functions = []
        for signal, mode, kind in info["signals"]:
            if kind in ("PWR", "GND", "CAP", "N/A"):
                continue
            periph, fn = split_signal(signal)
            if mode is not None:
                mux = {"vendor": {"muxmode": mode}}
            else:
                mux = "analog" if kind == "A" else "fixed"
            functions.append({"periph": periph, "name": fn, "mux": mux})
        pins[key] = {"functions": functions} if functions else {}
        pads_map[key] = pad
        info["key"] = key

    doc = {
        "schema": "pinmap/v1", "kind": "pindef", "meta": {"generated": True},
        "device": {"name": "AM62L32", "vendor": "ti", "family": "am62l"},
        "packages": {"ANB": pads_map},
        "pins": pins,
    }
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"{OUT.name}: {len(pins)} pins, "
          f"{sum(len(p.get('functions', [])) for p in pins.values())} functions")

    groups = defaultdict(list)
    for pad, info in attrs.items():
        if info["supply"]:
            groups[(info["supply"], info["volt"])].append(info)
    out = ["<!-- SPDX-License-Identifier: CC-BY-4.0 -->",
           "# AM62L I/O supply groups", "",
           "Generated by `specs/tools/gen_am62l_pindef.py` from Table 5-1 of the AM62L",
           "datasheet. pinmap has no field for a ball's I/O supply, so it is kept here.",
           "A pin's I/O voltage is the voltage of the supply rail listed for its group.", ""]
    for (supply, volt), infos in sorted(groups.items()):
        out += [f"## {supply} ({volt})", "", "| Ball | Pin | PADCONFIG |", "|---|---|---|"]
        for info in sorted(infos, key=lambda i: i["key"]):
            out.append(f"| {pads_map[info['key']]} | {info['key']} | {info['addr']} |")
        out.append("")
    DOMAINS.parent.mkdir(exist_ok=True)
    DOMAINS.write_text("\n".join(out))
    print(f"{DOMAINS.name}: {len(groups)} supply groups")


if __name__ == "__main__":
    main()
