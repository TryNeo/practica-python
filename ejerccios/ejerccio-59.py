#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Realizar un programa que dado un numero, determinar el mayor digito y menor digito de dicho numero
"""
def max_min(value):
    lista = []
    for i in str(value):
        if int(i) == 0:
            return 'No se Admiten 0'
        else:
            lista.append(int(i))
    if len(lista)!= 1:
        if max(lista) == min(lista):
            return 'Los Digitos son iguales'
        elif max(lista)  > min(lista) and min(lista)< max(lista) :
            return 'el mayor digito es:{} ; el menor digito es:{}'.format(max(lista),min(lista))
    else:
        return 'No se pueden comparar un digito'

def main():
    print("\tEjerccio 59")
    print()
    n = int(input("ingrese un numero:"))
    resultado = max_min(n)
    print(resultado)
if __name__ == "__main__":
    main()