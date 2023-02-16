#!python3

import unittest 
from my_lexer import lexer
from my_parser import parser
from my_eval import eval 



class TestLexer(unittest.TestCase):
    
    def test_eval(self):

        # test cases for integers
        self.assertEqual(
            eval(parser(lexer("0"))), 
            0
        )

        self.assertEqual(
            eval(parser(lexer("000000000000"))), 
            0
        )

        self.assertEqual(
            eval(parser(lexer("123"))), 
            123
        )

        # test cases for add
        self.assertEqual(
            eval(parser(lexer("(add 0 0)"))), 
            0
        )

        self.assertEqual(
            eval(parser(lexer("(add 1 1)"))), 
            2
        )

        self.assertEqual(
            eval(parser(lexer("(add 123 456)"))),
            579    
        )

        self.assertEqual(
            eval(parser(lexer("(add 0 (add 3 4))"))), 
            7
        )

        self.assertEqual(
            eval(parser(lexer("(add 3 (add (add 3 3) 3))"))),
            12
        )

        # test cases for multiply
        self.assertEqual(
            eval(parser(lexer("(multiply 1 1)"))), 
            1
        )

        self.assertEqual(
            eval(parser(lexer("(multiply 0 (multiply 3 4))"))), 
            0
        )

        self.assertEqual(
            eval(parser(lexer("(multiply 2 (multiply 3 4))"))), 
            24
        )

        self.assertEqual(
            eval(parser(lexer("(multiply 3 (multiply (multiply 3 3) 3))"))), 
            81
        )

        # test cases for mixed

        self.assertEqual(
            eval(parser(lexer("(add 1 (multiply 2 3))"))),
            7   
        )

        self.assertEqual(
            eval(parser(lexer("(multiply 2 (add (multiply 2 3) 8))"))),
            28
        )

        self.assertEqual(
            eval(parser(lexer("(multiply (add 1 2) 3)"))),
            9    
        )

        # test white spaces
        self.assertEqual(
            eval(parser(lexer(" ( \t\t\t\nmultiply (    add 001 2) 3)\n"))), 
            9
        )

        self.assertRaises(
            AssertionError,
            eval,
            parser(lexer(" (abc 0000 cde ) ")), 
        )
        
        


if __name__ == '__main__':
    unittest.main()