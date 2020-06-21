#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Mostrar el resultado de ejecutar estos bloques de código en el intérprete de python:

>>> for i in range(5):
    print i * i
>>> for i in range(2,6):
    print i, 2**i
>>> for d in [3, 1, 4, 1, 5]:
    print d,
"""

#definiendo el primer for 
def for_one():
	for i in range(5):
	    resultado = i * i
	    print(resultado)
	
	return resultado

#definiendo el segundo for
def for_two():
	for i in range(2,6):
		resultado = 2**i
		print(i,resultado)
	return resultado

#definiendo el tercer for
def for_three():
	for d in [3,1,4,1,5]:
		print(d)


#declarando las variables para  instaciar las funcionesww
a = for_one()
b = for_two()
c = for_three()
