#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año. Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.

"""

def main():
  print('\tEjerccio 49')
  print()
  actual = int(input('año actual:'))
  cualqui =  int(input('año cualquiera:'))

  if actual>cualqui:
    resto=actual-cualqui
    print(f'Desde el año {actual} han pasado {resto} años ')
  elif actual<cualqui:
    resto=cualqui-actual
    print(f'Para llega al año {cualqui} faltan {resto} años ')
  else:
    print('Los años son iguales')

if __name__ == '__main__':
  main()

