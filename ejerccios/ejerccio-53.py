#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("#"*20)
print("\tNotas")
print("#"*20)
#ACTIVIDADES FORMATIVA 30%
act_form_1 = int(input("ingrese la nota formativa:"))
act_form_2 = int(input("ingrese la nota formativa:"))
act_form_3 = int(input("ingrese la nota formativa:"))
act_form_4 = int(input("ingrese la nota formativa:"))
act_form_5 = int(input("ingrese la nota formativa:"))

resultado_form = (act_form_1+act_form_2+act_form_3+act_form_4+act_form_5)/5
ponder_form = resultado_form * 0.30


#ACTIVIDADES PRACTICA  30%
print("")
act_pract_1 = int(input("ingrese la nota pratica:"))
act_pract_2 = int(input("ingrese la nota pratica:"))
act_pract_3 = int(input("ingrese la nota pratica:"))
act_pract_4 = int(input("ingrese la nota pratica:"))
act_pract_5 = int(input("ingrese la nota pratica:"))

resultado_pract = (act_pract_1+act_pract_2+act_pract_3+act_pract_4+act_pract_5)/5
ponder_pract = resultado_pract * 0.30

#EXAMEN 40%
print("")
examen = int(input("Ingrese nota de Examen:"))
ponder_examen = examen * 0.40

resultado_final = ponder_pract+ponder_form+ponder_examen


if int(resultado_final) >= 7:
	print(f"""
		\tAprobado
		Nota Formativa:
		{ponder_form}
		Nota Practica:
		{ponder_pract}
		Nota Examen:{ponder_examen}
		Nota Final:{resultado_final}
		""")
else:
	print(f"Reprobaste tu nota es de :{resultado_final}")