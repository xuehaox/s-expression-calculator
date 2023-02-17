#!/usr/bin/env python3

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
            [Token(TokenType.WHITESPACE, ' \t \n\t'), ]
        )

        self.assertEqual(
            lexer("123"), 
            [Token(TokenType.INTEGER, "123"), ]
        )

        self.assertEqual(
            lexer("(add 123 456)"),
            [Token(TokenType.LPAREN, '('),
             Token(TokenType.ID, "add"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "123"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "456"),
             Token(TokenType.RPAREN, ')'), ]
        )

        self.assertEqual(
            lexer("(multiply (add 1 2) 3)"),
            [Token(TokenType.LPAREN, '('),
             Token(TokenType.ID, "multiply"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.LPAREN, '('),
             Token(TokenType.ID, "add"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "1"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "2"),
             Token(TokenType.RPAREN, ')'),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "3"),
             Token(TokenType.RPAREN, ')'), ]
        )

        self.assertEqual(
            lexer("abc 032"), 
            [Token(TokenType.ID, "abc"), 
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "032"), ]
        )

        self.assertEqual(
            lexer(" (abc 0000 cde ) "), 
            [Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.LPAREN, '('), 
             Token(TokenType.ID, "abc"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "0000"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.ID, "cde"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.RPAREN, ')'), 
             Token(TokenType.WHITESPACE, ' '),]
        )

        self.assertEqual(
            lexer("0mf)(abc 0000 cde )"), 
            [Token(TokenType.INTEGER, "0"),
             Token(TokenType.ID, "mf"),
             Token(TokenType.RPAREN, ')'),
             Token(TokenType.LPAREN, '('), 
             Token(TokenType.ID, "abc"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "0000"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.ID, "cde"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.RPAREN, ')'), ]
        )
        self.assertEqual(
            lexer("$m&)abc 0.0 cde )/"), 
            [Token(TokenType.UNKNOWN, "$"),
             Token(TokenType.ID, "m"),
             Token(TokenType.UNKNOWN, "&"),
             Token(TokenType.RPAREN, ')'),
             Token(TokenType.ID, "abc"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.INTEGER, "0"),
             Token(TokenType.UNKNOWN, "."),
             Token(TokenType.INTEGER, "0"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.ID, "cde"),
             Token(TokenType.WHITESPACE, ' '),
             Token(TokenType.RPAREN, ')'), 
             Token(TokenType.UNKNOWN, "/"),]
        )

        self.assertEqual(
            lexer("(multiply 2 (add (multiply (multiply 2 (add (multiply 2 (multiply 2 (add (multiply 2 3) 8))) 8)) 3) 8))"),
            [
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'multiply'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '2'),
                Token(TokenType.WHITESPACE, ' '), 
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'add'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'multiply'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'multiply'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '2'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'add'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'multiply'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '2'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'multiply'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '2'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'add'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.LPAREN, '('), 
                Token(TokenType.ID, 'multiply'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '2'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '3'), 
                Token(TokenType.RPAREN, ')'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '8'), 
                Token(TokenType.RPAREN, ')'),
                Token(TokenType.RPAREN, ')'),
                Token(TokenType.RPAREN, ')'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '8'), 
                Token(TokenType.RPAREN, ')'),
                Token(TokenType.RPAREN, ')'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '3'), 
                Token(TokenType.RPAREN, ')'), 
                Token(TokenType.WHITESPACE, ' '),
                Token(TokenType.INTEGER, '8'), 
                Token(TokenType.RPAREN, ')'),
                Token(TokenType.RPAREN, ')'),]
        )

if __name__ == '__main__':
    unittest.main()