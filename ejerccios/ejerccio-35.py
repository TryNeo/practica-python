#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Usando las funciones del ejercicio anterior, escribir un programa que lea de teclado dos tiempos
expresados en horas, minutos y segundos; las sume y muestre el resultado en horas, minutos y segundos por pantalla.
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
	print('\tEjercio 35')
	print()

	print('Tiempo 1')
	hor_one = int(input('ingrese la hora:'))
	mina_one = int(input('ingrese lo minuto:'))	
	seg_one = int(input('ingrese la segundo:'))
	print()
	print('Tiempo 2')
	hor_two = int(input('ingrese la hora:'))
	mina_two = int(input('ingrese lo minuto:'))	
	seg_two = int(input('ingrese la segundo:'))

	cal_one = cal_h_m_s(hor_one, mina_one, seg_one)
	cal_two = cal_h_m_s(hor_two, mina_two, seg_two)

	suma = cal_one + cal_two

	suma_seg = cal_seg(suma)
	print()
	print(f'Hora:{suma_seg[0]}, Minutos:{suma_seg[1]}, Segundos:{suma_seg[2]}')

if __name__ == '__main__':
	main()