
"""
El juego “Hundir el Barco Enemigo” consiste en realizar disparos desde un cañón defensor para hundir un barco rival mientras éste intenta esquivarse.

Considere en un plano cartesiano con las posiciones de ambos.

El cañón permanece en su ubicación inicial, mientras que el barco rival para evadir el disparo puede desplazarse aleatoriamente x metros (entre 1 y 3) y en una dirección aleatoria hacia el norte, sur, este u oeste.

Elabore un algoritmo que permita ingresar la ubicación inicial de avistamiento del barco rival (bx,by), luego registre la ubicación a donde el cañón dispara (cx,cy).

Simule el movimiento de evasión del barco y disparo del cañón, para luego verificar si se alcanzó el objetivo de “Hundir el Barco Enemigo”.
El juego se repite para n intentos de disparo y evasión, al final muestre el resultado del juego.
"""


import random

def barcoRival():
    dezplace = random.randint(1,3)
    direccion = random.randint(1,4)
    return direccion,dezplace

def main():
    n = int(input("¿Cuantas Municiones?:"))
    bx = int(input("¿Barco avistamiento Coordenada bx?:"))
    by = int(input("¿Barco avistamiento Coordenada y?:"))
    intentos = 0
    disparo = 0
    hundido = 0
    while intentos < n:
        intentos+=1
        print(f"Intento {intentos}")
        cx = int(input("¿Disparo cx?:"))
        cy = int(input("¿Disparo cy?:"))
        mov = barcoRival()
        if mov[0] == 1:
            by = by + mov[1]
        if mov[0] == 2:
            by = by - mov[1]
        if mov[0] == 3:
            bx = bx + mov[1]
        if mov[0] == 4:
            bx = bx - mov[1]

        if bx==cx and by == cy:
            hundido+=1
        disparo+=1
        print(f"Movimientos: {mov[0]}, {mov[1]} casillas")
        print('   Hundido: ',hundido)
        print('Disparados: ',disparo)
    print('Barco Hundido:', hundido)
    print('Disparos realizados:',disparo)

if __name__ == "__main__":
    main()