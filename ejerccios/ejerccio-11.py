#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Listar todos los números pares del 0 al 100"""

def main():
	print("\tEjerccio 11")
	print('Numeros pares:')
	lista = []
	for x in range(2,101,2):
		lista.append(x)
	
	resultado =  print(lista)
	return resultado


if __name__ == '__main__':
	main()