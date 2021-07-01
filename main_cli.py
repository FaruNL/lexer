from typing import Text
import helper

while True:
    texto = input('> ')
    resultado, error = helper.run(texto)

    if error:
        print(error)
    else:
        print(resultado)