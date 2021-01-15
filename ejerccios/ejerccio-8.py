#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dado un diccionario, el cual almacena las calificaciones de un alumno, 
siendo las llaves los nombres de las materia 
y los valores las calificación, mostrar en pantalla el promedio 
del alumno.


A partir del diccionario del ejercicio anterior, mostrar en pantalla
la materia con mejor promedio.

"""


#definimos la funcion que va ejecutar el script por completo
def main():
	print('\tEjerccio 8')
	print()
	#declaramos nuestra variable alumno
	alumno = input('ingrese su nombre:')
	
	#hacemos la condicional
	if alumno == '': # en el caso de que el usuario no ingrese ningun usuario,no le dara acesso  a la plataforma
		print("ERROR 403")
	else:
		print(f'\tBienvenid@ a la Plataforma {alumno} | version 1.0')
		print()
		print("""
			Materias disponibles en la plataforma

		1.Algebra y trigonometria
		2.Base de datos
		3.Ingles A2
		4.Lenguaje y Comunicacion
		5.Metodologia del desarrollo de software
		6.Programacion orientada a objeto

			""")

		nota_1 = float(input('ingrese nota de Algebra y trigonometria:'))
		nota_2 = float(input('ingrese nota de Base de datos:'))
		nota_3 = float(input('ingrese nota de Ingles A2:'))
		nota_4 = float(input('ingrese nota de Lenguaje y Comunicacion:'))
		nota_5 = float(input('ingrese nota de Metodologia del desarrollo:'))
		nota_6 = float(input('ingrese nota de Programacion:'))


		calificaciones = {
					
					'Algebra':nota_1,
					'BD':nota_2,
					'Ingles':nota_3,
					'Lenguaje':nota_4,
					'Metodologia':nota_5,
					'Programacion':nota_6

					}
		print()
		for materia, calificacion in calificaciones.items():
			print(f'Materia:{materia} \t Calificacion: {calificacion}')
			print()

		

		cal = (nota_1+nota_2+nota_3+nota_4+nota_5+nota_6)/6
		print(f"El Promedio del Alumno {alumno} es {round(cal,2)}")





if __name__ == '__main__':
	main()