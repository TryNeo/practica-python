#!/bin/python3

"""
Dada las siguiente función.

def deposit(amount, balance):
    return amount + balance

def withdraw(amount, balance):
    return balance - amount
Define un decorador que nos permita conocer si la cantidad a depositar o retirar es mayor que 0.

La función debe cumplir con los siguiente requerimientos.

La función (decorador) debe tener por nombre validate_transaction.
En caso la función decorada reciba como argumento una cantidad menor igual a 0, el decorador deberá mostrar el siguiente mensaje en consola:
No es posible completar la operación
En caso la función decorada reciba como argumento una cantidad menor igual a 0, la función decorada no será ejecutada.
Ejemplo.

>>> deposit(10, 100)
110

>>> deposit(0, 100)
No es posible completar la operación

>>> withdraw(0, 100)
No es posible completar la operación

>>> withdraw(10, 100)
90
"""


def validate_transaction(func):
    def validate(*args):
        if list(args)[0] <= 0:
            return "No es posible completar la operación"
        else:
            return func(*args)
    return validate



@validate_transaction
def deposit(amount, balance):
    return amount + balance


@validate_transaction
def withdraw(amount, balance):
    return balance - amount

if __name__ == "__main__":
    print(deposit(0,23))
    print(withdraw(0,100))