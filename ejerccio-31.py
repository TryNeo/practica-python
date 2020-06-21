#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
Escribir otra función repite_saludo que reciba como parámetro un número entero n y 
una cadena saludo retorne el valor de n concatenaciones de saludo. Invocarla con distintos valores de n y de saludo.
"""


def repite_saludo(n,saludo):
	for i in range(0,n):
		print(saludo+str(i))



def main():
	print('\tEjeccio 31')
	print()
	n = int(input("ingrese un numero:"))
	sal = input("ingrese un saludo:")

	imprime_saludo = repite_saludo(n, sal)

if __name__ == '__main__':
	main()