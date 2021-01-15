#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos. Por ejemplo,
si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre ellos.
"""

def four_number(a,b,c,d):
	 resul_pro_one = a * b
	 resul_pro_two = c * d
	 resultado = max(resul_pro_one,resul_pro_two)
	 return resultado



def main():
	print('\tEjerccio 36')
	print()
	a = int(input("ingrese un numero:"))
	b = int(input("ingrese un numero:"))
	c = int(input("ingrese un numero:"))
	d = int(input("ingrese un numero:"))
	producto = four_number(a, b, c, d)
	print(f"El Producto del Numero : {producto}")


if __name__ == '__main__':
	main()