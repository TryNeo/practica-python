#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desarrolla un programa en Python que escriba, cada segundo, la fecha actual en el archivo: dates.txt. El programa deberá
cumplir con los siguiente requerimientos.
En caso el archivo dates.txt no exista, el programa deberá crearlo.
Cada línea dentro del archivo corresponde a una nueva fecha.
Cada fecha deberá ser añadida al final del archivo.
En caso el archivo exista y posea contenido, la nuevas fechas deberán añadirse al final.
"""
import os.path as path
import datetime
import time


def main():
    print("\tEjerccio 62")
    print("")
    if path.exists('data.txt'):
        file = open('data.txt','a')
        fecha_actual = datetime.datetime.now()
        segundos = fecha_actual.second
        while segundos < 60:
            file.write(str(fecha_actual.date()))
            file.write("\n")
        file.close()
    else:
        file = open('data.txt', 'w')
        fecha_actual = datetime.datetime.now()
        segundos = fecha_actual.second
        while segundos < 60:
            file.write(str(fecha_actual.date()))
            file.write("\n")
        file.close()

if __name__ == '__main__':
    main()
