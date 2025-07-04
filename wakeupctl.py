#!/usr/bin/env python3

import sys
import subprocess
import time
from pathlib import Path


class colors:
    endc = "\033[0m"
    red_t = "\033[31m"
    green_t = "\033[32m"


def find_power_wakeups() -> list:
    power_paths = list(Path("/sys").rglob("power/wakeup"))
    results = []
    for path in power_paths:
        try:
            state = path.read_text().strip()
            device = path.parent
            name = device.name
            if (device / "uevent").exists():
                for line in (device / "uevent").read_text().splitlines():
                    if line.startswith("PRODUCT=") or line.startswith("PCI_ID="):
                        name += f" ({line})"
                        break
            results.append((str(device), state))
        except Exception:
            continue
    return results


def find_acpi_wakeups() -> list:
    acpi_file = Path("/proc/acpi/wakeup")
    entries = []
    if not acpi_file.exists():
        return entries
    for line in acpi_file.read_text().splitlines():
        if line and not line.startswith("Device"):
            parts = line.split()
            if len(parts) >= 4:
                device, state = parts[0], parts[3]
                entries.append((device, state.strip()))
    return entries


def find_rtc_wakeups() -> list:
    rtc_path = Path("/proc/driver/rtc")
    if not rtc_path.exists():
        return []
    lines = rtc_path.read_text().splitlines()
    alarm_irq = next((l for l in lines if l.startswith("alarm_IRQ")), None)
    return [
        ("rtc", "enabled" if alarm_irq and alarm_irq.endswith("yes") else "disabled")
    ]


def find_wol_wakeups() -> list:
    results = []
    try:
        links = Path("/sys/class/net").iterdir()
        for link in links:
            if not (link / "device").exists():
                continue
            try:
                out = subprocess.check_output(
                    ["ethtool", link.name], stderr=subprocess.DEVNULL
                ).decode()
                for line in out.splitlines():
                    if "Wake-on" in line:
                        state = line.split(":")[-1].strip()
                        if state != "d":
                            results.append((f"{link.name} (wol)", "enabled"))
                        else:
                            results.append((f"{link.name} (wol)", "disabled"))
                        break
            except Exception:
                continue
    except Exception:
        pass
    return results


def pf(name: str, state: str, space: int) -> None:
    if name.endswith("/power"):
        name = name[:-6]
    print(
        name
        + (" " * (space - len(name)))
        + " -> "
        + (colors.green_t if state == "enabled" else colors.red_t)
        + state
        + colors.endc
    )


def get_wakeups() -> list:
    wakeups = find_power_wakeups()
    acpi = find_acpi_wakeups()
    rtc = find_rtc_wakeups()
    wol = find_wol_wakeups()

    return wakeups + acpi + rtc + wol


def list_wakeups() -> None:
    wakeups = find_power_wakeups()
    acpi = find_acpi_wakeups()
    rtc = find_rtc_wakeups()
    wol = find_wol_wakeups()

    maxl = max([len(str(d)) for d, _ in wakeups + acpi + rtc + wol] + [5])

    print("== Kernel wakeup-capable devices (power/wakeup):")
    for dev, state in sorted(wakeups, key=lambda x: str(x[0])):
        pf(dev, state, maxl)

    if acpi:
        print("\n== ACPI wake sources:")
        for dev, state in acpi:
            pf(dev, state, maxl)

    if rtc:
        print("\n== RTC wake sources:")
        for name, state in rtc:
            pf(name, state, maxl)

    if wol:
        print("\n== Wake-on-LAN capable interfaces:")
        for name, state in wol:
            pf(name, state, maxl)


def set_wakeup(targets: list, state: str) -> None:
    for target in targets:
        target = target.lower()
        matches = set()

        wakeups = get_wakeups()

        for name, _ in wakeups:
            if target in name:
                matches.add(name)

        if not matches:
            print(f"No device matched '{target}'")
        else:
            for name in matches:
                try:
                    with open(f"{name}/wakeup", "w") as f:
                        f.write(state)
                    print(f"{name}: set to {state}")
                except Exception as e:
                    print(f"{name}: failed to set -> {e}")


def get_active_counts() -> dict:
    results = {}
    wakeups = get_wakeups()

    for name, state in wakeups:
        if state == "enabled":
            event_file = f"{name}/wakeup_active_count"
            if not Path(event_file).exists():
                continue
            try:
                with open(event_file) as f:
                    count = int(f.read().strip())
                    results[name] = count
            except Exception:
                continue
    return results


def monitor_wakeups(disable: False) -> None:
    print("== Monitoring enabled wakeup event counts.\n== Ctrl+C to exit.\n")
    prev = get_active_counts()
    try:
        while True:
            time.sleep(0.2)
            now = get_active_counts()
            for key in now:
                if key in prev and now[key] != prev[key]:
                    print(f"{key}: {prev[key]} -> {now[key]}")
                    if disable:
                        set_wakeup(key, "disabled")
            prev = now
    except KeyboardInterrupt:
        print("\r\033[K\n" + ("-" * 8) + "\nMonitoring finished")


def main() -> None:
    args = sys.argv[1:]
    print("BredOS Wakeup device trigger handler\n" + (36 * "-") + "\n")
    if not args:
        list_wakeups()
        print("\n" + ("-" * 13) + "\nEND OF REPORT")
    elif args[0] in ["-m", "--monitor"]:
        monitor_wakeups((len(args) - 1) and (args[1] in ["-a", "--autodisable"]))
    elif args[0] in ["-d", "--disable"]:
        if not len(args) - 1:
            print("No devices specified!")
        else:
            set_wakeup(args[2:], "disabled")
    elif args[0] in ["-e", "--enable"]:
        if not len(args) - 1:
            print("No devices specified!")
        else:
            set_wakeup(args[2:], "enabled")
    else:
        print(
            "Usage:\n  bredos-wakeupctl"
            + (" " * 15)
            + "# List all wake sources\n  bredos-wakeupctl usb enabled"
            + "   # Set USB-related wakeups to enabled\n  bredos-wakeupctl --monitor"
            + "          # Monitor active wakeups"
        )


if __name__ == "__main__":
    main()
