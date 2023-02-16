#!/usr/bin/env python3

import sys 
from my_lexer import lexer
from my_parser import parser
from my_eval import eval



if __name__ == "__main__":
    exprStr = sys.argv[1]

    tokens = lexer(exprStr)
    ast = parser(tokens)
    result = eval(ast)

    print(result)


    