#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desarrolla un programa el cual permita al usuarios ingresar un número flotante e imprimirlo en consola.

Requerimientos del programa:

El programa permitirá al usuario ingresar, vía teclado, un número flotante.
El programa imprimirá en consola el número ingresado con precisión 2, es decir, solo 2 números después del punto decimal.
"""


def main():
    print("\tEjerccio 63")
    print("")
    num =  float(input("Ingresa un número flotante:"))
    print(f"{round(num,2)}")

if __name__ == '__main__':
    main()