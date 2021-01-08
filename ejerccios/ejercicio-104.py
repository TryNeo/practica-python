#!/bin/python3

"""
A partir de la clase Exception generar una excepción llamada DivisionByZero.
El programa debe lanzar una excepción de tipo DivisionByZero (dentro de la función division) siempre que se intente dividir por 0.
El llamado a la función debe encontrarse dentro de un try y un except.
En caso una excepción de tipo DivisionByZero sea lanzada, mostrar en consola el siguiente mensaje: 'No es posible dividir entre 0.'
def division(dividendo, divisor):
    return dividendo / divisor
Ayuda: Recuerda que en Python es mejor pedir perdón que pedir permiso. 🐍🎉
"""

class DivisionByZero(Exception):
    pass



def division(dividendo,divisor):
    if divisor == 0:
        raise DivisionByZero
    return dividendo/divisor

def main():
    try:
        dividendo = 10
        divisor = 0
        division(dividendo,divisor)
    except DivisionByZero:
        print("No es posible dividir entre 0")



if __name__ =="__main__":
    main()