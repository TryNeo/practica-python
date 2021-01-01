#!/bin/python3

"""
El tema de listas es sin duda uno de los temas preferidos entre los desarrolladores, es por ello que en esta ocasión tocará el turno que desarrolle un programa el cual cumpla con los siguientes requerimientos.

El programa debe ser capaz de crear dos listas a partir de lo que el usuario introduzca en consola (vía teclado).
La longitud de las listas estará dada por el usuario (Pueden ser de longitudes diferentes).
Las listas almacenará, única y exclusivamente, números enteros.
El programa debe mostrar en consola los elementos de ambas listas.
Ejemplo.

Ingresa la longitud de la primera lista: 3
Ingresa un número a la lista: 10
Ingresa un número a la lista: 20
Ingresa un número a la lista: 30

Ingresa la longitud de la segunda lista: 2
Ingresa un número a la lista: 5
Ingresa un número a la lista: 6

[10, 20, 30]
[5, 6]
"""


def main():
    a = [int(input("Ingresa un número a la lista:"))for _ in range(int(input("ingrese la longitud de la primera lista:")))]
    b = [int(input("Ingresa un número a la lista:"))for _ in range(int(input("ingrese la longitud de la segunda lista:")))]
    print(a)
    print(b)
if __name__ == "__main__":
    main()