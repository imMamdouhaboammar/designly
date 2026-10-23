"""Development dependencies must never become part of the public plugin artifact."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
VALIDATOR = REPO / "tools" / "validate_public_plugin.py"
PACKAGER = REPO / "tools" / "package_plugin.py"


class PluginPackageExclusionTests(unittest.TestCase):
    def test_packager_excludes_node_modules(self):
        with tempfile.TemporaryDirectory(prefix="designly-package-test-") as directory:
            root = Path(directory)
            (root / "node_modules" / "example").mkdir(parents=True)
            (root / "node_modules" / "example" / "package.json").write_text("{}")
            (root / "sample.txt").write_text("public content")
            output = root.parent / (root.name + ".zip")
            try:
                subprocess.run(
                    [sys.executable, str(PACKAGER), str(root), str(output)],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                with zipfile.ZipFile(output) as archive:
                    self.assertIn("sample.txt", archive.namelist())
                    self.assertFalse(any(name.startswith("node_modules/") for name in archive.namelist()))
            finally:
                output.unlink(missing_ok=True)

    def test_validator_ignores_dependencies_but_still_inspects_project_files(self):
        spec = importlib.util.spec_from_file_location("designly_validator", VALIDATOR)
        assert spec and spec.loader
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory(prefix="designly-validator-test-") as directory:
            root = Path(directory)
            (root / "node_modules" / ".bin").mkdir(parents=True)
            (root / "skills").mkdir()
            (root / "node_modules" / ".bin" / "tsc").symlink_to(root / "missing")
            (root / "skills" / "malicious-link").symlink_to(root / "missing")
            inventory = {path.relative_to(root).as_posix() for path in validator.plugin_files(root)}
            self.assertIn("skills/malicious-link", inventory)
            self.assertNotIn("node_modules/.bin/tsc", inventory)


if __name__ == "__main__":
    unittest.main()
