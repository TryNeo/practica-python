#!/bin/python3


"""

Para cierta aplicación informática se necesitan codificar números enteros.

Elabore un ALGORITMO que solicite al usuario un número entero positivo de tres dígitos, el cual necesita ser codificado.

Considere que:
a) Si el dígito de dicho número es 2, 5 o 7, se le debe sumar la unidad.
b) Si el dígito es 1, 4, 8 o 9, se le resta la unidad.
c) Los dígitos restantes no se alteran.

Ejemplos:

Original		Codificado
472	←	383
503	←	603
615	←	606
"""

def codificador(num):
    num_codificado = []
    for i in num:
        if i == "2" or i == "5" or i == "7":
            resultado = int(i)+1
            num_codificado.append(resultado)
        elif  i == "1" or i == "4" or i == "8" or i == "9":
            resultado_2 = int(i) - 1
            num_codificado.append(resultado_2)
        else:
            num_codificado.append(int(i))
    return num_codificado
 
def main():
    try:
        num = int(input("ingrese un numero:"))
        resultado = codificador(str(num))
        print(f"Numero:{num} - Codificado:{resultado}")
    except ValueError as error:
        print("Solo Numeros positivos")

if __name__ == "__main__":
    main()