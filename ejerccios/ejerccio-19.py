#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que use un ciclo definido con rango numérico, 
que averigue a cuántos amigos quieren saludar, les pregunte los nombres 
de esos amigos/as, y los salude.
"""


def main():
	print("\tEjerccio 19")
	print()

	amigos = int(input("¿Cuantos amigos quieres saludar?:"))
	for i in range(0,amigos):
		nombre = input("¿Cual es el nombre de tu amigo?\n")
		print(f"Hola {nombre} saludos")

	print()
	print(f"Saludo {amigos} amigos")


if __name__ == '__main__':
	main()