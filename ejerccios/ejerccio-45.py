#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
La regla de Paolo Ruffini sirve para realizar la división de un polinomio (de grado mayor que 1) para un binomio de la forma (x – a), ambos con coeficientes enteros.

a) Permita el ingreso de:

El grado n de un polinomio, validando que n sea entero mayor que 1 y menor que 10.
Los coeficientes de dicho polinomio en un arreglo de enteros (el orden de ingreso será desde los coeficientes del término de mayor grado hasta el término independiente).
El valor de a (entero) del divisor ( x – a )
b) Muestre por pantalla el resultado de la división (cociente y residuo).

"""

def ruffini(grado,polinomio):
  if polinomio[0] < 0:
    a = (polinomio[0]) * grado
  else:
    a = grado * polinomio[0] #2 * 1 = 2

  if polinomio[1] < 0:
    b = (polinomio[1]) + a # -3 + 2 = 5
    c = grado * b #10
  else:
    b = polinomio[1] + a
    c = grado * b

  if polinomio[2] < 0:
    c = (polinomio[2]) + c #9
    d = grado * c # 18
  else:
    c = polinomio[2] + c
    d = grado * c
  
  if polinomio[3] < 0:
    e = (polinomio[3]) + d # 17
  else:
    e = polinomio[3] + d

  resultado = [a,b,c,e]
  return f'Relga de ruffini:\n{resultado}'
  
      



def division_polinomio(grado):
  if grado >= 1 and grado <= 10:
    polinomio = []
    for i in range(1,4+1): #rango maximo de 4
      numero = int(input('ingresa un numero:'))
      polinomio.append(numero)
    regla_ruffini = ruffini(grado,polinomio)
    return regla_ruffini
  else:
    return False

if __name__ == '__main__':
  print(division_polinomio(2))