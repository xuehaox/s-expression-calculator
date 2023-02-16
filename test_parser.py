#!/usr/bin/env python3

import unittest 
from my_lexer import TokenType, Token, lexer
from my_parser import Expr, parser



class TestLexer(unittest.TestCase):
    
    def test_parser(self):
        
        self.assertRaises(
            AssertionError, 
            parser,
            lexer("") 
        )

        self.assertRaises(
            AssertionError,
            parser,
            lexer(" \t \n\t") 
        )

        self.assertEqual(
            parser(lexer("123")), 
            (Token(TokenType.INTEGER, "123")) 
        )

        self.assertEqual(
            parser(lexer("(add 123 456)")),
            Expr((Token(TokenType.ID, "add"),
                  Token(TokenType.INTEGER, "123"),
                  Token(TokenType.INTEGER, "456"),))
        )

        self.assertEqual(
            parser(lexer("(multiply (add 1 2) 3)")),
            Expr((Token(TokenType.ID, "multiply"), 
                  Expr((Token(TokenType.ID, "add"),
                        Token(TokenType.INTEGER, "1"),
                        Token(TokenType.INTEGER, "2"),)), 
                  Token(TokenType.INTEGER, "3"),))
        )

        self.assertRaises(
            AssertionError,
            parser,
            lexer("abc 032") 
        )

        self.assertEqual(
            parser(lexer(" (abc 0000 cde ) ")), 
            Expr((Token(TokenType.ID, "abc"),
                  Token(TokenType.INTEGER, "0000"),
                  Token(TokenType.ID, "cde"),))
        )

        self.assertRaises(
            AssertionError,
            parser,
            lexer("0mf)(abc 0000 cde )") 
        )
        
        self.assertRaises(
            AssertionError,
            parser,
            lexer("$m&)abc 0.0 cde )/") 
        )


if __name__ == '__main__':
    unittest.main()