#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
""" 
En un juego se lanza un dado 5 veces y se gana cuando la suma de puntos obtenida en los dos primeros lanzamientos es igual a la obtenida en los restantes tres.
"""

def juego():
  Lista = []
  for i in range(1,5+1):
   dado = random.randrange(1,6)
   Lista.append(dado)
  suma = []
  a = Lista[0]+Lista[1]
  b = Lista[2]+Lista[3]+Lista[4]
  if (a == b):
    suma.append(a)
    suma.append(b)
    print('ganador:',1)
  else:
    suma.append(a)
    suma.append(b)
    print('perdedor:',0)
  return suma
  

if __name__ == '__main__':
	print('\tEjerccio 44')
	juego()