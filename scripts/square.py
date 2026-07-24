#!/usr/bin/env python3
"""Compute the square of a number."""
import sys


def square(n):
    return n * n


def main(argv):
    if len(argv) != 2:
        print("usage: square.py <number>", file=sys.stderr)
        return 1
    value = float(argv[1])
    print(square(value))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
