#!/bin/venv python


import logging
import threading

"""
El número estándar internacional de un libro (ISBN: International Standard Book Number) es un código de 10 dígitos. La última cifra es un dígito verificador que indica si el ISBN está correcto.
ígito verificador es obtenido mediante la operación residuo de S para 11, donde S es la suma de:

una vez el primer dígito,
mas dos veces el segundo dígito,
mas tres veces el tercer dígito,
mas nueve veces el noveno dígito.

Ejemplo:
 la suma S para el ISBN 9684443242 es:
 1*9+2*6+3*8+4*4+5*4+6*4+7*3+8*2+9*4 = 178
 El dígito verificador es el residuo(178/11) 
 que es igual a 2.
 
 a) Escriba un algoritmo que lea un número ISBN que verifique si éste es o no correcto.

b) Realice la prueba de escritorio de su algoritmo, utilizando el ISBN 9701702533.
"""
logging.basicConfig(
    level = logging.DEBUG,
    format='%(message)s'
)

def main():
    lista=[]
    print("\tEjerccio76")
    isbn = int(input("ingrese isbn:"))
    count=0
    isbn_val = isbn%10
    isbn_content = [i for i in str(isbn)]
    for i in isbn_content[:-1]:
        count = count+1
        result= count*int(i)
        lista.append(result)
    validate = sum(lista)%11
    logging.info('ISBN 10 solo')
    logging.info(f'Valido:{validate==isbn_val}')
  

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()