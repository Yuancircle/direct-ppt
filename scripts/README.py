#!/usr/bin/env python3
"""Direct PPT skill helper.

This file stays lightweight on purpose. The actual runtime loading logic
lives in scripts/pptx-runtime.js so the skill can fall back to bundled
offline dependencies when the host does not have pptxgenjs installed.
"""

from pathlib import Path


def main():
    runtime_dir = Path(__file__).resolve().parent / "runtime"
    print("direct-ppt skill scaffold is ready")
    print(f"Bundled runtime directory: {runtime_dir}")
    print("Use scripts/pptx-runtime.js to load pptxgenjs with offline fallback.")


if __name__ == "__main__":
    main()
