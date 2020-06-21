#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
"""


def main():
	print("\tEjerccio 23")
	print()

	a = int(input("ingrese un numero:"))
	b = int(input("ingrese un numero:"))

	for i in range(a,b + 1):
		if i %2 == 0:
			print(f"Es Par {i}")
		else:
			print(f"Es impar {i}")
			
if __name__ == '__main__':
	main()