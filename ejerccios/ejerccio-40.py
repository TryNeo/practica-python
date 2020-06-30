#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Generar n numeros aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el numero
hexadecimal

PROPIEDAD - > Catedra de Algoritmos y Estructuras de Datos
"""
import random

def main():
	print("\tEjerccio 40")
	print()

	intNumero = int(input("numero:"))
	for i in range(intNumero):
		numero = random.randrange(5000,45000)
		hexadecimal = ''
		valor = numero % 16
		siguiente = numero // 16
		digito = ''
		while valor > 0:
			if valor < 10:
				digito = str(valor)
			else:
				digito = chr(55 + valor)
			hexadecimal = digito + hexadecimal
			valor = siguiente % 16
			siguiente //= 16
		print('El numero ',numero, 'en hexadecimal es', hexadecimal)




if __name__ == '__main__':
	main()