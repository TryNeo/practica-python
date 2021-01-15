#!/usr/bin/python3

import random
"""
Desarrolla un programa que nos permita sumar una n cantidad de números aleatorios.

El usuario podrá ingresar vía teclado la cantidad de números aleatorios a generar.
Los números aleatorios generados por el programa deberán comprender del 1 al 100.
El programa deberá mostrar en consola el resultado de la suma de todos los números aleatorios.
Ejemplo.

Cantidad de números aleatorios a generar: 10
El resultado de la suma: 186
Ayuda: La función randint sin duda te será de mucha útilidad.
"""

def sumAleatorios(cantidad):
    suma = 0
    for i in range(1,cantidad):
        suma += random.randint(1,100)
    return suma

def main():
    cantidad = int(input("cantidad de numeros aleatorios a generar:"))
    resultado = sumAleatorios(cantidad)
    print(resultado)

if __name__ == "__main__":
    main()