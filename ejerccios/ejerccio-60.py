#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dada la siguiente lista.

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Mostrar el consola el inverso de la misma.

Ejemplo.

[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Para este ejercicio No es posible el uso de ningún tipo de ciclo.
"""


def main():
    print("\tEjerccio 60")
    print("")
    items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    items.reverse()
    return items    

if __name__ == '__main__':
    print(main())