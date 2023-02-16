from dataclasses import dataclass
from typing import Iterator, Union
from my_lexer import TokenType, Token, lexer



@dataclass(frozen=True)
class Expr:
    terms: tuple['Expr'] | Token


# parse tokens recursively
def __parseExpr(tokenIter: Iterator[Token | None]) -> Expr:
    token = next(tokenIter)
    assert(token.type != TokenType.UNKNOWN)
    
    terms = []

    while token != None:
        if token.type == TokenType.INTEGER:
            terms.append(token)
            token = next(tokenIter)

        elif token.type == TokenType.ID:
            terms.append(token)
            token = next(tokenIter)

        # parse an embeded expression
        elif token.type == TokenType.LPAREN:
            terms.append(__parseExpr(tokenIter))
            token = next(tokenIter)
        
        elif token.type == TokenType.RPAREN:
            break 

        else:
            assert(False)
        
    return Expr(tuple(terms))


# parse tokens to AST tree
def parser(tokens: list[Token]) -> Expr | Token:
    assert(len(tokens) != 0)
    
    if len(tokens) == 1:
        return tokens[0]
    
    else:
        tokenIter = iter(tokens + [None])
        
        token = next(tokenIter)
        assert(token.type == TokenType.LPAREN)
        expr = __parseExpr(tokenIter)

        return expr

