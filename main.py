#!/usr/bin/env python3
"""Ship It Friday: the one-line commit message an AI coding agent
writes right before breaking production on a Friday."""

import os

LINE = "fix: revert revert of the revert (it worked on my machine, anyway deploying)"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)

if __name__ == "__main__":
    main()
