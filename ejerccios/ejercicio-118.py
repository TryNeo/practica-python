#!/usr/bin/env python
from pathlib import Path
import os
"""
Desarrolla un programa el cual permita a los usuario poder crear nuevos archivo en el sistema.

El usuario podrá ingresar vía teclado, la dirección y el nombre del archivo a crear.
Ejemplo.

>>> Ingresa el nombre del archivo a crear: '/Users/pywombat/eduardo/demo.txt'
Archivo creado de forma exitosa

>>> Ingresa el nombre del archivo a crear: '/Users/pywombat/documents/pywombat.txt'
Archivo creado de forma exitosa
"""

def main():
    paths = input("ingresa el nombre del archivo a crear:").split("/")
    name_archivo = paths[-1]
    dirs = "/".join(paths[:-1])
    dirs = Path(dirs)
    route = dirs / name_archivo
    file = open(route,'w')
    print("archivo creado de forma exitosa")
    file.close()

if __name__ == '__main__':
    main()
