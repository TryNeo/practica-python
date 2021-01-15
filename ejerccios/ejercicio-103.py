#!/bin/python3


""" 
Dado una tupla de n número de elementos:

Ejemplo.

('Loki', 'Duke', 'Princesa', 'Lisa', 'Burns', 'Latin')
Desarrolla un script que nos permita almacenar en variables el primer, segundo y último elemento.

Ejemplo.

>>> primer_elemento
Loki

>>> segundo_elemento
Duke

>>> ultimo_elemento
Latin
Restricciones:

No es posible obtener los elementos por su índice.
"""





if __nane__ == "__main__":
    primer_elemento,segundo_elemento,*_,ultimo_elemento = ('Loki', 'Duke', 'Princesa', 'Lisa', 'Burns', 'Latin')
    print(primer_elemento,segundo_elemento,ultimo_elemento)