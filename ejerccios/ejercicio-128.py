#!/usr/bin/python3
import string
import random
"""
Utilizando el módulo string (de la biblioteca estándar de Python) definir una función que permita generar un código promocional.

La función debe tener por nombre get_promo_code.
La función debe retornar un string alfanumérico de 7 caracteres.
Ejemplo.

>>> print(get_promo_code())
9Z51SJG

>>> print(get_promo_code())
Q0AVM2E

>>> print(get_promo_code())
EK12EU6
Ayuda:

Puedes apoyarte de la librería random.
El método join del string puede serte de mucha utilidad.
Restricciones:

El código promocional deberá tener todas sus letras en mayúsculas.
El código promocional podrá o no tener dígitos en él.

"""



def get_promo_code():
    return "".join([random.choice(string.ascii_uppercase+string.digits) for i in range(0,7)])


if __name__ == "__main__":
    print(get_promo_code())