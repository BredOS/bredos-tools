#!/usr/bin/env python3

import argparse
import subprocess
from pathlib import Path
import sys

CONFIG_PATH = Path.home() / ".config/sleepctl.conf"
SERVICE_NAME = "sleepctl.service"


def write_config(mode, processes):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        f.write(f"mode={mode}\n")
        if processes:
            f.write(f"processes={','.join(processes)}\n")


def read_status():
    subprocess.run(["systemctl", "--user", "status", SERVICE_NAME])


def systemctl_user(*args, capture=False):
    if capture:
        return subprocess.run(
            ["systemctl", "--user"] + list(args), capture_output=True, text=True
        )
    return subprocess.run(["systemctl", "--user"] + list(args))


def toggle_service():
    enabled = systemctl_user("is-enabled", SERVICE_NAME, capture=True)
    if "enabled" in enabled.stdout:
        systemctl_user("disable", "--now", SERVICE_NAME)
        return False
    else:
        systemctl_user("daemon-reexec")
        systemctl_user("enable", "--now", SERVICE_NAME)
        return True


def main():
    parser = argparse.ArgumentParser(description="Suspend inhibitor (user slice)")
    parser.add_argument(
        "-e",
        "--enable",
        action="store_true",
        help="Enable and start the inhibitor service",
    )
    parser.add_argument(
        "-d",
        "--disable",
        action="store_true",
        help="Stop and disable the inhibitor service",
    )
    parser.add_argument(
        "-s", "--status", action="store_true", help="Show systemd user service status"
    )
    parser.add_argument(
        "-t", "--toggle", action="store_true", help="Toggle the service state"
    )

    parser.add_argument(
        "-m",
        "--mode",
        nargs="+",
        metavar=("MODE", "PROCS"),
        help="Set mode: always | lid | processes proc1,proc2,...",
    )

    args = parser.parse_args()

    if args.status:
        read_status()
        return

    if args.toggle:
        print("Toggled " + ("on" if toggle_service() else "off") + ".")
        return

    if args.mode:
        if len(args.mode) == 1:
            mode = args.mode[0]
            processes = []
            if mode not in {"always", "lid"}:
                print(
                    "Error: '--mode processes' requires a process list.",
                    file=sys.stderr,
                )
                sys.exit(1)
        elif len(args.mode) == 2:
            mode, process_str = args.mode
            if mode != "processes":
                print(
                    f"Error: Unsupported mode '{mode}' with arguments.", file=sys.stderr
                )
                sys.exit(1)
            processes = [p.strip() for p in process_str.split(",") if p.strip()]
        else:
            print("Error: Too many arguments to --mode", file=sys.stderr)
            sys.exit(1)

        write_config(mode=mode, processes=processes)

    if args.enable:
        systemctl_user("daemon-reexec")
        systemctl_user("enable", "--now", SERVICE_NAME)
        print("Enabled.")

    if args.disable:
        systemctl_user("disable", "--now", SERVICE_NAME)
        print("Disabled.")

    if not (args.mode or args.enable or args.disable or args.status):
        parser.print_help()


if __name__ == "__main__":
    main()
