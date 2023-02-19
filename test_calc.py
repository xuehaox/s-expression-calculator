#!/usr/bin/env python3

import sys
import unittest
from subprocess import check_output


TEST_CASES = [
    ("0",
     0
     ),

    ("13147483647",
     13147483647
     ),

    ("(add 1547483647 1547483647)",
     1547483647 + 1547483647
     ),

    ("(add 1 1)",
     2
     ),

    ("(add 123 456)",
     579
     ),

    ("(add 0 (add 3 4))",
     7
     ),

    ("(add 3 (add (add 3 3) 3))",
     12
     ),

    ("(multiply 1 1)",
     1
     ),

    ("(multiply 0 (multiply 3 4))",
     0
     ),

    ("(multiply 3 (multiply (multiply 3 3) 3))",
     81
     ),

    ("(add 1 (multiply 2 3))",
     7
     ),

    ("(multiply 2 (add (multiply 2 3) 8))",
     28
     ),

    ("(multiply (add 1 2) 3)",
     9
     ),

    ("(multiply 2 (add (multiply (multiply 2 (add (multiply 2 (multiply 2 (add (multiply 2 3) 8))) 8)) 3) 8))",
     784
     ),
]


def runCalc(expr: str) -> str:
    return check_output('python ./calc.py "{}"'.format(expr), shell=True).decode(sys.stdout.encoding).strip()


class TestCalc(unittest.TestCase):

    def testCalc(self):
        for testCase in TEST_CASES:
            testInput, result = testCase
            self.assertEqual(
                runCalc(testInput),
                str(result)
            )


if __name__ == '__main__':
    unittest.main()
