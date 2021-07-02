import ply.lex as lex

class Lexer(object):
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
        print("ERROR: %s" % t.value[0])
        t.lexer.skip(1)

    #--------#
    # RUNNER #
    #--------#

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def run(self, data):
        self.lexer.input(data)
        
        return self.lexer
