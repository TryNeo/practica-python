#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un ciclo definido que salude por pantalla a sus cinco mejores amigos/as
"""

def main():
	print("\tEjerccio 17")

	#definiendo una lista sencilla para implementarlo en un for
	lista = ['joel','mari','paola','isela','juka']
	#realizando un ciclo for 
	for i in lista:
		print(f"Hola , saludos desde un bucle for,  {i}")


if __name__ == '__main__':
	main()