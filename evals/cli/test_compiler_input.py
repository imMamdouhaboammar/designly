"""Regression tests for the compiler's documented input channels."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "skills/prompt-compiler/scripts/compile_prompt.py"


class CompilerInputTests(unittest.TestCase):
    def run_compiler(self, *args: str, input_text: str | None = None):
        return subprocess.run(
            [sys.executable, str(COMPILER), "-m", "gemini-nano-banana", "-f", "json", *args],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=15,
            check=False,
        )

    def assert_subject(self, result: subprocess.CompletedProcess, subject: str):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(subject, result.stdout)

    def test_long_inline_json_is_not_interpreted_as_a_file_path(self):
        subject = "precision watch " + "x" * 8000
        result = self.run_compiler("-i", json.dumps({"subject": subject}))
        self.assert_subject(result, subject)

    def test_explicit_json_file_path_still_works(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "creative-brief.json"
            path.write_text(json.dumps({"subject": "A cobalt blue concept car"}), encoding="utf-8")
            self.assert_subject(self.run_compiler("-i", str(path)), "A cobalt blue concept car")

    def test_piped_json_is_processed(self):
        self.assert_subject(
            self.run_compiler(input_text=json.dumps({"subject": "A red silk umbrella"})),
            "A red silk umbrella",
        )

    def test_plain_text_input_preserves_existing_subject_fallback(self):
        self.assert_subject(self.run_compiler("-i", "A coastal perfume campaign"), "A coastal perfume campaign")


if __name__ == "__main__":
    unittest.main()
