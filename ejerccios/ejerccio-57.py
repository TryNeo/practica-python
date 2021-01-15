#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crea una expresión regular que nos permita conocer si PyWombat se encuentra la comienzo de una cadena de texto.

"""

import re

def main():
    print("Ejerccio 57")
    #palabra clave PyWombat
    patron = re.compile(r'\APyWombat')
    texto = input("ingresa la palabra clave:")
    comprobador = patron.match(texto)
    if comprobador:
        print("se encuentra la comienzo")
    else:
        print("No se encuentra al comienzo")

if __name__ == '__main__':
    main()