#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dadas dos listas de números enteros con longitud x y y ( y > x), respectivamente, desarrolla un programa el cual nos permita conocer si los elementos de la lista longitud x se encuentran dentro de la lista con longitud y.

x = [1, 2, 3, 4, 5, 6, 7, 8] 
y = [10, 25, 52, 80, 1, 46, 6, 33, 14, 27, 19]
El programa debe cumplir con los siguiente requerimientos.

Debe existir una función llamada _sub_list.
La función debe poseer los parámetros _list_x_ y _list_y_.
La función debe retornar una nueva lista con todos aquellos elementos que se encuentren tanto en _list_x_ como en _list_y_.
En caso no existan elementos que coincidan, la función debe retornar una lista vacía.

"""

def sub_list(list_x_,list_y_):
  if list_x_ > list_y_:
    return []
  else:
    a = set(list_x_)
    b = set(list_y_)

    comparacion = a & b
    lista = []
    if len(comparacion) >= 0:
      print(f'{list(comparacion)}')
    else:
      return []


def main():
  print('\tEjerccio 42')
  print()

  x = [0, 2, 3, 4, 5] 
  y = [0, 2, 4, 6, 8, 10]
  sub_list(x,y)


if __name__ == '__main__':
  main()