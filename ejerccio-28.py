#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Escribir una función repite_hola que reciba como parámetro un 
número entero n y escriba por pantalla el mensaje "Hola" n veces. Invocarla con distintos valores de n.
"""

def repite_hola(n):

	"""
	Esta funcion recibe como parametro:
	n : int

	que sera mandado en un rango para poder repetirlo con cantidades diferente dentro de un for
	"""

	#recibe como parametro n el for
	for i in range(0,n):
		"""
		impriendo hola , hasta donde se haya indicado
		"""
		print('Hola')


def main():
	print('\tEjerccio 28')
	print()
	#declaramos un variable entero que recibira como parametro un numero entero
	n = int(input("¿Cuantas veces quieres repetir Hola?\n"))

	#llamamos a la funcion repite_hola()
	imprime_hola = repite_hola(n)

if __name__ == '__main__':
	main()