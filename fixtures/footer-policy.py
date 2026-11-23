#!/usr/bin/env python3
"""Check Chronicle's footer policy through Base's neutral reading fixture.

Chronicle's product listing selects the compact colophon footer, where Base's
default listing keeps the quiet footer. This fixture renders Base's neutral reading
workspace through Chronicle with that expectation, so every other reading check
runs unchanged. No preview server, publication or configured output is involved.
"""
import argparse
import os
from pathlib import Path
import subprocess
import sys

THEME = Path(__file__).resolve().parents[1]
# The landing patterns whose footer this world's templates change.
FOOTERS = {"product-listing": "colophon"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gazette", required=True, help="Exact built Gazette executable")
    parser.add_argument("--resource-bindings", type=Path, required=True, help="JSON bindings for this world's external resource inputs")
    parser.add_argument("--base", type=Path, default=THEME.parent / "gazette-theme-base", help="Base checkout; defaults to the sibling directory")
    parser.add_argument("--keep", action="store_true", help="Retain the temporary workspace for browser inspection")
    args = parser.parse_args()
    command = [sys.executable, str(args.base.resolve(strict=True) / "fixtures" / "reading.py"), "--gazette", args.gazette,
               "--theme", str(THEME), "--resource-bindings", str(args.resource_bindings)]
    for pattern, treatment in FOOTERS.items():
        command += ["--footer-treatment", f"{pattern}={treatment}"]
    if args.keep:
        command.append("--keep")
    # Base's fixture is captured as a Theme source, so it must stay free of bytecode.
    return subprocess.run(command, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1")).returncode


if __name__ == "__main__":
    sys.exit(main())
