#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
Implementar algoritmos que resuelvan los siguientes problemas:

1.Dados dos números, indicar la suma, resta, división y multiplicación de ambos.
2.Dado un número entero N, imprimir su tabla de multiplicar.
3.Dado un número entero N, imprimir su fact  orial.

"""


#definiendo la funcion que va sacar el factorial de un numero ingresado
def cal_fact(a): 
	#hacemos una condicional de que si es == a 1  nos retorne el mismo resutlado ingresado , caso contrario nos  sacara el factorial de dicho numero 
	if a == 1:
		return a 
	else: 
		#hacemos la formula respectiva
		resutlado = a *cal_fact(a-1)
		return resutlado

#definiendo la funcion que va a hacer la tabla de multiplicacion 
def tabla_mult_rand(a): 
	#hacemos un for con rango de 0 a 13
	for numero in range(0,13):
		#respectivamente hacemos el calculo
		resultado = numero * a
		print(f"{a} x {numero} = {resultado}")
	return resultado # y retornamos 



#definiendo la funcion que va a calcular la suma, resta, multiplicacion y division 
def calculadora_basic(a,b):
	
	#respectivamente creamoas las variables 
	suma = a + b
	resta = a - b
	mult = a * b 
	div = a /b

	print(f"EL resutlado de  {a} y {b }, entre suma {suma} , resta {resta}, multiplicación {mult} y division {round(div,2)}")

	return suma, resta, mult, div # y retornamos

#definimos la funcion factorial
def factorial():
	print()
	#definimos las variables
	a = int(input("ingres un numero:"))
	print()
	#definimos las variables para poder instanciar la funcion
	factorial = cal_fact(a)
	print(factorial)
	return factorial


#definimos la funcion tabla de multiplicacion
def tabla_mult():
	print()
	#definimos las variables
	a = int(input("ingrese un numero:"))
	print()
	#definimos las variables para poder instanciar la funcion
	tabla = tabla_mult_rand(a)
	return tabla

#definimos la funcion calculadora 
def calculadora():
	print()
	#definimos las variables
	a = int(input("ingresa un numero:"))
	b = int(input("ingresa un numero:"))
	print()
	#definimos las variables para poder instanciar la funcion
	calculadora = calculadora_basic(a, b)
	return calculadora



def main():
	print("\tEjerccio 5")
	print()
	#declaramos un meno con triple comilla dentro de una variable llamada menu
	menu = """
	1.Calculadora
	2.tabla de multiplicacion
	3.factorial
	"""
	#lo imprimimos por pantalla
	print(menu)
	#declaramos una variable llamda funcion que recibira un input , donde el usuario ingresara una de las opciones que existan en el menu
	opciones = input("ingrese una opcion:")
	#declaramos un bucle while
	while True:	
		#hacemos las condicionales para validar las opciones ingresadas por el usuario sean existente
		if opciones == "1":
			#llamamos a unas de las funciones para ejecutar todo lo que hay dentro de esta funcion
			calculadora()
			#una vez terminado nos rompera el bucle y le dara a la funcion y al script
			break
		elif opciones == "2":
			tabla_mult()
			break
		elif opciones == "3":
			factorial()
			break
		#caso contrario que el usuario ingrese un numero que no exista, le mandara un mensaje de error por pantalla y rompera el bucle
		else:
			print("opcion no existente")
			break

if __name__ == '__main__' :
	main()
