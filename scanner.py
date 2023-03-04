import ply.lex as lex

reserved = {
    "and": "AND",
}

# List of token names. This is always required
tokens = ("IDENTIFIER", "COMMA", "OP") + tuple(reserved.values())

t_COMMA  = r'\,'

def t_OP(t):
    r"in|not_in|contains|not_contains|eq|not_eq|lt|gt|le|ge"
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z]+"
    t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Test it out
# data = "as IN bn"

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
