#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
Crear una lista la cual almacene 10 números positivos ingresados
por el usuario, mostrar en pantalla: la suma de todos los números,

el promedio, el número mayor y el número menor.
"""




def main():
	print('\tEjerccio 9')
	print("ingrese 10 numeros positivos:")
	lista = []
	for i in range(1,11):
		usuario = int(input())
		lista.insert(i,usuario)

		suma = sum(lista)
		promedio = suma / len(lista)

	print()
	print(f"Lista con 10 numeros:{lista}")
	print(f"Suma de los numeros:{suma}")
	print(f"Promedio:{promedio}")
	print(f"Número mayor:{ max(lista)}")
	print(f"Número menor:{ min(lista)}")



if __name__ == '__main__':
	main()