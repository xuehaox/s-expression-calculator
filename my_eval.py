import operator
from dataclasses import dataclass
from typing import Callable, Dict
from my_lexer import TokenType, Token
from my_parser import Expr



@dataclass(frozen=True)
class Function:
    call: Callable 
    argc: int 


# pre-defined identifiers
ID_TABLE: Dict[str, Function] = {
    "multiply": Function(operator.mul, 2),
    "add": Function(operator.add, 2) 
}


# evaluate an expr recursively
def eval(expr: Expr | Token) -> int:
    
    # evaluate an integer
    if type(expr) == Token:
        assert(expr.type == TokenType.INTEGER)
        return int(expr.value)
    
    # evaluate an expression
    else:
        assert(type(expr.terms) == tuple)
        assert(expr.terms[0].type == TokenType.ID)
        assert(expr.terms[0].value in ID_TABLE)

        function = ID_TABLE.get(expr.terms[0].value)
        assert(type(function) == Function)
        assert(function.argc == len(expr.terms)-1)

        args = list(map(eval, expr.terms[1:]))

        return function.call(*args)

