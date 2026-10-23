"""Verify the actual npm archive matches Designly's declared entry points."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class PackedPackageContractTests(unittest.TestCase):
    def test_all_declared_entry_points_ship_in_npm_archive(self):
        manifest = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as cache:
            result = subprocess.run(
                ["npm", "pack", "--dry-run", "--json", "--ignore-scripts", "--cache", cache],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=45,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            files = {entry["path"] for entry in json.loads(result.stdout)[0]["files"]}

        expected = {
            manifest["main"].removeprefix("./"),
            manifest["types"].removeprefix("./"),
            *(entry.removeprefix("./") for entry in manifest["bin"].values()),
        }
        self.assertTrue(expected.issubset(files), f"Missing publish artifacts: {expected - files}")
        self.assertFalse(any(name.startswith(("evals/", "tests/", ".git/")) for name in files))


if __name__ == "__main__":
    unittest.main()
