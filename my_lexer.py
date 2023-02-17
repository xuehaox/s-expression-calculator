from ast import Tuple
from enum import Enum
from dataclasses import dataclass
import string
from typing import Dict, Iterator, Tuple 


class TokenType(Enum):
    UNKNOWN = 0
    ID = 1
    INTEGER = 2
    LPAREN = 3
    RPAREN = 4
    WHITESPACE = 5


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: str | None = None


TOKEN_CHARSET: Dict[TokenType, set] = {
    TokenType.LPAREN: set('('),
    TokenType.RPAREN: set(')'),
    TokenType.WHITESPACE: set(string.whitespace),
    TokenType.ID: set(string.ascii_letters),
    TokenType.INTEGER: set(string.digits),
}


# iterate chars and scan one token, return the token and last char 
def _scanToken(currentChar: str, charsIter: Iterator[str]) -> Tuple[Token, str]:
    # decide token type
    tokenType = TokenType.UNKNOWN

    for key in TOKEN_CHARSET:
        if currentChar in TOKEN_CHARSET[key]:
            tokenType = key 
            break 
    
    # scan unknown token and return
    if tokenType == TokenType.UNKNOWN:
        token = Token(TokenType.UNKNOWN, currentChar)
        currentChar = next(charsIter)
        return token, currentChar
    
    # scan paran
    if tokenType == TokenType.LPAREN or tokenType == TokenType.RPAREN:
        token = Token(tokenType, currentChar)
        currentChar = next(charsIter)
        return token, currentChar
    
    
    # scan token
    tokenStr = currentChar
    charSet = TOKEN_CHARSET[tokenType]

    while True:
        currentChar = next(charsIter)
        
        if currentChar in charSet:
            tokenStr += currentChar
        else:
            break 

    token = Token(tokenType, tokenStr)

    return (token, currentChar)



# read expression characters and produce tokens
def lexer(exp: str) -> list[Token]:
    charsIter = iter(list(exp) + [None])
    currentChar = next(charsIter)
    tokens = []

    while currentChar != None:
        token, currentChar = _scanToken(currentChar, charsIter)
        tokens.append(token)
    
    return tokens

