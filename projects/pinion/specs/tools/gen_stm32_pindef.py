#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Generate pinmap pindef files for the STM32 parts from ST's open pin data.

    gen_stm32_pindef.py          write ../pinout/stm32*.pindef.json

Stands in for pinmap's stm32 importer until that exists. Reads the XML files
that fetch.sh downloads into ../reference/st-pin-data/.
"""
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "reference" / "st-pin-data"
OUT = HERE.parent / "pinout"
NS = {"m": "http://dummy.com", "g": "http://mcd.rou.st.com/modules.php?name=mcu"}

PARTS = [
    # (mcu xml, gpio modes xml, device name, family, package, output stem)
    ("STM32H743VIHx.xml", "GPIO-STM32H747_gpio_v1_0_Modes.xml",
     "STM32H743VIH6", "stm32h7", "TFBGA100", "stm32h743vih6"),
    ("STM32F103C8Tx.xml", "GPIO-STM32F103x8_gpio_v1_0_Modes.xml",
     "STM32F103C8T6", "stm32f1", "LQFP48", "stm32f103c8t6"),
]

# Signal prefixes that contain an underscore and must stay in one piece.
PERIPH_PREFIXES = ("USB_OTG_FS", "USB_OTG_HS")
ANALOG_PERIPHS = re.compile(r"^(ADC\d*|DAC\d*|COMP\d*|OPAMP\d*)$")


def split_signal(signal):
    for prefix in PERIPH_PREFIXES:
        if signal.startswith(prefix + "_"):
            return prefix, signal[len(prefix) + 1:]
    periph, _, name = signal.partition("_")
    return (periph, name) if name else ("SYS", periph)


def pin_name(raw, kind="I/O"):
    """PA13 (JTMS/SWDIO), PC14-OSC32_IN and PC2_C all reduce to the port pin."""
    m = re.match(r"P[A-K]\d+", raw)
    return m.group(0) if m and kind == "I/O" else raw


def local(tag):
    return tag.rsplit("}", 1)[-1]


def load_modes(path):
    """(pin, signal) -> mux, from the GPIO modes file."""
    muxes = {}
    for pin in ET.parse(path).getroot().iter():
        if local(pin.tag) != "GPIO_Pin":
            continue
        name = pin_name(pin.get("Name"))
        for sig in pin:
            if local(sig.tag) != "PinSignal":
                continue
            mux = None
            for node in sig.iter():
                tag = local(node.tag)
                if tag == "PossibleValue" and node.text:
                    m = re.match(r"GPIO_AF(\d+)_", node.text)
                    if m:
                        mux = {"af": int(m.group(1))}
                elif tag == "RemapBlock" and mux is None:
                    m = re.search(r"REMAP(\d+)$", node.get("Name", ""))
                    if m:
                        mux = {"vendor": {"remap": int(m.group(1))}}
            if mux is not None:
                muxes[(name, sig.get("Name"))] = mux
    return muxes


def build(mcu_xml, modes_xml, device, family, package, stem):
    muxes = load_modes(SRC / modes_xml)
    root = ET.parse(SRC / mcu_xml).getroot()
    pins, pads, seen = {}, {}, {}
    for pin in root.findall("m:Pin", NS):
        raw, pad, kind = pin.get("Name"), pin.get("Position"), pin.get("Type")
        name = pin_name(raw, kind)
        seen[name] = seen.get(name, 0) + 1
    for pin in root.findall("m:Pin", NS):
        raw, pad, kind = pin.get("Name"), pin.get("Position"), pin.get("Type")
        name = pin_name(raw, kind)
        if seen[name] > 1:
            name = f"{name}_{pad}"  # several pads share one supply name
        entry = {}
        m = re.match(r"^P([A-K])(\d+)$", name)
        if m:
            entry["port"] = {"bank": m.group(1), "index": int(m.group(2))}
        functions = []
        for sig in pin.findall("m:Signal", NS):
            signal = sig.get("Name")
            if signal == "GPIO":
                continue
            periph, fn = split_signal(signal)
            mux = muxes.get((name, signal))
            if mux is None:
                mux = "analog" if ANALOG_PERIPHS.match(periph) else "fixed"
            functions.append({"periph": periph, "name": fn, "mux": mux})
        if functions:
            entry["functions"] = functions
        pins[name] = entry
        pads[name] = pad
    doc = {
        "schema": "pinmap/v1",
        "kind": "pindef",
        "meta": {"generated": True},
        "device": {"name": device, "vendor": "st", "family": family},
        "packages": {package: pads},
        "pins": pins,
    }
    out = OUT / f"{stem}.pindef.json"
    out.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"{out.name}: {len(pins)} pins, {len(set(pads.values()))} pads, "
          f"{sum(len(p.get('functions', [])) for p in pins.values())} functions")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for part in PARTS:
        build(*part)
