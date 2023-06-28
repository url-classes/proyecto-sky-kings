import pygame
import sys
from pygame import *
from Screen import Screen
from Character import Character
from Colisioner import Colisioner


pygame.init()
back_ground_color = (0, 0, 0)
ventana = Screen(500, 500, 'nose', back_ground_color)
reloj = pygame.time.Clock()

personaje = Character('personaje 2.png', 3, 7, 1024, 1024, 0.1, back_ground_color)
paredes = [pygame.Rect(200, 350, 50, 50), pygame.Rect(260, 350, 50, 50)]
up = down = left = rigth = False
distancia_salto = 0
doble_salto = True
index = 0
while True:
    ventana.fondear()

    movimiento = [0, 0]
    if distancia_salto > 0:
        movimiento[1] -= 30
        distancia_salto -= 1
    if down:
        movimiento[1] += 5
    if rigth:
        movimiento[0] += 5
    if left:
        movimiento[0] -= 5
    personaje.move_position(movimiento, paredes)

    for pared in paredes:
        pygame.draw.rect(ventana.view, (255, 0, 0), pared)
    if index == 10:
        personaje.actualizar_posee_correr()
    ventana.view.blit(personaje.get_actual_frame(), (personaje.get_x(), personaje.get_y()))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == KEYDOWN:
            if evento.key == K_w:
                if distancia_salto == 0 and (Colisioner.tocar_suelo(personaje.get_hitbox(), paredes) or doble_salto):
                    distancia_salto = 8
                    if doble_salto and not Colisioner.tocar_suelo(personaje.get_hitbox(), paredes):
                        doble_salto = False
            if evento.key == K_s:
                down = True
            if evento.key == K_a:
                left = True
            if evento.key == K_d:
                rigth = True

        elif evento.type == KEYUP:
            if evento.key == K_w:
                up = False
            if evento.key == K_s:
                down = False
            if evento.key == K_a:
                left = False
            if evento.key == K_d:
                rigth = False
    if Colisioner.tocar_suelo(personaje.get_hitbox(), paredes):
        doble_salto = True
    if index < 10:
        index += 1
    else:
        index = 0
    pygame.display.update()
    reloj.tick(40)
