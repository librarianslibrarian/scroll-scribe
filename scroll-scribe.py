#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import sys

def ensure_dep(name: str) -> None:
    """
    Check that a required command-line program is available in the PATH.

    If it is missing, print an error message and exit the script.
    """
    if shutil.which(name) is None:
        print(f"[ERROR] Required dependency not found in PATH: {name}")
        print("Hint: install it first. For example, on macOS with Homebrew:")
        print(f"  brew install {name}")
        sys.exit(1)


def main() -> None:
    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        description=(
            "Force OCR on every page of a PDF to create a fully searchable PDF. "
        )
    )
    parser.add_argument(
        "input_pdf",
        help="Path to the source PDF (non-searchable or partially searchable).",
    )
    parser.add_argument(
        "output_pdf",
        help="Path to the output searchable PDF that will be created.",
    )
    parser.add_argument(
        "--lang",
        default="eng",
        help="Tesseract language(s), e.g. 'eng' or 'eng+deu'. Default: eng",
    )
    parser.add_argument(
        "--dpi",
        default="300",
        help="Rasterization DPI for OCR. Higher = better text, bigger file. Default: 300",
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=0,
        help=(
            "Number of parallel jobs (CPU cores) for ocrmypdf to use. "
            "Default 0 means 'let ocrmypdf decide', but we set 1 by default below "
            "for stability. Try 4 or 8 on a multi-core machine."
        ),
    )
    args = parser.parse_args()

    # Make sure the required tools are installed
    for dep in ("ocrmypdf", "tesseract", "gs"):
        ensure_dep(dep)

    # Build the ocrmypdf command.
    #
    # Key flags:
    #   --force-ocr
    #       OCR every page, even if it looks like it already has text.
    #   --rotate-pages / --deskew
    #       Try to straighten/rotate pages automatically.
    #   --clean-final
    #       Clean up the images to reduce background noise.
    #   --pdf-renderer sandwich
    #       Keep the original page image, but overlay an invisible text layer.
    cmd = [
        "ocrmypdf",
        "--force-ocr",
        "--rotate-pages",
        "--deskew",
        "--clean-final",
        "--optimize", "1",
        "--output-type", "pdf",
        "--tesseract-timeout", "0",
        "--tesseract-pagesegmode", "1",  # '1' = automatic page segmentation with OSD
        "--language", args.lang,
        "--jobs", str(args.jobs) if args.jobs else "1",
        "--pdf-renderer", "sandwich",
        "--image-dpi", args.dpi,
        args.input_pdf,
        args.output_pdf,
    ]

    print("[INFO] Running:", " ".join(cmd))
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] OCR failed with exit code {e.returncode}")
        sys.exit(e.returncode)

    if os.path.exists(args.output_pdf):
        print(f"[OK] Wrote searchable PDF → {args.output_pdf}")
    else:
        print("[ERROR] Output PDF not created.")
        sys.exit(1)


if __name__ == "__main__":
    main()