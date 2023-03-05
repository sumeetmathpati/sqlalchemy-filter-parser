import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from .scanner import tokens
from models import Downloads

table = None
cols = {"tenant": Downloads.tenant}


def p_expressions(p):
    """expressions : expression
    | expression AND expressions"""

    p[0] = [p[1]] + p[3] if len(p) == 4 else [p[1]]


def p_expression(p):
    "expression : IDENTIFIER OP identifiers"

    global table
    col = cols.get(p[1])

    if not col:
        p[0] = table

    elif p[2] == "in":
        p[0] = table.filter(col.in_(p[3]))


def p_identifiers(p):
    """identifiers : IDENTIFIER
    | IDENTIFIER COMMA identifiers"""

    p[0] = [p[1]] + p[3] if len(p) == 4 else [p[1]]


# Error rule for syntax errors``
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()


def parse(data, session, s):
    global table

    table = data

    return parser.parse(s)
    