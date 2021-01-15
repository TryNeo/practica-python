#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definir una función la cual nos permita convertir un string a un formato título. Es entiende por formato título un string con su primera letra en mayúscula.

La función debe tener por nombre to_title.
La función debe poser el parámetro message.
El parámetro debe ser obligatorio.
La función debe retornar el parámetro en su formato título.
Ejemplos.

print(to_title('eduardo'))
>>> Eduardo

print(to_title('hola mundo'))
>>> Hola mundo
"""
def to_title(message):
    if message:
        return message[0].upper()+message[1::]
    else:
        return 'Error!- Ingrese un mensaje'

def main():
    print("\tEjerccio 68")
    print("")
    message = input(":")
    result = to_title(message)
    print(result)

if __name__ == '__main__':
    main()
