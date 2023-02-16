#!python3

import unittest
from my_lexer import TokenType, Token, lexer



class TestLexer(unittest.TestCase):
    
    def test_lexer(self):
        
        self.assertEqual(
            lexer(""), 
            []
        )

        self.assertEqual(
            lexer(" \t \n\t"), 
            []
        )

        self.assertEqual(
            lexer("123"), 
            [Token(TokenType.INTEGER, "123"), ]
        )

        self.assertEqual(
            lexer("(add 123 456)"),
            [Token(TokenType.LPAREN),
             Token(TokenType.ID, "add"),
             Token(TokenType.INTEGER, "123"),
             Token(TokenType.INTEGER, "456"),
             Token(TokenType.RPAREN), ]
        )

        self.assertEqual(
            lexer("(multiply (add 1 2) 3)"),
            [Token(TokenType.LPAREN),
             Token(TokenType.ID, "multiply"),
             Token(TokenType.LPAREN),
             Token(TokenType.ID, "add"),
             Token(TokenType.INTEGER, "1"),
             Token(TokenType.INTEGER, "2"),
             Token(TokenType.RPAREN),
             Token(TokenType.INTEGER, "3"),
             Token(TokenType.RPAREN), ]
        )

        self.assertEqual(
            lexer("abc 032"), 
            [Token(TokenType.ID, "abc"), 
             Token(TokenType.INTEGER, "032"), ]
        )

        self.assertEqual(
            lexer(" (abc 0000 cde ) "), 
            [Token(TokenType.LPAREN), 
             Token(TokenType.ID, "abc"),
             Token(TokenType.INTEGER, "0000"),
             Token(TokenType.ID, "cde"),
             Token(TokenType.RPAREN), ]
        )

        self.assertEqual(
            lexer("0mf)(abc 0000 cde )"), 
            [Token(TokenType.INTEGER, "0"),
             Token(TokenType.ID, "mf"),
             Token(TokenType.RPAREN),
             Token(TokenType.LPAREN), 
             Token(TokenType.ID, "abc"),
             Token(TokenType.INTEGER, "0000"),
             Token(TokenType.ID, "cde"),
             Token(TokenType.RPAREN), ]
        )
        self.assertEqual(
            lexer("$m&)abc 0.0 cde )/"), 
            [Token(TokenType.UNKNOWN, "$"),
             Token(TokenType.ID, "m"),
             Token(TokenType.UNKNOWN, "&"),
             Token(TokenType.RPAREN),
             Token(TokenType.ID, "abc"),
             Token(TokenType.INTEGER, "0"),
             Token(TokenType.UNKNOWN, "."),
             Token(TokenType.INTEGER, "0"),
             Token(TokenType.ID, "cde"),
             Token(TokenType.RPAREN), 
             Token(TokenType.UNKNOWN, "/"),]
        )

if __name__ == '__main__':
    unittest.main()