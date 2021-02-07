#!/bin/python3

"""
Python es sin duda uno de los lenguajes de programación más versátiles que existen en la actualidad. La cantidad de cosas que podemos hacer con él son muchas y muy variadas, para prueba de ello en esta ocasión será necesario crees un programa el cual imprima en consola el Sistema operativo donde se encuentra ejecutando.

$ python main.py
El sistema operativo es: Darwin
Ayuda: El módulo platform sin duda te será de mucha utilidad.

"""

import platform


if __name__ == "__main__":
	print(platform.system())
