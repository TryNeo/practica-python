#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que use un ciclo definido con rango numérico,
que pregunte los nombres de sus cinco mejores amigos/as, y los salude.
"""

def main():
	print("\tEjerccio 18")
	for i in range(0,5):
		print()
		n = input("¿Cual es tu nombre?\n")
		print()
		print(f"Saludos {n} un gusto en conocerte")



if __name__ == '__main__':
	main()