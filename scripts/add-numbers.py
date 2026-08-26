#!/usr/bin/env python3
#***************************************************************************
#                                  _   _ ____  _
#  Project                     ___| | | |  _ \| |
#                             / __| | | | |_) | |
#                            | (__| |_| |  _ <| |___
#                             \___|\___/|_| \_\_____|
#
# Copyright (C) curl project authors, et al.
#
# SPDX-License-Identifier: curl
#
###########################################################################

"""Add two numbers supplied on the command line."""

import argparse
from decimal import Decimal, InvalidOperation


def parse_number(value):
    """Convert a command-line value to a decimal number."""
    try:
        return Decimal(value)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError(f"invalid number: {value!r}") from error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first", type=parse_number)
    parser.add_argument("second", type=parse_number)
    args = parser.parse_args()

    print(args.first + args.second)


if __name__ == "__main__":
    main()
