#!/bin/python3



import pygame
import sys
import datetime

"""
Utilizando la librería de PyGame desarrolla un pequeño reloj digital.

El reloj debe mostrar en pantalla la cantidad de segundos transcurridos una vez el programa haya sido ejecutado.
El contador debe encontrarse justo en el centro de la pantalla.

"""


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Reloj Digital")
    font = pygame.font.Font('freesansbold.ttf', 48)
    white = (255, 255, 255)
    red = (115, 38, 80)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(white)

        seconds = pygame.time.get_ticks() // 1000
        text = font.render(str(seconds), True, red)

        rect = text.get_rect()
        rect.center = ( SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        screen.blit(text, rect)

        pygame.display.update()

if __name__ == "__main__":
    main()