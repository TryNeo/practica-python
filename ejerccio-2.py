#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Escribir un programa que pregunte al usuario:

1.su nombre, y luego lo salude.
2.dos números y luego muestre el producto.

"""


#declaramos la funcion que sacara el producto 
def productos(a,b):
	resutlado = (a)*(b)
	# e imprimimos el resultado corresponiendete
	print(resutlado)
	return resutlado # y retornamos el resiltado

#declaramos la variable que va a saludar al usuario
def saludar(nombre):
	saludar = f"Hola {nombre} un gusto verte de nuevo por aqui"
	# e imprimimos el resultado corresponiendete
	print(saludar)
	return saludar 	# y retornamos el resiltado


#declarando la funcion que va ejecutar mayor parte del script
def main():
	print("Ejerccio 2")
	print()
	#declaramos una variable llamado nombre, en donde va a recibit lo que el usuario le mande por el teclado
	nombre = input("ingrese su nombre:")
	#llamamaos a la funcion mediante una variable y le pasamos como parametro la variable declarada anteriormente
	saludo = saludar(nombre)
	#declaramos 2 variables que reciben por teclado 2 numeros enteros 
	uno = int(input("ingrese un numero:"))
	dos = int(input("ingrese un numero:"))
	#llamamos la funcion mediante una variable y le pasamos como parametros las variables declaradas anteriormente
	producto = productos(uno,dos)

if __name__ == '__main__':
	main()


	