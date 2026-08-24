# typed: false
# frozen_string_literal: true

# Homebrew Formula for Designly
# Commercial Art Direction & Design Neural Mesh Plugin CLI
class Designly < Formula
  desc "Commercial Art Direction & Design Neural Mesh with 21 modular skills & 8 model adapters"
  homepage "https://github.com/imMamdouhaboammar/designly"
  url "https://github.com/imMamdouhaboammar/designly/archive/refs/tags/v5.0.2.tar.gz"
  sha256 "ea49bf1b39493bace44d2884fc71e1aa4a53b2537313a185ca38a2939a10f302"
  license "MIT"
  head "https://github.com/imMamdouhaboammar/designly.git", branch: "main"

  depends_on "python@3.12" => :recommended
  depends_on "node" => :optional

  def install
    # Install all core libraries and skills into libexec
    libexec.install Dir["*"]

    # Generate executable wrapper script in bin
    (bin/"designly").write <<~EOS
      #!/usr/bin/env bash
      exec "#{Formula["python@3.12"].opt_bin}/python3" "#{libexec}/skills/prompt-compiler/scripts/compile_prompt.py" "$@"
    EOS
    chmod 0755, bin/"designly"
  end

  test do
    output = shell_output("#{bin}/designly --list-models")
    assert_match "gemini-nano-banana", output
    assert_match "kling", output
    assert_match "seedance", output
  end
end
