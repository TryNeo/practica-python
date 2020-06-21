#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
 Área de un triángulo en base a sus puntos:

1) Escribir una función que dado un vector al origen (definido por sus puntos x, y),
 devuelva la norma del vector, dada por (x^2 + y^2) ^ 1/2

2) Escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2),
 devuelva la resta de ambos (debe devolver un par de valores).

3) Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2), 
devuelva la distancia entre ambos.


"""

import math

def distancia(x1, y1, x2, y2):
	dist = (x2-x1)**2 +(y2-y1)**2
	return math.sqrt(dist)


def plano(x1, y1, x2, y2):
	m = x2-x1
	m2 = y2-y1
	return m,m2


def vector(x, y):
	resultado = (x**2+y**2)**1/2
	return resultado

def main():
	print("\tEjerccio 37")
	print()

	print(""""
		\t..:Menu:..
		1.Vector
		2.Plano
		3.Distancia 
		""")

	op = input("ingrese una opcion:")
	if op == "1":	
		x = int(input("ingrese el punto x:"))
		y = int(input("ingrese el punto y:"))
		resultado = vector(x, y)
		print(f"El Vector es:{resultado}")
	elif op == "2":
		x1 = int(input("ingrese el punto x1:"))
		y1 = int(input("ingrese el punto y1:"))
		x2 = int(input("ingrese el punto x2:"))
		y2 = int(input("ingrese el punto y2:"))
		resultado_two = plano(x1, y1, x2, y2)
		print(f"Los Puntos : {resultado_two[0],resultado_two[1]}")
	elif op == "3":
		x1 = int(input("ingrese el punto x1:"))
		y1 = int(input("ingrese el punto y1:"))
		x2 = int(input("ingrese el punto x2:"))
		y2 = int(input("ingrese el punto y2:"))
		resultado_three = distancia(x1, y1, x2, y2)
		print(f"La distancia es de : {round(resultado_three,2)}")
	else:
		print("opcion incorrecta")


if __name__ == "__main__":
	main()