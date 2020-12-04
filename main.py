"""
Helper for PDF conversion because Bash sucks.
"""

import argparse
import os
import pathlib
import subprocess


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("pwd")
    parser.add_argument("filepath")
    return parser.parse_args()


def absolutize(pwd, path):
    pwd = pathlib.Path(pwd)
    path = pathlib.Path(path)

    if path.is_absolute():
        return path
    return pwd / path


def convert(filepath):
    lo_path = pathlib.Path(os.environ["LIBREOFFICE"])
    lo_context_path = lo_path / "Contents" / "MacOS"

    args = [
        "./soffice",
        "--headless",
        "--convert-to",
        "pdf",
        filepath,
        "--outdir",
        filepath.parent,
    ]

    print(args)
    print("Exporting as PDF...")
    out = subprocess.check_output(args, cwd=lo_context_path)
    print("Done.")

    return out


def main():
    args = parse_args()
    filepath = absolutize(args.pwd, args.filepath)
    print(convert(filepath))


if __name__ == '__main__':
    main()
