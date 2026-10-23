"""Fixture-based guard against accidental publication of private artifacts."""

import json
import unittest
from pathlib import Path

from test_supply_chain import validate_package_files


PACKAGE_JSON = Path(__file__).resolve().parents[2] / "package.json"


class PackageWhitelistTests(unittest.TestCase):
    def test_repository_whitelist_is_exact_and_granular(self):
        data = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))
        self.assertEqual(validate_package_files(data.get("files")), [])

    def test_rejects_broad_dist_and_private_paths(self):
        valid = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))["files"]
        for unsafe in ("dist", "evals", ".planning", ".env", "./secrets", "../private"):
            with self.subTest(unsafe=unsafe):
                self.assertTrue(validate_package_files([*valid, unsafe]))

    def test_rejects_missing_entry_or_duplicate(self):
        valid = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))["files"]
        self.assertTrue(validate_package_files([path for path in valid if path != "dist/index.js"]))
        self.assertTrue(validate_package_files([*valid, "skills"]))


if __name__ == "__main__":
    unittest.main()
