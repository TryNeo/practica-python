#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Santiago quiere conocer la suma de todos de los dígitos que comprenden un número. Por ejemplo, 10 y 1456

Número: 10

1 + 0 = 1

Número: 1456

1 + 4 + 5 + 6 = 20

Si bien, la suma es una tarea fácil, también es repetitiva y puede llegar hacer laboriosa para número grandes, es por ello que en esta ocasión será necesario que crees un script el cual nos permita solucionar el problema. Aquí un par de requerimientos.

Definir una función llamada _sum_digits_.
La función debe poseer como parámetro la variable number.
La función debe recibir como argumento, de forma obligatoria, un número entero.
La función debe retornar la suma de todos los dígitos del parámetro.
"""

def sum_digits(number):
    lista = [int(i) for i in str(number)]
    res = print(sum(lista))
    return res

def main():
    print("Ejerccio 58")
    numero = int(input("ingresa un numero:"))
    return sum_digits(numero)

if __name__ == '__main__':
    main()