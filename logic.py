##################
# CONSTANTES
##################

DIGITOS = '0123456789'

##################
# ERRORES
##################

class Error:
    def __init__(self, nombre, detalles) -> None:
        self.nombre = nombre
        self.detalles = detalles

    def __repr__(self) -> str:
        return f'{self.nombre}:{self.detalles}'

class CharInvalidoError(Error):
    def __init__(self, detalles) -> None:
        super().__init__('Caracter inválido', detalles)

##################
# TOKENS
##################

TT_INT      = 'INT'
TT_FLOAT    = 'FLOAT'
TT_MAS      = 'MÁS'
TT_MENOS    = 'MENOS'
TT_MULT     = 'MULT'
TT_DIV      = 'DIV'
TT_PAREN_I  = 'PAREN_I'
TT_PAREN_D  = 'PAREN_D'

class Token:
    def __init__(self, tipo, valor=None) -> None:
        self.tipo = tipo
        self.valor = valor

    def __repr__(self) -> str:
        if self.valor:
            return f'{self.tipo}:{self.valor}'
        return f'{self.tipo}'

##################
# LEXER
##################

class Lexer:
    def __init__(self, texto) -> None:
        self.texto = texto
        self.posicion = -1
        self.char_actual = None
        self.__avanzar()

    def __avanzar(self) -> None:
        self.posicion += 1
        self.char_actual = self.texto[self.posicion] if self.posicion < len(self.texto) else None

    def lista_tokens(self) -> list:
        tokens = []

        while self.char_actual != None:
            if self.char_actual in ' \t':
                self.__avanzar()

            elif self.char_actual == '+':
                tokens.append(Token(TT_MAS))
                self.__avanzar()
            
            elif self.char_actual == '-':
                tokens.append(Token(TT_MENOS))
                self.__avanzar()

            elif self.char_actual == '*':
                tokens.append(Token(TT_MULT))
                self.__avanzar()

            elif self.char_actual == '/':
                tokens.append(Token(TT_DIV))
                self.__avanzar()

            elif self.char_actual == '(':
                tokens.append(Token(TT_PAREN_I))
                self.__avanzar()

            elif self.char_actual == ')':
                tokens.append(Token(TT_PAREN_D))
                self.__avanzar()
            
            elif self.char_actual in DIGITOS:
                tokens.append(self.__generar_numero())

            else:
                invalid_char = self.char_actual
                tokens.append(Token("ERROR", self.char_actual))
                self.__avanzar()


        return tokens

    def __generar_numero(self) -> Token:
        num_str = ''
        punto_count = 0

        while self.char_actual != None and self.char_actual in DIGITOS + '.':
            if self.char_actual == '.':
                if punto_count == 1: break
                punto_count += 1
                num_str += '.'
            else:
                num_str += self.char_actual
            self.__avanzar()
            
        if punto_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

##################
# EJECUCION
##################

def run(texto):
    lexer = Lexer(texto)
    return lexer.lista_tokens()
