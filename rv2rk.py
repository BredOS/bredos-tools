#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import argparse

FASTBOOT_BIN = "/usr/bin/fastboot"
DEFAULT_FSBL = "/usr/share/rv2rk/FSBL.bin"
DEFAULT_UBOOT = "/usr/share/rv2rk/u-boot.itb"


def run_command(cmd, capture_output=False):
    try:
        result = subprocess.run(
            cmd, shell=True, text=True, capture_output=capture_output
        )
        return result
    except subprocess.CalledProcessError:
        print(f"Error running command: {cmd}")
        return None


def ensure_fastboot():
    if not os.path.exists(FASTBOOT_BIN):
        print(f"{FASTBOOT_BIN} not found. Attempting to install...")
        install_cmd = "sudo pacman -Sy && sudo pacman -S --noconfirm android-tools"
        run_command(install_cmd)

        if not os.path.exists(FASTBOOT_BIN):
            print(
                "Error: fastboot could not be installed. Please install 'android-tools' manually."
            )
            sys.exit(1)
        print("Installation successful.")


def flash_stage_2(uboot_path):
    print(f"Staging U-Boot: {uboot_path}")
    run_command(f"{FASTBOOT_BIN} stage {uboot_path}")

    print("Continuing boot...")
    run_command(f"{FASTBOOT_BIN} continue")

    print("Process completed successfully.")
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Flash RV2RK device using fastboot.")
    parser.add_argument(
        "-f",
        "--fsbl",
        default=DEFAULT_FSBL,
        help=f"Path to FSBL binary (default: {DEFAULT_FSBL})",
    )
    parser.add_argument(
        "-u",
        "--uboot",
        default=DEFAULT_UBOOT,
        help=f"Path to U-Boot image (default: {DEFAULT_UBOOT})",
    )
    args = parser.parse_args()

    ensure_fastboot()

    print("Checking device status...")
    dev_proc = run_command(f"{FASTBOOT_BIN} devices", capture_output=True)
    output = dev_proc.stdout if dev_proc else ""

    if "Android Fastboot" in output:
        print("Device already detected in Android Fastboot mode.")
        flash_stage_2(args.uboot)
    elif "dfu-device" in output:
        print("Device detected in DFU mode.")

        print(f"Staging FSBL: {args.fsbl}")
        run_command(f"{FASTBOOT_BIN} stage {args.fsbl}")

        print("Continuing boot...")
        run_command(f"{FASTBOOT_BIN} continue")

        print("Waiting for device to re-enumerate (10s timeout)...")
        start_time = time.time()

        while time.time() - start_time < 10:
            check_proc = run_command(f"{FASTBOOT_BIN} devices", capture_output=True)
            if check_proc and "Android Fastboot" in check_proc.stdout:
                print("Device detected in Android Fastboot mode.")
                flash_stage_2(args.uboot)

            time.sleep(0.5)

        print(
            "Timeout: Device did not appear in 'Android Fastboot' mode within 10 seconds."
        )
        sys.exit(1)

    else:
        print("No compatible device detected.")
        sys.exit(1)


if __name__ == "__main__":
    main()
