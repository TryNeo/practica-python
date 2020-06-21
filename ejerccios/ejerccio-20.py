#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que le pregunte al usuario una cantidad de pesos, 
una tasa de interés y un número de años y muestre como resultado el monto final a obtener. 
La fórmula a utilizar es:
Cn = C * (1 + x/100) ^ n
"""


def main():
	print("\tEjerccio 20")
	print()
	pesos = float(input("ingrese una cantidad de pesos:"))
	tasa_interes = float(input("ingrese taza de interes:"))
	agno = int(input("ingrese un numero de años:"))

	frm = pesos * (1 + tasa_interes/100)**agno

	print(f"El Monto final es de {frm}")
if __name__ == '__main__':
	main()
