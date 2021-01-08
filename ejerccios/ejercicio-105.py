#!/bin/python3
"""
Desarrolla una función que nos permite obtener el valor absoluto de un número.

La función debe cumplir con los siguientes requerimientos.

La función debe tener por nombre absoluto.
La función debe recibir de forma obligatoria un número entero.
La función debe retornar el valor absoluto de dicho número.
Ejemplo.

>>> absoluto(3)
3

>>> absoluto(-5)
5

>>> absoluto(-10)
10


"""

def absoluto(n):
    return abs(n)

def main():
    n = int(input("numero:"))
    res = absoluto(n)
    print(res)

if __name__ == "__main__":
    main()