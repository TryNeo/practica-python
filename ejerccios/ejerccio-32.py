#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""

	Sea un número n, si el número es par dividalo entre dos, si es impar, 
	multiplique por tres y sume uno, haga esto todas las veces que sean necesarias hasta llegar a uno

"""


def collatz(n):
	print(n)
	print()
	print(5*"-")
	while n != 1:
		if n % 2 == 0:
			n = n // 2
			print(n)
		else:
			n = n *3 +1
			print(n)


def main():
	print('\tEjerccio 32')
	print()

	n = int(input("ingrese un numero:"))
	resultado = collatz(n)

if __name__ == '__main__':
	main()


