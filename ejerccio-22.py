#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde 0º F hasta 120º F, de 10 en 10.
"""


def main():
	print("\tEjerccio 21")
	print()

	for i in range(0,130,10):
		formula = (i- 32) * 5/9 
		print(f"{i}ºF = {formula}ºC")
	return formula

if __name__ == '__main__':
	main()