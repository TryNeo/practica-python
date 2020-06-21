#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Eliminar todas las vocales de una frase dado por el usuario 
y mostrar el nuevo string en pantalla."""

def vocal(frase):
	vocales = ['a', 'e', 'i', 'o', 'u']
	for vocal in vocales:
	    frase = frase.replace(vocal, "")
	return f'Nueva Frase :{frase}'

def main():
	print("\tEjerccio 12")
	print()
	frase= input("introduzca el texto:").lower()
	resultado = vocal(frase)
	print()
	print(resultado)
	return resultado


if __name__ == '__main__':
	main()