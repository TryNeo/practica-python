#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Mostrar en pantalla la cantidad de vocales que existe en una
 frase dada por el usuario."""

def vocales(frase):
	vocal = ['a','e','i','o','u']
	lista = []
	for i in frase:
		if i in vocal:
			lista.append(i)
	return lista

def main():
	print("\tEjerccio 13")
	print()
	frase = input("ingrese una frase:")
	resultado = vocales(frase)
	print("cantidad de vocales en su frase es de : ",len(resultado))
	return resultado

if __name__ == '__main__':
	main()
