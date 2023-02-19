#!/usr/bin/env python3

import unittest
from my_lexer import lexer
from my_parser import parser
from my_eval import eval

TEST_CASES = [
    ("0",
     0
     ),

    ("000000000000",
     0
     ),

    ("123",
     123
     ),

    # test cases for add
    ("(add 0 0),",
     0
     ),

    ("(add 1 1),",
     2
     ),

    ("(add 123 456),",
     579
     ),

    ("(add 0 (add 3 4),),",
     7
     ),

    ("(add 3 (add (add 3 3), 3),),",
     12
     ),

    # test cases for multiply
    ("(multiply 1 1),",
     1
     ),

    ("(multiply 0 (multiply 3 4),),",
     0
     ),

    ("(multiply 2 (multiply 3 4),),",
     24
     ),

    ("(multiply 3 (multiply (multiply 3 3), 3),),",
     81
     ),

    # test cases for mixed
    ("(add 1 (multiply 2 3),),",
     7
     ),

    ("(multiply 2 (add (multiply 2 3), 8),),",
     28
     ),

    ("(multiply (add 1 2), 3),",
     9
     ),

    # test white spaces
    (" ( \t\t\t\nmultiply (    add 001 2), 3),\n",
     9
     ),

    # test exception
    (" (abc 0000 cde ) ", AssertionError)
]


class TestEval(unittest.TestCase):

    def testEval(self):
        for testCase in TEST_CASES:
            testInput, result = testCase
            if (type(result) is type) and issubclass(result, Exception):
                self.assertRaises(
                    result,
                    eval,
                    parser(lexer(testInput))
                )
            else:
                self.assertEqual(
                    eval(parser(lexer(testInput))),
                    result
                )


if __name__ == '__main__':
    unittest.main()
