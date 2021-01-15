#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Escribir un programa que le pida una palabra al usuario,

para luego imprimirla 1000 veces, con espacios intermedios.

"""

#declaramos la funcion
def intermedios(palabra):
	#declaramos un contador
	contador = 0
	#declaramos un bucle que si el contador es menor que 1000, esto sera true caso contrario que el contador sea mayora sera false y se rompera el bucle
	while contador < 1000:
		#declaramos la variable resultado que llevara como parametro palabra la cual va a tener la funcion replace que remplazara los que no tienen y se les agregara un espacio
		resultado = palabra.replace('',' ')
		print(resultado)
		#e incrementaremos el contador hasta que sea mayor a 1000
		contador+=contador 
	return resultado # y retornamos

#definimos esta funcion que va ejecutar mayor parte del script
def main():
	print("\tEjerccio 6")
	print()
	#declaramos la variable palabra, que recibiria por teclado una palabra que le envie el usuario
	palabra = input("ingrese una palabra:")
	print()
	#declaramos la variable espacio que va instaciar la funcion intermedios que recibe como parametro la palabra
	espacios = intermedios(palabra)


if __name__ == '__main__':
	main()