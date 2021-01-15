#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no. Se puede mejorar el programa haciendo que tenga en cuenta que no se puede dividir por cero.
"""
from math import remainder


def main():
    print("\tEjerccio 48")
    a = int(input('Escriba el dividendo:'))
    b = int(input('Escriba el divisor:'))
    resto = remainder(a,b)
    if resto < 0:
      dividir = a%b
      cociente = a//b
      print(f'La división no es exacta. Cociente: {cociente} Resto: {dividir}')
    else:
      cociente = a//b
      print(f'La división es exacta. Cociente: {cociente}')


if __name__ == '__main__':
    main()
