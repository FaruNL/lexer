import ply.lex as lex

# class Lexer(object):
#     #--------#
#     # TOKENS #
#     #--------#

#     tokens = (
#         'ID',
#         'NUMERO',
#         'MAS',
#         'MENOS',
#         'MULTIPLICACION',
#         'DIVISION',
#         'PARENTESIS_I',
#         'PARENTESIS_D',
#         'PUNTO_COMA',
#         'PUNTO'
#     )

#     #---------#
#     # LEXEMAS #
#     #---------#

#     t_MAS             = r'\+'
#     t_MENOS           = r'-'
#     t_MULTIPLICACION  = r'\*'
#     t_DIVISION        = r'/'
#     t_PARENTESIS_I    = r'\('
#     t_PARENTESIS_D    = r'\)'
#     t_PUNTO_COMA      = r';'
#     t_PUNTO           = r'\.'

#     def t_ID(self, t):
#         r'[a-zA-Z_]\w*'
#         return t

#     def t_NUMERO(self, t):
#         r'\d+'
#         t.value = int(t.value)
#         return t

#     def t_SINGLELINE_COMMENT(self, t):
#         r'//.*'
#         pass

#     def t_MULTILINE_COMMENT(self, t):
#         r'(?s)/\*.*?\*/'
#         pass

#     t_ignore = ' \t\n'

#     #-------------------#
#     # MANEJO DE ERRORES #
#     #-------------------#

#     def t_error(self, t):
#         print("Caracter inválido '%s' - l:%s" % t.value[0], t.lexer.lineno)
#         t.lexer.skip(1)

#     #--------#
#     # RUNNER #
#     #--------#

#     def build(self, **kwargs):
#         self.lexer = lex.lex(module=self, **kwargs)

#     def run(self, data):
#         self.lexer.input(data)
        
#         while True:
#             tok = self.lexer.token()
#             if not tok: break
#             print(tok)

        
# lx = Lexer()
# lx.build()

# data = """12.12 + 12 &\';
# hola perro HOLA hOlA
# /*Perro
# yeih*/"""

# lx.run(data)

# for tok in lx.lexer:
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)


class MyLexer(object):
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

    def t_ID(self, t):
        r'[a-zA-Z_]\w*'
        return t

    def t_NUMERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_SINGLELINE_COMMENT(self, t):
        r'//.*'
        pass

    def t_MULTILINE_COMMENT(self, t):
        r'(?s)/\*.*?\*/'
        pass

    t_ignore = ' \t\n'

    #-------------------#
    # MANEJO DE ERRORES #
    #-------------------#

    def t_error(self, t):
        print("Caracter inválido '%s' - l:%s" % t.value[0], t.lexer.lineno)
        t.lexer.skip(1)

    #--------#
    # RUNNER #
    #--------#

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def run(self, data):
        self.lexer.input(data)
        
        for tok in self.lexer:
            print(f'{tok.type}:{tok.value}')

# Build the lexer and try it out
m = MyLexer()
m.build()
m.run("""3 + 4
hola perro
//asdasldkj 123123
asd123"""
)