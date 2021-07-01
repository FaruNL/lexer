from typing import Text
import logic

while True:
    texto = input('> ')
    resultado = logic.run(texto)

    print(resultado)
        