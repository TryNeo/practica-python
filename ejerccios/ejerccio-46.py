#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un programa que lea una lista de diez números y determine cuántos son positivos, y cuántos son negativos.
"""

def main(lista):
  print('\t\t\t\t\tEjerccio 46')
  print()
  negativo = []
  positivo = []
  for i in lista:
    if i < 0:
      negativo.append(i)
    if i > 0:
      positivo.append(i)
  return (len(positivo),len(negativo),len(lista))


if __name__ == '__main__':
  main = main([1,-3,4,-45,10,22,-43,239,-90,10,-3,10,32023,-3])
  print(f'\tLista de {main[2]} digitos negativos o positivos')
  print()
  print(f'Positivos : {main[0]}\nNegativos : {main[1]}')