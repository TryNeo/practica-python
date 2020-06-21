#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
Recordar que la fórmula para la conversión es:( n °F − 32) × 5/9 
"""

def main():
	print("\tEjerccio 21")
	print()

	gfahren = int(input("ingrese grados Fahrenheit:"))
	formula = (gfahren - 32) * 5/9 
	print(f"Esto es a grado Celsius {formula}°C")

if __name__ == '__main__':
	main()