#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Dado una lista de frases ingresadas por el usuario, mostrar 
en pantalla todas aquellas que sean palíndromo.
"""

def palindromo(lista):
	for x in lista:
	    if x==x[::-1]:
	        print(f"Es palindromo {x}")
	    else:
	    	print(f"No es palindromo {x}")

def main():
	global palindromo

	print('\tEjerccio 10')
	print()
	n=int(input("Cuantás frases o palabras deseas ingresar:"))
	lista=[]
	i=0

	while i<n:
	    palabra=input("ingrese la palabra o frase: ").lower()
	    lista.append(palabra.replace('',''))
	    i+=1

	palindromo = palindromo(lista)


if __name__ == '__main__':
	main()