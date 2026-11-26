#!/usr/bin/env python3
"""news-image-20261126 entry: copy the artwork to /output/entry.png.

The artwork is entry.png beside this file: a one-page newspaper front
page summing up Thursday 26 November 2026 in six stories (the US
proposes new tariffs on 14 trading partners, highest on China; Kim
Jong Un orders wider deployment of tactical nuclear weapons; the
Houthis claim a strike on Saudi Arabia's Ras Tanura refinery; the
first Pakistani astronaut reaches China's Tiangong station aboard
Shenzhou-24; a fuel tanker crash near Cairo kills at least 30; and
15-year-old Vaibhav Sooryavanshi smashes the fastest List A double
century, 204 off 53 balls).
Standard library only, no network, deterministic: the same bytes are
written on every run.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The gate reads exactly the bytes written: refuse a partial copy.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy incomplete")


if __name__ == "__main__":
    main()
