#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Elabore un diagrama de flujo, tal que dado un valor n entero positivo, calcule y muestre los elementos correspondientes a la CONJETURA DE ULLMAN (en honor al matemático S. Ullman) que consiste en lo siguiente:

Empiece con cualquier entero positivo.
Si es par, divídalo entre 2.
Si es impar multiplíquelo por 3 y agréguele 1.
Obtenga enteros sucesivamente repitiendo el proceso.
Al final se obtendrá el número 1, independientemente del entero inicial.

"""


def ullman():
  print('\tEjerccio 46')
  print()
  n = int(input('ingrese un numero:'))
  if n < 0:
    return False
  else:
    cont=0
    while not(n==1):
        if n % 2 == 0:
            n=n/2
        else:
            n=n*3+1
        cont+=1
    return cont

if __name__ == '__main__':
  conjentura = ullman()
  print(conjentura)