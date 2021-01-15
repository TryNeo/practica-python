#!/usr/bin/env python
"""
Desarrolla un programa en Python que nos permita conocer todas las vocales que existen dentro de una palabra.

Requerimentos:

El usuario podrá ingresar, vía teclado, una palabra o sentencia de la cual quiera conocer todas sus vocales.
Todas las vocales deberán imprimirse en una sola línea.
Ejemplo.
"""
def main():
    palabra = input("ingrese una palabra/setencia:").lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    espacio = ''
    vocales_comprehesion = [j for i in vocales for j in palabra if i == j]
    for i in vocales:
        for j in palabra:
            if i == j:
                espacio = j+espacio
    print(espacio)
    print(vocales_comprehesion)
if __name__ == '__main__':
    main()