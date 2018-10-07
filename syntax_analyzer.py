from ply import lex  # http://manual.freeshell.org/ply/ply.html
import re
from ply.lex import TOKEN

from python_tokens import keywords, identifier

tokens = ['IDENTIFIER', 'ignore', 'SPACETAB']
tokens.extend(keywords)
reserved = {key.lower(): key for key in keywords}



def t_error(t):
    print (f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

@TOKEN(identifier)
def t_IDENTIFIER(t):
    r'[a-z]\w*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

# TODO make tabs
def t_SPACETAB(t):
    r'[ \t]+'
    print("Space(s) and/or tab(s)")
    t.type = 'SPACETAB'
    return t

t_ignore = ' \r\f' # if uncomment ignores tabs


lexer = lex.lex(reflags=re.UNICODE | re.DOTALL, debug = 1)
# lexer = lex.lex(debug=1)
data = '''from _kek'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)