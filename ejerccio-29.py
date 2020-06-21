#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir otra función repite_hola que reciba como parámetro un número entero n 
y retorne la cadena formada por n concatenaciones de "Hola". Invocarla con distintos valores de n.
"""

def repite_hola(n):
		"""
	Esta funcion recibe como parametro:
	n : int

	que sera mandado en un rango para poder repetirlo con cantidades diferente dentro de un for
	"""

	#recibe como parametro n el for
	for i in range(0,n):
		print(f'Hola - {i}')



def main():
	print("\tEjerccio 29")
	print()
	#declaramos un variable entero que recibira como parametro un numero entero
	n = int(input("ingrese numero:"))

	#llamamos a la funcion repite_hola()
	iprime_hola = repite_hola(n)

if __name__ == '__main__':
	main()