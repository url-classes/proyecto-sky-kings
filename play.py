import pygame
import sys
from pygame import *
from Screen import Screen
from CharacterDecorator.SpriteCharacter import SpriteCharacter
from CharacterDecorator.HorizontalCharacter import HorizontalCharacter
from CharacterDecorator.VerticalCharacter import VerticalCharacter
from CharacterDecorator.ControlCharacter import ControlCharacter


pygame.init()
back_ground_color = (0, 0, 0)
ventana = Screen(500, 500, 'nose', back_ground_color)
reloj = pygame.time.Clock()

personaje = SpriteCharacter('personaje 2.png', 3, 7, 1024, 1024, 0.1, back_ground_color)
personaje1 = SpriteCharacter('personaje 1.png', 3, 7, 1024, 1024, 0.1, back_ground_color)
personaje = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje)), K_w, K_s, K_a, K_d)
personaje1 = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje1)), K_UP, K_DOWN, K_LEFT, K_RIGHT)
paredes = [pygame.Rect(0, 350, 50, 50), pygame.Rect(260, 350, 500, 50)]
up = down = left = rigth = False
distancia_salto = 0
doble_salto = True
index = 0
while True:
    ventana.fondear()
    eventos = pygame.event.get()
    personaje.control_move(eventos)
    personaje1.control_move(eventos)
    personaje.move(paredes)
    personaje1.move(paredes)
    for pared in paredes:
        pygame.draw.rect(ventana.view, (255, 0, 0), pared)
    #if index == 100:
    #    personaje.update_pose()
    #    personaje1.update_pose()
    #pygame.draw.rect(ventana.view, (255, 0, 0), personaje.get_hitbox())
    ventana.view.blit(personaje.get_actual_frame(), (personaje.get_x_coordinate(), personaje.get_y_coordinate()))
    ventana.view.blit(personaje1.get_actual_frame(), (personaje1.get_x_coordinate(), personaje1.get_y_coordinate()))
    for evento in eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if index < 100:
        index += 1
    else:
        index = 0
    pygame.display.update()
    reloj.tick(40)
