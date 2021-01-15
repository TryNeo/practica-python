#!/bin/env python3


"""
El índice de masa corporal (IMC) es el cociente entre el
 peso de una persona en Kg dividido para su estatura al 
 cuadrado en metros.

La Organización Mundial de la Salud OMS, clasifica a las
 personas según su IMC de la siguiente forma:


IMC	Tipo IMC
Menos de 17	1. Infrapeso
más de 17 hasta 18	2. Bajo Peso
mas de 18 hasta 25	3. Peso Normal
mas de 25 hasta 30	4. Obesidad tipo I
más de 30 hasta 35	5. Obesidad tipo II
mas de 35 hasta 40	6. Obesidad tipo III
mas de 40	7. Obesidad mórbida

Escriba una función tipoimc(peso,estatura) que reciba el peso y 
estatura de una persona para dar como resultado el tipo de masa
corporal

"""

def tipoimc(peso,altura):
    masa_corporal = peso/(altura*altura)
    print(int(masa_corporal))
    if int(masa_corporal) <= 17:
        return f"Infrapeso {round(masa_corporal,2)}"
    elif int(masa_corporal) >= 17 and int(masa_corporal) =< 18:
        return f"Baso peso {round(masa_corporal,2)}"
    elif int(masa_corporal) >= 18 and int(masa_corporal) =< 25:
        return f"Peso Normal {round(masa_corporal,2)}"
    elif int(masa_corporal) >= 25 and int(masa_corporal) =< 30:
        return f"Obesidad 1 {round(masa_corporal,2)}"
    elif int(masa_corporal) >= 30 and int(masa_corporal) =< 35:
        return f"Obesidad 2 {round(masa_corporal,2)}"
    elif int(masa_corporal) >= 35 and int(masa_corporal) =< 40:
        return f"Obesidad 3 {round(masa_corporal,2)}"
    elif int(masa_corporal) >= 40:
        return f"Obesidad morbida {round(masa_corporal,2)}"
    else:
        return f"Error"
def main():
    print("\tEjerccio 79")
    peso = int(input("peso:"))
    altura = float(input("altura:"))
    resultado = tipoimc(peso,altura)
    print(resultado)
if __name__ == "__main__":
    main()