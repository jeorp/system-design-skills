"""Exercise the bundle sync CLI against isolated repositories."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_tips.py"
BUNDLE = ("scripts/tips.py", "references/tips.json", "references/tip-index.md")


class SyncTipsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.script = self.root / "scripts" / "sync_tips.py"
        self.script.parent.mkdir()
        shutil.copyfile(SCRIPT, self.script)
        self.source = self.add_skill("system-design-diagnosis")
        for name in BUNDLE:
            path = self.source / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(f"canonical {name}\n".encode())

    def add_skill(self, name):
        skill = self.root / "skills" / name
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")
        return skill

    def run_sync(self, *args):
        return subprocess.run(
            [sys.executable, str(self.script), *args],
            capture_output=True, text=True, cwd=self.root,
        )

    def test_discovers_new_skills_and_ignores_other_directories(self):
        target = self.add_skill("new-domain")
        unrelated = self.root / "skills" / "not-a-skill"
        unrelated.mkdir()
        result = self.run_sync()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in BUNDLE:
            self.assertEqual((target / name).read_bytes(), (self.source / name).read_bytes())
        self.assertEqual(list(unrelated.iterdir()), [])
        self.assertEqual(self.run_sync("--check").returncode, 0)
        self.assertIn("Updated 0 bundled files", self.run_sync().stdout)

    def test_check_reports_missing_files_without_writing(self):
        target = self.add_skill("new-domain")
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob("*") if path.is_file()}
        result = self.run_sync("--check")
        self.assertEqual(result.returncode, 1)
        for name in BUNDLE:
            self.assertIn(str((target / name).relative_to(self.root)), result.stderr)
        after = {path.relative_to(self.root): path.read_bytes()
                 for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)

    def test_stale_copy_is_detected_and_repaired(self):
        target = self.add_skill("new-domain")
        self.assertEqual(self.run_sync().returncode, 0)
        stale = target / "references/tips.json"
        stale.write_bytes(b"outdated\n")
        self.assertEqual(self.run_sync("--check").returncode, 1)
        self.assertEqual(stale.read_bytes(), b"outdated\n")
        self.assertEqual(self.run_sync().returncode, 0)
        self.assertEqual(stale.read_bytes(), (self.source / "references/tips.json").read_bytes())

    def test_missing_source_leaves_destinations_untouched(self):
        target = self.add_skill("new-domain")
        (self.source / BUNDLE[-1]).unlink()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn("Error:", result.stderr)
        self.assertEqual([path.name for path in target.iterdir()], ["SKILL.md"])


if __name__ == "__main__":
    unittest.main()
