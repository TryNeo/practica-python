#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""


def main():
  print('\tEjerccio 50')
  print()
  loteria = int(input('numeros de ganadores:'))
  primitiva = []
  for i in range(loteria):
      num = int(input('ingrese el N* - Loteria:'))
      primitiva.append(num)

  primitiva.sort()
  return primitiva

if __name__ == '__main__':
  print(main())