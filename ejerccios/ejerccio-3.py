#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math #importamos la libreria math 

"""
implementar algoritmos que permitan:

1.Calcular el perímetro y área de un rectángulo dada su base y su altura.
2.Calcular el perímetro y área de un círculo dado su radio.
3.Calcular el volumen de una esfera dado su radio.
4.Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2.
5.Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""

###################################################

#definiendo la funcion que va a calcular la hipotenusa 
def cal_hip(a,b):
	#definimos la formula respectiva usando una variable para calcular el cuadrado
	cuadrado = a**2+b**2
	#definimos la formula respectiva usando el uso de libreria math para poder obtener la raiz cuadrada
	hipotenusa = math.sqrt(cuadrado)
	#imprimos por pantalla el resultado obtenido y ese la hipotenusa,con estilo de formato muy gusto
	print(f"La hipotenusa del triangulo es : {round(hipotenusa,2)}")
	return hipotenusa # y al final retornamos la hipotenusa como resultado final obtenido



def cal_ar_cor(*args):	
	
	#error de principiante deberia arreglar y hacerlo mas accesible a los argumento que le paso que es una tupla

	x1 = args[0]
	y1 = args[1]
	
	x2 = args[2]
	y2 = args[3]


	base = x1 - x2
	altura = y1 - y2

	area = base * altura

	print(f"El Area del rectangulo alineado con los ejes x e y es {area}")

	return area


#definiendo la funcion que va calcular el volumen mediante su radio
def cal_vol(r):	
	#creamos la variable, pi que contendra lo que vale pi
	pi = 3.141592
	#definimos la formula respectiva  usando una variable para calcular el volumen
	volumen = 4/3 * pi * r**3
	#imprimos por pantalla el resultado obtenido del perimetro y area con estilo de formato muy gusto	
	print(f"El volumen de una esfera es : {round(volumen,2)}")
	return volumen  # y al final retornamos el area  y el perimetro 

#definiendo la funcion que va calcular el perimetro y area de un circulo mediante su radio
def cal_per_ar_rad(r):
	#creamos la variable, pi que contendra lo que vale pi
	pi = 3.141592
	#definimos la formula respectiva  usando una variable para calcular la area
	area = pi * r**2
	#definimos la formula respectiva  usando una variable para calcular el perimetro
	perimetro = 2 * pi *r
	#imprimos por pantalla el resultado obtenido del perimetro y area con estilo de formato muy gusto	
	print(f"El Area del circulo es : {round(area,2)} cm2 y su perimetro es {round(perimetro,2)} cm")
	return area, perimetro # y al final retornamos el area  y el perimetro 

#definiendo la funcion que va a calcular la base y altura de un triangulo 
def cal_per_ar(b,a):
	#definimos la siguiente formula para poder obtener el perimetro
	perimetro = 2 * (b+a)
	#definimos la siguiente formula para poder obtener la area 
	area = b * a
	#imprimos por pantalla el resultado obtenido del perimetro y area con estilo de formato muy gusto
	print(f"El Area del rectángulo es {round(area,2)} cm2 y su perimetro es {round(perimetro,2)} cm")
	return area, perimetro # y al final retornamos el area  y el perimetro 

###################################################

###################################################
#declaramos la funcion triangulo
def triangulo():
	print()
	#declaramos las respectivas variables , para poder calcular la hipotenusa del triangulo
	cateto_a = int(input("ingrese un numero:"))
	cateto_b = int(input("ingrese un numero:"))
	print()
	#declaramos las respectivas variables , para poder calcular el area del rectangulo
	hipotenusa = cal_hip(cateto_a, cateto_b)

#declaramos la funcion rectangulo ejes
def rectangulo_ejes():
	print()
	
	x1 = int(input("ingrese x1:"))
	y1 = int(input("ingrese y2:"))
	
	x2 = int(input("ingrese x2:"))
	y2 = int(input("ingrese y2:"))
	
	print()
	rectangulo_coor = cal_ar_cor(x1,y1,x2,y2)

#declaramos la funcion esfera
def esfera():
	print()
	#declaramos las respectiva variable , para poder calcular el volumen de una esfera
	radio = int(input("ingrese el radio del circulo:"))
	print()
	#creamos una variable que contendra una funcion que recibira como parametro nuestra  variable declaradas anteriormente
	esfera = cal_vol(radio)

#declaramos la funcion circulo
def circulo():
	print()
	#declaramos las respectiva variable , para poder calcular el area y perimetro de un circulo
	radio = int(input("ingrese el radio del circulo:"))
	print()
	#creamos una variable que contendra una funcion que recibira como parametro nuestras variables declaradas anteriormente
	circulo = cal_per_ar_rad(radio)

#declaramos la funcion rectangulo 
def rectangulo():
	print()
	#declaramos las respectivas variables , para poder calcular el area del rectangulo
	base = int(input("ingrese la base:"))
	altura= int(input("ingrese la altura:"))
	print()
	#creamos una variable que contendra una funcion que recibira como parametro nuestras variables declaradas anteriormente
	rectangulo = cal_per_ar(base,altura)
	print()

###################################################


#declaramos la funcion main, que va ejecutar un pequeño menu y mayor parte el script
def main():
	print("\t\tEjerccio 3")
	print()
	#declaramos un meno con triple comilla dentro de una variable llamada menu
	menu = """
	1.Calcular el Area y Perimetro de un Rectangulo
	2.Calcular el Area y Perimetro de un circulo
	3.Calcular el Volumen de una esfera
	4.Calcular el area de un rectangulo mediante el uso de coordenadas
	5.Calcular la hipotenusa de un Triangulo	
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
			rectangulo()
			#una vez terminado nos rompera el bucle y le dara a la funcion y al script
			break
		elif opciones == "2":
			circulo()
			break
		elif opciones == "3":
			esfera()
			break
		elif opciones == "4":
			rectangulo_ejes()
			break
		elif opciones == "5":
			triangulo()
			break
		#caso contrario que el usuario ingrese un numero que no exista, le mandara un mensaje de error por pantalla y rompera el bucle
		else:
			print("opcion no existente")
			break


if __name__ == '__main__':
	main()
	