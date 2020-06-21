#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al
tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas .

"""
 


def main():
	print('\tEjerccio 39')
	print()

	intCompetidores = int(input('competidores:'))
	intRecord = int(input("record:"))
	TIEMPO_FIJO = 10
	for i in range(0,intCompetidores):
		strNombre = input("ingrese nombre de competidor:\n")
		intTiempo_carrera = int(input("tiempo:"))
		if intTiempo_carrera>= TIEMPO_FIJO:
			print(f"El ganador es : {strNombre}")
			if intTiempo_carrera < intRecord:
				print("No Rompistes el record")
			else:
				print("Rompistes el record")
		else:
			print(f"No Eres el Ganador:{strNombre}")


if __name__ == '__main__':
	main()
