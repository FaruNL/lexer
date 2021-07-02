import ply.lex as lex

#--------#
# TOKENS #
#--------#

tokens = (
    'ID',
    'NUMERO',
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'PARENTESIS_I',
    'PARENTESIS_D',
    'PUNTO_COMA',
    'PUNTO'
)

#---------#
# LEXEMAS #
#---------#

t_MAS             = r'\+'
t_MENOS           = r'-'
t_MULTIPLICACION  = r'\*'
t_DIVISION        = r'/'
t_PARENTESIS_I    = r'\('
t_PARENTESIS_D    = r'\)'
t_PUNTO_COMA      = r';'
t_PUNTO           = r'\.'

t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SINGLELINE_COMMENT(t):
    r'//.*'
    pass

def t_MULTILINE_COMMENT(t):
    r'(?s)/\*.*?\*/'

#-------------------#
# MANEJO DE ERRORES #
#-------------------#

def t_error(t):
    print("Caracter inválido '%s'" % t.value[0])
    t.lexer.skip(1)

#-------#
# LEXER #
#-------#

lexer = lex.lex()

data = """12.12 + 12 &\';
hola perro HOLA hOlA
/*Perro
yeih*/"""

lexer.input(data)

for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
    
