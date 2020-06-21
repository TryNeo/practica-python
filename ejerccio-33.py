#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Algoritmo de luhn

"""

def luhn(tarjetaCredito):
	#5181271099000012
	suma = 0
	for i in range(len(tarjetaCredito)//2):
		suma += int(tarjetaCredito[2*i])*2//10 + int(tarjetaCredito[2*i])*2%10 + int(tarjetaCredito[2*i+1])//10 + int(tarjetaCredito[2*i+1])%10 
	
	if(suma%10 == 0):
		print('Lunh válido.')
	else:
		print('Lunh inválido.')


def main():
	print("\tEjerccio 33")
	print()

	n = int(input("ingrese un numero:"))
	resultado = luhn(str(n))

if __name__ == '__main__':
	main()