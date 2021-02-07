#!/bin/python3

"""
Dado el siguiente diccionario.

prices = {
   'A': 89.77,
   'B': 12.65,
   'C': 85.55,
   'D': 7.25,
   'F': 198.75
}
O cualquier otro diccionario que almacene por valores números enteros y/o flotantes. Desarrolla una función que nos permita conocer el valor mínimo de un diccionario. La función debe cumplir los siguiente requerimientos.

La función debe tener por nombre min_dic.
La función debe recibir como argumento un diccionario.
La función debe retornar la llave que almacene el valor minimo dentro del diccionario.
Ejemplo.

prices = {
   'A': 89.77,
   'B': 12.65,
   'C': 85.55,
   'D': 7.25,
   'F': 198.75
}

>>> min_dict(prices)
'D'

"""

def min_dict(dicionario):
    result = list(dicionario.keys())[list(dicionario.values()).index(min([key for key in dicionario.values()]))]
    print(result)

def main():
    prices = {
        'A': 89.77,
        'B': 12.65,
        'C': 85.55,
        'D': 7.25,
        'F': 198.75
    }
    min_dict(prices)



if __name__ == "__main__":
    main()