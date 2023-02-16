from enum import Enum
from dataclasses import dataclass
import string 


class TokenType(Enum):
    UNKNOWN = 0
    ID = 1
    INTEGER = 2
    LPAREN = 3
    RPAREN = 4


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: str | None = None


# read expression characters and produce tokens
def lexer(exp: str) -> list[Token]:
    chars = iter(list(exp) + [None])
    char = next(chars)
    tokens = []

    while char != None:
        # ignore white spaces
        if char in string.whitespace:
            char = next(chars)
        
        # read left parenthesis token
        elif char == '(':
            tokens.append(Token(TokenType.LPAREN))
            char = next(chars)
        
        # read right parenthesis token
        elif char == ')':
            tokens.append(Token(TokenType.RPAREN))
            char = next(chars)
        
        # read an integer token
        elif char in string.digits:
            integer = char 
            while True:
                char = next(chars)
                if char is None:
                    break
                elif char not in string.digits:
                    break
                else: 
                    integer += char 
            tokens.append(Token(TokenType.INTEGER, integer))

        
        # read an identifier token
        elif char in string.ascii_letters:
            variable = char 
            while True:
                char = next(chars)
                if char is None:
                    break
                elif char not in string.ascii_letters:
                    break
                else: 
                    variable += char 
            tokens.append(Token(TokenType.ID, variable))

        # read unknown chars
        else:
            tokens.append(Token(TokenType.UNKNOWN, char))
            char = next(chars)

    return tokens

