#!/usr/bin/python3

"""
@author Josue lopez

scriba una función validaid(cédula) que valide si un número de cédula ingresado es válido.
Para validar una cédula de identidad ecuatoriana el proceso es el siguiente:

Ejemplo:	0909407173
El décimo es dígito verificador que se validará	3 es el dígito verificador
Se trabaja con los primeros 9 dígitos de la cédula	090940717
Cada dígito de posición impar se lo duplica, si el resultado es mayor que nueve se resta nueve	090980515
Se suman todos los resultados de posición impar	0+0+8+5+5 = 18
Se suman todos los dígitos de posición par	9+9+0+1 = 19
Se suman los dos resultados.	18+19 = 37
Se resta de la decena inmediata superior; en caso de ser 10, el resultado se vuelve a restar 10	40 – 37 = 3
Este es el verificador “calculado”	3
Si el dígito verificador es igual al verificador “calculado”, la cédula es válida, caso contrario es falsa	3 = 3 Cédula válida 
"""

def verificadorCedula(cedula):
    contenido = [int(i) for i in cedula]
    ultimo_digito = contenido[-1]
    primeros_digito = contenido[:-1]
    a = [primeros_digito[i] for i in [i for i in range(0,len(primeros_digito))] if i %2 == 1]
    b = [i for i in [i+i for i in [primeros_digito[i] for i in [i for i in range(0,len(primeros_digito))] if i %2 == 0]] if i <= 9 ]\
        +[ i-9  for i in [i*2 for i in [primeros_digito[i] for i in [i for i in range(0,len(primeros_digito))] if i %2 == 0]] if i >= 9 ]
    digito = str(sum(a)+sum(b))
    total = (int(digito[0])+1)*10
    if total == 10:
        total = 0
    if total-(sum(a)+sum(b)) == ultimo_digito:
        return True
    else:
        return False
def main():
    cedulas = ['0909407173','0996576155','0915336085','0926579640','0936574891']
    for cedula in cedulas:
        resultado = verificadorCedula(cedula)
        print(resultado)

if __name__ == "__main__":
    main()