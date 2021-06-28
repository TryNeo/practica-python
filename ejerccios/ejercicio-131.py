#!/usr/bin/python3
import random

"""
  Dada una matriz de 3 x 3.

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 100],
]
Desarrolla un script el cumpla con los siguientes requerimientos.

Mostrar en consola la suma de cada una de las columnas de la matriz.
Mostrar en consola la suma de cada una de las filas de la matriz.
Mostrar en consola la suma de todas las esquinas de la matriz.
Los resultados deben estar separados mediante un guión (-)
Ejemplo.

La suma de las columnas es: 120 - 150 - 190
La suma de las filas es: 60 - 250 - 250
La suma de las esquinas es: 210

"""

aleatorios = [i for i in range(random.randint(0,100))]


def crear_matriz(fila,columna):
    matriz = []
    for i in range(fila):
        matriz.append(random.sample(aleatorios, columna))
    return matriz


if __name__ == "__main__":
    matriz = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 100],
    ]
    filas = len(matriz)
    columnas = len(matriz[0])
    fila = [str(sum(matriz[i])) for i in range(filas)]
    columna = [ str(sum(fila[i] for fila in matriz)) for i in range(columnas)]
    esquinas = matriz[0][0] + matriz[0][2] + matriz[2][0] + matriz[2][2]
    print(esquinas)
    print("La suma de las filas es:"," - ".join(fila))
    print("La suma de las columnas es:"," - ".join(columna))