#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mostrar en pantalla la frecuencia de aparición de vocales 
en una frase dada por el usuario.

Ejemplo : 'Hola Mundo' salida : o=2, a=3, u=1

"""
def vocales(frase):
	
	a = ['a']
	vocal_a = []
	
	e = ['e']
	vocal_e = []

	i = ['i']
	vocal_i = []

	o = ['o']
	vocal_o = []

	u = ['u']
	vocal_u = []

	for x in frase:
		if x in a:
			vocal_a.append(x)
		if x in e:
			vocal_e.append(x)
		if x in i:
			vocal_i.append(x)
		if x in o:
			vocal_o.append(x)
		if x in u:
			vocal_u.append(x)

	print("a:",len(vocal_a))
	print("e:",len(vocal_e))
	print('i:',len(vocal_i))
	print('o:',len(vocal_o))
	print('u:',len(vocal_u))



def main():
	print("\tEjerccio 14")
	print()
	frase = input("ingrese una frase:").lower()
	resultado = vocales(frase)

if __name__ == '__main__':
	main()
