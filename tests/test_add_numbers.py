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

"""Tests for the add-numbers script."""

import subprocess
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "add-numbers.py"


class AddNumbersTest(unittest.TestCase):
    def test_invalid_number_reports_usage_error(self):
        result = subprocess.run(
            [SCRIPT, "nope", "2"], capture_output=True, check=False, text=True
        )

        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid number", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
