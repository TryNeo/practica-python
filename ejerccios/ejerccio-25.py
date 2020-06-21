#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que tome una cantidad m de valores ingresados por el usuario,
a cada uno le calcule el factorial e imprima el resultado junto con el número de orden correspondiente.
"""


import math

def main():
	print("\tEjerccio 25")
	print()

	num = int(input("imgrese un número:"))

	for i in range(0,num):
		resultado = math.factorial(i)
		print(f"{i} - {resultado}")

if __name__ == '__main__':
	main()