from dataclasses import dataclass
from typing import Iterator, Tuple, Union
from my_lexer import TokenType, Token, lexer



@dataclass(frozen=True)
class Expr:
    terms: Tuple[Union['Expr', Token], ...]


# parse tokens recursively
def _parseExpr(tokenIter: Iterator[Token | None]) -> Expr:
    token = next(tokenIter)
    assert(token.type != TokenType.UNKNOWN)
    
    # an expr consists of terms, terms can be expr or token
    terms = []

    while token != None:

        if token.type == TokenType.RPAREN:
            break 

        # parse an embeded expr, then put this expr to terms 
        elif token.type == TokenType.LPAREN:
            terms.append(_parseExpr(tokenIter))
            token = next(tokenIter)
        
        # put a token into terms
        else:
            terms.append(token)
            token = next(tokenIter)
        
    return Expr(tuple(terms))


# parse tokens to AST tree
def parser(tokens: list[Token]) -> Expr | Token:
    # filter whitespace tokens
    tokens = [token for token in tokens if token.type not in [TokenType.WHITESPACE, TokenType.UNKNOWN]]

    assert(len(tokens) != 0)
    
    if len(tokens) == 1:
        return tokens[0]
    
    else:
        tokenIter = iter(tokens + [None])
        
        token = next(tokenIter)
        assert(token.type == TokenType.LPAREN)
        expr = _parseExpr(tokenIter)

        return expr

