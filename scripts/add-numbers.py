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
from decimal import Decimal


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first", type=Decimal)
    parser.add_argument("second", type=Decimal)
    args = parser.parse_args()

    print(args.first + args.second)


if __name__ == "__main__":
    main()
