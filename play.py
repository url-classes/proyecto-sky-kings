import pygame
import sys
from pygame import *
from Screen import Screen
from CharacterDecorator.SpriteCharacter import SpriteCharacter
from CharacterDecorator.HorizontalCharacter import HorizontalCharacter
from CharacterDecorator.VerticalCharacter import VerticalCharacter
from CharacterDecorator.Character import Character
from Colisioner import Colisioner


pygame.init()
back_ground_color = (0, 0, 0)
ventana = Screen(500, 500, 'nose', back_ground_color)
reloj = pygame.time.Clock()

personaje: Character = SpriteCharacter('personaje 2.png', 3, 7, 1024, 1024, 0.1, back_ground_color)
personaje = VerticalCharacter(HorizontalCharacter(personaje))
paredes = [pygame.Rect(0, 350, 50, 50), pygame.Rect(260, 350, 50, 50)]
up = down = left = rigth = False
distancia_salto = 0
doble_salto = True
index = 0
while True:
    ventana.fondear()

    movimiento = [0, 0]
    if up:
        movimiento[1] -= 1
    if down:
        movimiento[1] += 5
    if rigth:
        movimiento[0] += 5
    if left:
        movimiento[0] -= 5
    personaje.move(paredes, movimiento)

    for pared in paredes:
        pygame.draw.rect(ventana.view, (255, 0, 0), pared)
    if index == 10:
        personaje.update_pose()
    #pygame.draw.rect(ventana.view, (255, 0, 0), personaje.get_hitbox())
    ventana.view.blit(personaje.get_actual_frame(), (personaje.get_x_coordinate(), personaje.get_y_coordinate()))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == KEYDOWN:
            if evento.key == K_w:
                up = True
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
