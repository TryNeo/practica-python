#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
"""
Dado una lista de longitud n, desarrolla un programa el cual cumpla con los siguiente requerimientos.

El programa debe ser capaz de crear una lista de longitud n, a partir de los datos ingresados por el usuario (vía teclado).
La longitud de la lista será dada por el usuario.
Las listas almacenará, única y exclusivamente, números enteros.
El programaba debe mostrar en consola el número que más se repite dentro de la lista.
En caso ningún elemento se encuentre más de una vez en la lista, el programa deberá mostrar el siguiente mensaje en consola.
Todos los elementos son únicos en tu lista.

"""


def main():
  global n
  print('\tEjerccio 41')
  print()
  try:
    lista = []
    n = int(input('Cantidad de elementos:'))
    for x in range(1,n+1):
      num = int(input(f'Ingresa el {x}º número:'))
      lista.append(num)
    for i in lista:
      repite = lista.count(i)
    if repite <= 1:
      print('Todos los elementos son únicos en tu lista')
    else:
      print(f"El número que más se repite es:{lista.count(i)}")

  except ValueError as error:
    print("Ingresa un entero - >",error)


if __name__ == '__main__':
  main()