"""
Para el Homenaje a Michael Jackson, más de 1,6 millones de seguidores se registraron en Internet para participar en el sorteo de entradas para asistir a
 la ceremonia en estadio “Staples Center”, y solo 8.750 participantes serian seleccionados para asistir.
Realice un algoritmo para sortear m boletos entre los n participantes registrados y presentar el listado de los números seleccionados.

Nota: Se supone que las personas se registran una sola vez, Suponga que n es mayor que m.
"""

import threading
import random

def sorteoBoletos(boletos,participantes):
    if participantes >=  boletos: return [[random.choice([j for j in range(1,participantes+1)]),random.randint(1,99999)] for i in range(1,boletos+1)]
    else: return 'Sorteo Imposible'

def main():
    boletos = int(input("Boletos a Sortear:"))
    participantes = int(input("Participantes:"))
    resultado = sorteoBoletos(boletos,participantes)
    print(resultado)    
        

if __name__ == "__main__":
    main()