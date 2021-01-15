#!/bin/venv python


import logging
import threading

"""

"""
logging.basicConfig(
    level = logging.DEBUG,
    format='%(message)s'
)


def main():
    print("\tEjerccio75")
    lista = []
    while True:
        prta = int(input("ingrese mm de precipitaciones:"))
        if prta == 0:
            break
        else:
            lista.append(prta)
    logging.info(f'Mayor Precipatcion :{max(lista)} mm')
    logging.info(f'Menor Precipatcion :{min(lista)} mm')
    logging.info(f'Total Precipatcion :{sum(lista)} mm')

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()