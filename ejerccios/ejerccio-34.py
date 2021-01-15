#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

"""

def cal_h_m_s(horas, minutos, segundos):
	horas_seg = (horas * 60)*60
	total_seg= (minutos*60)+horas_seg + segundos
	return total_seg

def cal_seg(segundos):
	hora = (segundos//60) // 60
	minutos = (segundos//60)%60
	segundo = segundos % 60 
	return hora,minutos,segundo

def main():
	print('\tEjerccio 34')
	print()

	print("""\t Menu Time:
1. Convertir Horas,Minutos,Segundos a Segundos
2. Convertir Segundos a Horas,Minutos,Segundos
		""")
	op = input('opcion:')
	if op == '1':
		hor = int(input('ingrese la hora:'))
		mina = int(input('ingrese lo minuto:'))	
		seg = int(input('ingrese la segundo:'))
		calculo_1 = cal_h_m_s(hor, mina, seg)
		print()
		print(f'Horas:{hor},Minutos:{mina},Segundos:{seg} --> Esto es a Segundos:{calculo_1}')
	elif op == '2':
		seg = int(input('ingrese los segundos:'))
		calculo_2 = cal_seg(seg)
		print(f'Segundos:{seg} - > Hora:{calculo_2[0]}, Minutos:{calculo_2[1]}, Segundos:{calculo_2[2]}')

if __name__ == '__main__':
	main()