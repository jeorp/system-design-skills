#!/usr/bin/env python3
"""Copy the canonical Tips bundle into other skills for standalone installation."""

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "system-design-diagnosis"
FILES = ("scripts/tips.py", "references/tips.json", "references/tip-index.md")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report stale copies without writing")
    args = parser.parse_args()
    try:
        # Read all source files before changing any destination.
        bundle = {name: (SOURCE / name).read_bytes() for name in FILES}
        stale = []
        targets = sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md"))
        for target in targets:
            if target == SOURCE:
                continue
            for name, content in bundle.items():
                destination = target / name
                if destination.exists() and destination.read_bytes() == content:
                    continue
                stale.append(destination.relative_to(ROOT))
                if not args.check:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(content)
        if args.check and stale:
            for name in stale:
                print(f"Out of sync: {name}", file=sys.stderr)
            return 1
        print("Tips bundles are in sync." if args.check else f"Updated {len(stale)} bundled files.")
        return 0
    except OSError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
