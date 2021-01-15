#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aplicando las reglas matemáticas de asociatividad, 
decidir cuáles de las siguientes expresiones son iguales entre sí:


1.((b * b) - (4 * a * c)) / (2 * a), b) (b * b - 4 * a * c) / (2 * a)
2.b * b - 4 * a * c / 2 * a
3.(b * b) - (4 * a * c / 2 * a)
4.1 / 2 * b
5.b / 2



En Python hagan lo siguiente: Denle a a, b y c los valores 
10, 100 y 1000 respectivamente y evalúen las expresiones del 
ejercicio anterior.


En Python hagan lo siguiente: Denle a a, b y c los valores 
10.0, 100.0 y 1000.0 respectivamente y evalúen las expresiones
del punto anterior.


"""

#definimos la funcion que ejecutara el script
def main():
	print("\tEjerccio 7")
	print()

	#creamos nuestras respectivas variables
	a = int(input('ingrese un numero:'))
	b = int(input('ingrese un numero:'))
	c = int(input('ingrese un numero:'))

	#creamos nuestras respectivas variables con las formulas para poder haceer la asosiactividad
	mat_asc_one = (((b * b) - (4 * a * c ) / (2 * a),b), (b * b - 4 * a * c) / (2 * a))
	mat_asc_two = b * b - 4 * a * c / 2 * a 	
	mat_asc_three = (b * b) - (4 * a * c / 2 * a)
	mat_asc_four = 1 / 2 * b	
	mat_asc_five = b / 2

	print()

	#e imprimos los resultados respectivos, para poder decicidi cuales son iguales y cuales no
	print(f"1.{mat_asc_one}")
	print(f"2.{mat_asc_two}") 
	print(f"3.{mat_asc_three}")  
	print(f"4.{mat_asc_four}")
	print(f"5.{mat_asc_five}") 
	


if __name__ == '__main__':
	main()