import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from scanner import tokens


def p_expressions(p):
    '''expressions : expression
                   | expression AND expressions'''

    if len(p) == 4:
        expressions = [p[1]]
        if isinstance(p[3], list):
            expressions = expressions + p[3]
        else:
            expressions.append(p[3])
        p[0] = expressions
    else:
        p[0] = p[1]

def p_expression(p):
    "expression : IDENTIFIER OP identifiers"
    p[0] = (p[1], p[2], p[3])


def p_identifiers(p):
    '''identifiers : IDENTIFIER
                   | IDENTIFIER COMMA identifiers'''

    if len(p) == 4:
        identifiers = [p[1]]
        if isinstance(p[3], list):
            identifiers = identifiers + p[3]
        else:
            identifiers.append(p[3])
        p[0] = identifiers
    else:
        p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print(p)
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input("calc > ")
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
