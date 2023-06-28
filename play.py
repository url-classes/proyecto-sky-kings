import pygame
import sys
from pygame import *
from Screen import Screen
from CharacterDecorator.SpriteCharacter import SpriteCharacter
from CharacterDecorator.HorizontalCharacter import HorizontalCharacter
from CharacterDecorator.VerticalCharacter import VerticalCharacter
from CharacterDecorator.Character import Character
from CharacterDecorator.ControlCharacter import ControlCharacter


pygame.init()
back_ground_color = (0, 0, 0)
ventana = Screen(500, 500, 'nose', back_ground_color)
reloj = pygame.time.Clock()

personaje: Character = SpriteCharacter('personaje 2.png', 3, 7, 1024, 1024, 0.1, back_ground_color)
personaje = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje)), K_w, K_s, K_a, K_d)
paredes = [pygame.Rect(0, 350, 50, 50), pygame.Rect(260, 350, 50, 50)]
up = down = left = rigth = False
distancia_salto = 0
doble_salto = True
index = 0
while True:
    ventana.fondear()
    movimiento = [0, 0]
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
    if index < 10:
        index += 1
    else:
        index = 0
    pygame.display.update()
    reloj.tick(40)
