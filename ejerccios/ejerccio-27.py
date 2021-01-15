#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a n.
"""


def main():
	print("\tEjerccio 27")
	print()

	n = int(input("ingree cantidad de fichas:"))

	for i in range(1,n):
		print(i*"-")
		print(i*"⚫")

if __name__ == '__main__':
	main()