#!/bin/python3

""" 
Ayuda: A las funciones que pueden recibir una n cantidad de argumentos se les conoce como Variadic function.

Desarrolla una función la cual nos permita calcular el promedio de un alumno. La función debe cumplir con los siguiente requerimientos.

La función debe poseer por nombre promedio.
La función debe ser capaz de recibir un n cantidad de calificaciones como argumento.
La función retornará un promedio a partir de dichas calificaciones.
El promedio debe poser un máximo de un dígito después del punto decimal.
Ejemplo.

>>> print(promedio(10, 9, 8, 10, 8, 9))
9.0

>>> print(promedio(10, 7, 7, 8, 9, 10))
8.5

>>> print(promedio(9, 9, 9, 9, 8, 9))
8.8
La función NO debe recibir como argumento una lista.
"""

def promedio(*args):
    prom = [i for i in args]
    return sum(prom)/len(prom)
    

def main():
    n = promedio(10, 7, 7, 8, 9, 10)
    print(n)


if __name__ == "__main__":
    main()