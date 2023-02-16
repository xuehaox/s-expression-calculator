# S-expression Calculator
S-expression Calculator implemented in Python.

> Tested in Python 3.11.1 Windows

## Implementation

`expression` --lexer--> `tokens` --parser--> `ast` --eval--> `result`

## Extensibility

Defining new functions with arbitrary number of arguments is implemented. You can define new functions in `ID_TABLE` in `my_eval.py` file. `Function.call` is the handle of the function, `Function.argc` specifies the number of arguments. 

## Error Handling 

Error handling can be implemented separatly.   

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

