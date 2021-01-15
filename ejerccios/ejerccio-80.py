#!/usr/bin/env python3

"""
Una vez terminado el invierno, 
el subsidio de la tarifa eléctrica residencial 
cambia para los clientes residenciales en la costa.medidorelectrico

La tarifa se establece acorde a los consumos
 en pliego tarifario mostrado.

Consumo entre (KWh)	Invierno ($)	Verano ($)	Cambio ($)
< 130	0.04	0.04	0.00
130 a 500	0.08	0.11	0.03
500 a 700	0.11	0.13	0.02
superior a 700	0.16	0.26	0.10

a) Ingresar el consumo de n clientes residenciales,

b) Calcular el valor facturado y el incremento para cada cliente en verano,

c) Mostrar el total facturado en el mes y

d) ¿Cuál es el cliente que más valor se le ha facturado? (suponga que existe solo uno).
"""

def consumoElectrico(clientes):
    consumo = list()
    incremento = list()
    cambio_1,cambio_2,cambio_3,cambio_4 = 0,3,2,10
    for i in range(1,clientes+1):
        fact = int(input(f"Cliente {i} consumo entre (kWh):"))
        if fact>=0 and fact <=130:
            consumo.append(float(fact*0.4))
        elif fact >=130 and fact<=500:
            incremento.append(i*(cambio_2+cambio_2))
            consumo.append(float(fact*0.11))
        elif fact >=500 and fact<=700:
            incremento.append(i*(cambio_3+cambio_3))
            consumo.append(float(fact*0.13))
        elif fact >=700:
            incremento.append(i*(cambio_4+cambio_4))
            consumo.append(float(fact*0.26))
    return f'Total Facturado ${sum(consumo)} en el mes\nCliente {consumo.index(max(consumo))} es del  mas valor facturado {max(consumo)}'

def main():
    print("\tEjerccio 80")
    clientes = int(input("clientes residenciales:"))
    resultado = consumoElectrico(clientes)
    print(resultado)

if __name__ == "__main__":
    main()