#!/usr/bin/env python3

import unittest
from my_lexer import TokenType, Token, lexer
from my_parser import Expr, parser


TEST_CASES = [

    ["", AssertionError],

    [" \t \n\t", AssertionError],

    ["abc 032", AssertionError],

    ["0mf)(abc 0000 cde )", AssertionError],

    ["$m&)abc 0.0 cde )/", AssertionError],

    ["123",
     Token(TokenType.INTEGER, "123")
     ],

    ["(add 123 456)",
     Expr((Token(TokenType.ID, "add"),
          Token(TokenType.INTEGER, "123"),
          Token(TokenType.INTEGER, "456"),))
     ],

    ["(multiply (add 1 2) 3)",
     Expr((Token(TokenType.ID, "multiply"),
          Expr((Token(TokenType.ID, "add"),
                Token(TokenType.INTEGER, "1"),
                Token(TokenType.INTEGER, "2"),)),
          Token(TokenType.INTEGER, "3"),))
     ],

    [" (abc 0000 cde ) ",
     Expr((Token(TokenType.ID, "abc"),
          Token(TokenType.INTEGER, "0000"),
          Token(TokenType.ID, "cde"),))
     ],
]


class TestParser(unittest.TestCase):

    def testParser(self):
        for testCase in TEST_CASES:
            testInput, result = testCase
            if (type(result) is type) and issubclass(result, Exception):
                self.assertRaises(
                    result,
                    parser,
                    lexer(testInput)
                )
            else:
                self.assertEqual(
                    parser(lexer(testInput)),
                    result
                )


if __name__ == '__main__':
    unittest.main()
