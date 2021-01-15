#!/bin/python3

from datetime import datetime

""" 
Desarrolla una función que nos permite generar una fecha a partir de un mes y un año. La función debe cumplir con los siguiente requerimientos.

La función debe tener por nombre get_date_by_month.
La función debe poser dos parámetros: year y month.
La función debe recibir como argumento el año y el mes a partir del cual se desea generar la fecha.
El parámetro year será de tipo entero, y el parámetro month será de tipo string.
El mes deberá ser definido por un string en ingles.
Ejemplo: 'January'
La función siempre retornará el día primero del mes.
En dado caso no sea posible generar la fecha a partir de los datos ingresado, la función retornará la fecha actual.
Ejemplo.
"""
def get_date_by_month(year,month):
    try:
        year_month = month+","+str(year)
        return datetime.strptime(year_month,'%B,%Y')
    except ValueError as error:
        return datetime.now()


def main():
    year = int(input("año:"))
    month = input("mes:")
    resultado = get_date_by_month(year,month)
    print(resultado)
if __name__ == "__main__":
    main()