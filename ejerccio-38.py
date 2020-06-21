#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Programa de astrologia: el usuario debe ingresar el dia y 
mes de su cumpleaños y el programa le debe decir a que signo corresponde.
"""


def signo(dia, mes):
	signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
	fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
	
	mes = mes -1
	print(mes)
	if dia > fechas[mes]:
		mes = mes+1
		print(fechas[mes])
	if mes == 12:
		mes = 0
	print("tu signo es :",signo[mes])



def main():
	print("\tEjerccio 38")
	print()

	dia = int(input("ingrese el dia:"))
	mes = int(input("ingrese el mes:"))

	resultado = signo(dia, mes)



if __name__ == "__main__":
	main()