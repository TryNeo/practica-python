#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desarrolla un programa el cual permita al usuario ingresar 3 números positivos vía teclado.

El programa debe ser capaz de imprimir en consola, de forma descendente, los números ingresados.
"""


def main():
  print("\tEjerccio 54")
  print()
  num_one = int(input("ingrese un numero:"))
  num_two = int(input("ingrese un numero:"))
  num_three = int(input("ingrese un numero:"))

  if num_one >0 and num_two > 0 and num_three >0:
    desc = [num_one,num_two,num_three]
    desc.sort(reverse=True)
    for i in desc:
      print(f"{i}",end=" ")
  else:
    print("Alerta ingresa un numero Positivo :)")

if __name__ == '__main__':
  main()