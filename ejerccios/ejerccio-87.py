#!/bin/python3

import datetime

"""
Una persona que deposita C dólares
en una cuenta de ahorros, el banco 
le paga una tasa de interés anual r,
luego de n años tendrá un valor acumulado de A dólares


La siguiente expresión matemática relaciona estos valores:

A=C(1+r)^nA=C(1+r) 



uan y Pedro abren cuentas de ahorros en diferentes bancos.

En el banco X, Juan deposita en una cuenta de ahorros C=200 que paga un interés anual de r=0.08.
En el banco Y, Pedro deposita en otra cuenta de ahorros C=300 que paga un interés anual de r=0.05.
Escriba un algoritmo que solicite los datos para las cuentas de Juan y Pedro, determine el año n cuando la cantidad acumulada A de Juan superará a la cantidad acumulada A de Pedro.

Nota: Para el algoritmo no se considerarán depósitos o retiros entre los años. Suponga que Juan deposita menos que Pedro y que el interés del Banco X es mayor que Y.
"""

def main():
    
    tasa_x = float(input("tasa - Banco x:"))
    ahorro_x = int(input(f"deposite - Banco x:"))

    tasa_y = float(input("tasa - Banco y:"))
    ahorro_y = int(input("deposite - Banco y:"))
    agno = 0
    agno_x = ahorro_x
    agno_y = ahorro_y
    while agno_x <= agno_y:
        agno = agno+1
        agno_x = float(ahorro_x)*((1+tasa_x)**agno)
        agno_y = float(ahorro_y)*((1+tasa_y)**agno)

    print(f"Años Transcurridos {agno}")
if __name__ == "__main__":
    main()