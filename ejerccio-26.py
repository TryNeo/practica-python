#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir.
"""



def main():
	print("\tEjerccio 26")
	print()

	for i in range(1,29):
		print(i*"-")
		print(i*"⚫")

if __name__ == '__main__':
	main()