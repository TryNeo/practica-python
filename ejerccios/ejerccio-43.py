#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desarrolla un programa el cual nos permita conocer la cantidad de segundos en un día.

El programa debe mostrar en consola la cantidad de segundos que existen en un día.
Ejemplo

$python main.py

Existen 86400 segundos en un día.
"""

def main():
  print('\tEjerccio 43')
  print('')

  SEGUNDOS = 86400
  dia = int(input('dia:'))

  print(f'Existen {dia*SEGUNDOS} segundos en el {dia} dia ')


if __name__ == '__main__':
  main()