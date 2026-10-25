#!/usr/bin/env python3
"""Read selected Tips or rebuild a portable diagnostic snapshot; stdlib only."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys


REFERENCES = Path(__file__).resolve().parents[1] / "references"
FIELDS = ("id", "category", "title", "keyPoint", "body", "inDesign", "tradeOffs", "sources")


def validated_tips(value):
    if not isinstance(value, list) or not value:
        raise ValueError("tips must be a non-empty list")
    seen = set()
    for tip in value:
        if not isinstance(tip, dict):
            raise ValueError("each tip must be an object")
        for field in FIELDS[:6]:
            if not isinstance(tip.get(field), str) or not tip[field].strip():
                raise ValueError(f"tip {tip.get('id', '?')}: missing text field {field}")
        tip_id = tip["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", tip_id):
            raise ValueError(f"invalid tip ID: {tip_id}")
        if tip_id in seen:
            raise ValueError(f"duplicate tip ID: {tip_id}")
        seen.add(tip_id)
        for field, keys in (("tradeOffs", ("option", "gain", "cost")), ("sources", ("title", "url"))):
            entries = tip.get(field)
            if not isinstance(entries, list):
                raise ValueError(f"tip {tip_id}: {field} must be a list")
            for entry in entries:
                if not isinstance(entry, dict) or any(not isinstance(entry.get(k), str) for k in keys):
                    raise ValueError(f"tip {tip_id}: invalid {field} entry")
    return value


def load_snapshot():
    snapshot = json.loads((REFERENCES / "tips.json").read_text(encoding="utf-8"))
    validated_tips(snapshot.get("tips"))
    return snapshot


def table_text(value):
    return value.replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def refresh(source):
    source_bytes = source.read_bytes()
    catalog = json.loads(source_bytes)
    if not isinstance(catalog, dict):
        raise ValueError("catalog must be an object")
    tips = validated_tips(catalog.get("tips"))
    snapshot = {
        "provenance": {
            "source_project": "system-design-skill-developer",
            "source_file": source.name,
            "release_id": catalog.get("releaseId"),
            "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "imported_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "tip_count": len(tips),
            "note": "教材からの抽出。取り込み日は技術内容の再検証日ではない。",
        },
        "tips": [{field: tip[field] for field in FIELDS} for tip in tips],
    }
    metadata = snapshot["provenance"]
    lines = [
        "# Tip索引", "",
        f"元教材：`{metadata['source_project']}` / `{table_text(source.name)}`。"
        f"releaseId：`{table_text(str(metadata['release_id']))}`。{len(tips)}件。",
        f"取り込み時刻（UTC）：{metadata['imported_at_utc']}。", "",
        "原本のSHA-256：`" + metadata["source_sha256"] + "`。", "",
        "この索引は選択用。見出しを普遍的な要件として使わず、必要なIDの本文・条件・比較を読む。",
        "取り込み日は再レビュー日ではなく、出典の現在性や対象製品のバージョンを保証しない。",
        "同梱snapshotだけで利用でき、元リポジトリへの接続は不要。", "",
        "```sh",
        'python3 "<skill-dir>/scripts/tips.py" search 再試行',
        'python3 "<skill-dir>/scripts/tips.py" show timeout-budget retry-amplification',
        "```", "",
    ]
    groups = {}
    for tip in tips:
        groups.setdefault(tip["category"], []).append(tip)
    for category, entries in groups.items():
        lines.extend(["## " + table_text(category), "", "| ID | 話題 |", "| --- | --- |"])
        lines.extend(f"| `{tip['id']}` | {table_text(tip['title'])} |" for tip in entries)
        lines.append("")
    # Fully parse and validate the input before replacing either generated file.
    REFERENCES.mkdir(parents=True, exist_ok=True)
    (REFERENCES / "tips.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REFERENCES / "tip-index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Imported {len(tips)} Tips; source SHA-256: {metadata['source_sha256']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    show = commands.add_parser("show", help="Print complete diagnostic fields for selected IDs")
    show.add_argument("ids", nargs="+")
    search = commands.add_parser("search", help="Search diagnostic text; print only matching IDs and titles")
    search.add_argument("terms", nargs="+")
    refresh_command = commands.add_parser("refresh", help="Replace generated references from a local catalog")
    refresh_command.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "refresh":
            refresh(args.source)
            return 0
        snapshot = load_snapshot()
        if args.command == "show":
            by_id = {tip["id"]: tip for tip in snapshot["tips"]}
            missing = [tip_id for tip_id in args.ids if tip_id not in by_id]
            if missing:
                raise ValueError("unknown Tip IDs: " + ", ".join(missing))
            print(json.dumps({"provenance": snapshot["provenance"], "tips": [by_id[tip_id] for tip_id in args.ids]}, ensure_ascii=False, indent=2))
            return 0
        terms = [term.casefold() for term in args.terms]
        count = 0
        for tip in snapshot["tips"]:
            # Match all terms; exclude source URLs to avoid incidental domain matches.
            haystack = json.dumps({k: v for k, v in tip.items() if k != "sources"}, ensure_ascii=False).casefold()
            if all(term in haystack for term in terms):
                print(f"{tip['id']}\t{tip['category']}\t{tip['title']}")
                count += 1
        if not count:
            print("No matching Tips.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
