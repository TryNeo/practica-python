#!/bin/python3


""" 
Una compañía de telecomunicaciones tiene sospechas de que sus datos están
siendo interceptados y desea transmitirlos de manera segura usando algoritmos
de encriptación de tal forma que solo la pueda entender el destinatario.emcriptarcandado

Toda su información se transmite como enteros de 4 dígitos.

El asesor de seguridad informática le recomienda seguir los siguientes pasos:

A cada dígito súmele siete.
Al resultado de esta suma, divídelo para 10 y extráigale el residuo.
El valor resultante reemplaza al dígito original
Intercambie el primer dígito con el tercero y el segundo con el cuarto.
Ejemplo: 
 >> encripta(1254)
 ans= 2189
 
"""

def encriptar(n):
    try:
        encript = [int(i) for i in str(n)]
        a = [(encript[0]+7)%10,(encript[1]+7)%10,(encript[2]+7)%10,(encript[3]+7)%10]
        b = [a[2],a[3],a[0],a[1]]
        return b
    except IndexError as error:
        return "Accion no permitida , Fuera de rango"

def main():
    n = int(input("ingrese numero a encriptar:"))
    if n >= 0 and n >= 4:
        resultado = encriptar(n)
        print(resultado)
    else:
        print("Fuera de rango el PIN")


if __name__ == "__main__":
    main()

    89012