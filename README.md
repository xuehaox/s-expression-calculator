# S-expression Calculator

## Author: Xuehao Xiang

S-expression Calculator implemented in Python.

## Entry Script

`calc.py` is the entry script.

```bash
$ ./calc.py "(add 12 12)"  
24
```

## Implementation

`expression` --lexer--> `tokens` --parser--> `ast` --eval--> `result`

The lexer will take expression string as input, and output a list of tokens (Left Parenthesis, Right Parenthesis, Integer, Identifier, etc.).  
The parser will take tokens as input, and output the abstract syntax tree for the expression.  
the evaluator execute the AST recursively.

## Extensibility

### New type of tokens
New types of tokens can be easily added in `TOKEN_CHARSET` in `my_lexer.py`.  
For example, operators can be allowed by adding `TokenType.OPERATOR: set("+-*/^")`

### New functions
New functions with arbitrary number of arguments can be easily defined in `ID_TABLE` in `my_eval.py` file. `Function.call` is the handle of the function, `Function.argc` specifies the number of arguments.  
For example, to pre-define a `square` function, add `"square": Function(lambda x: x**2, 1),`, then expression like `(square 3)` can be evaluated.

## Error Handling 

 Error handling functions can be implemented separately (without handling errors inside of lexer, parser, and evaluator). 

### Check invalid characters and unknown tokens
A `checkInvalidTokens(tokens: list[Token])` function can be implemented. 
It takes `tokens` as input, and check if `tokens` has `UNKNOWN` type (invalid character) or token's `ID` is not in the `ID_TABLE` (undefined function or variable). 

### Check syntax error

A `checkSyntaxErrors(tokens: list[Token]):` function can be implemented.
It takes `tokens` as input, but only check if parentheses are matched. It can read parentheses and put them into a `stack`. If a `')'` matches with a `'('` in the stack, pop that `'('`, otherwise the syntax of the expression is not correct.
At the end, if there are `'('` left in the stack, the syntax of the expression is not correct.

### Check semantic error

Semantic error can be checked after the `ast` is built.  
A function can be implement that **trys** to execute the `ast` recursively but not actually execute it. It can check if the numbers of arguments of functions are correct and check if all leaf nodes on the `ast` are `Integers`.

