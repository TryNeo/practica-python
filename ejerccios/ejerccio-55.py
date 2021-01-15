#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
from PIL import Image, ImageDraw, ImageFont
"""
Hace un par de días lanzamos en la plataforma el apartado de Recursos, un lugar donde podrás encontrar tanto artículos como vídeos de temas muy puntales sobre Python.

Cada uno de los temas se listan mediante tarjetas, y creemos es una muy buena idea que cada tarjeta debe poseer un pequeño thumbnail, una imagen representativa del tema. No queremos complicar esto, así que con un simple texto pudiera bastar.

Es por que ello que para esta tarea pedimos tu ayuda. Nos gustaría desarrollaras un pequeño script el cual nos permita generar thumbnails de forma dinámica.

El script debe cumplir con los siguiente requerimientos.

1.El usuario deberá ingresar, mediante teclado, el color de fondo del thumbnail, esto mediante un código hexadecimal.
2.El usuario deberá ingresar, mediante teclado, el texto el cual desea el thumbnail posea.
3.El script debe ser capaz de generar una imagen .PNG con el texto ingresado.
4.La imagen debe tener por dimensiones 780x150
5.El texto debe encontrarse justo en el centro de la image.
6.El texto debe tener un color blanco.
7.El texto debe utilizar la fuente Roboto de google fonts.
8.Hemos pensado que el tamaño de la fuente puede ser de 65, sin embargo esto puede cambiar dependiendo del tipo de fuente (Bold, Italic, etc... ) Dejamos el tamaño, y el estilo de la fuente a tu libre albedrío.
9.Finalmente, el archivo debe tener por nombre el texto ingresado por el usuario, en formato slug.
	Todas las palabras unidas por un guión bajo (_) y todos los caracteres en minúsculas.
	Ejemplo hola_mundo.png

"""
def thumbnail(hexa,titulo):
	if (titulo == " " or titulo == "") and (hexa == " " or hexa == ""):
		return False
	else:
		crea_imagen = Image.new('RGBA',(780,150),hexa)
		draw = ImageDraw.Draw(crea_imagen)
		font = ImageFont.truetype("/usr/share/fonts/truetype/roboto/hinted/Roboto-Bold.ttf", 65)
		draw.text((70,25),titulo, font=font, fill="white",align="center")
		slug = titulo.lower()
		imagen = slug.replace(" ","_")
		
		crea_imagen.save(imagen+'.png')

def main():
	print("Ejerccio 55")
	hexa = input("Ingresa un color hexadecimal:")
	titulo = input("Ingresa el titulo de la imagen:")
	thumbnail(hexa,titulo)

if __name__ == "__main__":
	main()
