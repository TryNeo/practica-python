#!/bin/python3

"""
Escribe un programa en Python donde el usuario podrá ingresar una secuencia de números enteros. Los números debe encontrarse separados por una coma (,)

Ejemplo.

Ingresa una secuencia de números: 10, 20, 30, 14, 14, 16, 20
El programa debe mostrar en consola la suma de todos los números ingresados.

Ingresa una secuencia de números: 10, 20, 30
El resultado de la suma es: 60
Ayuda: Una función que sin duda te puede ser de mucha utilidad es int.
"""



def main():
    numeros = input("Ingresa una secuencia de números: ")
    numeros = sum([int(i) for i in numeros.split(",")])
    print(numeros)



if __name__ == "__main__":
    main()