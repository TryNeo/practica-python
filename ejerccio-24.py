#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
 Escribir un programa que reciba un número n por parámetro e imprima los primeros n 
 números triangulares, junto con su índice. Los números triangulares se obtienen mediante 
 la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números 
 triangulares, el programa debe imprimir:
"""



def triangulares(num):
	for i in range(1,num):
		resultado = i * (i + 1) / 2
		print(f"{i} - {int(resultado)}")

def main():
	print("\tEjerccio 24")
	print()

	num = int(input("ingrese un numero:"))
	resultado = triangulares(num)


if __name__ == '__main__':
	main()