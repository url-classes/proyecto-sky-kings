import pygame
import sys
from pygame import *
from Screen import Screen
from CharacterDecorator.SpriteCharacter import SpriteCharacter
from CharacterDecorator.HorizontalCharacter import HorizontalCharacter
from CharacterDecorator.VerticalCharacter import VerticalCharacter
from CharacterDecorator.ControlCharacter import ControlCharacter
from img import Img


class Play:
    def __init__(self, screen: Surface):
        self.screen = screen

    def play_screen(self):
        back_ground_color = (0, 0, 0)
        personaje = SpriteCharacter('personaje 2.png', 3, 7, 1024, 1024, 0.1, back_ground_color)
        personaje1 = SpriteCharacter('personaje 1.png', 3, 7, 1024, 1024, 0.1, back_ground_color)
        personaje = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje)), K_w, K_s, K_a, K_d)
        personaje1 = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje1)), K_UP, K_DOWN, K_LEFT, K_RIGHT)
        paredes = [pygame.Rect(0, 500, 960, 50),
                   pygame.Rect(270, 350, 170, 50), pygame.Rect(570, 350, 170, 50),
                   pygame.Rect(65, 100, 170, 50), pygame.Rect(800, 100, 170, 50),
                   pygame.Rect(300, -150, 170, 50), pygame.Rect(700, -150, 170, 50),
                   pygame.Rect(250, -350, 170, 50), pygame.Rect(625, -350, 170, 50),
                   pygame.Rect(250, -550, 170, 50), pygame.Rect(625, -550, 170, 50),
                   pygame.Rect(250, -650, 170, 50), pygame.Rect(625, -650, 170, 50)]
        up = down = left = rigth = False
        distancia_salto = 0
        doble_salto = True
        index = 0
        img_play = Img(self.screen)
        y_pos = -1080
        vel = 0
        while True:
            img_play.add_img('img/map/map.png', 0, y_pos, 1, 1)
            eventos = pygame.event.get()
            personaje.control_move(eventos)
            personaje1.control_move(eventos)
            personaje.move(paredes)
            personaje1.move(paredes)
            for pared in paredes:
                #rectangle = pygame.draw.rect(self.screen, (0, 0, 0), pared)
                pared[1] += vel
                img_play.add_img('img/map/platform(0.2)col.png', pared[0]-10, pared[1], 1, 1)
            if index == 10:
                personaje.update_pose()
                personaje1.update_pose()
            #pygame.draw.rect(ventana.view, (255, 0, 0), personaje.get_hitbox())
            self.screen.blit(personaje.get_actual_frame(), (personaje.get_x_coordinate(), personaje.get_y_coordinate()))
            self.screen.blit(personaje1.get_actual_frame(), (personaje1.get_x_coordinate(), personaje1.get_y_coordinate()))
            for evento in eventos:
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if index < 10:
                index += 1
            else:
                index = 0
            pygame.display.update()
            reloj = pygame.time.Clock()
            if y_pos < 0:
                y_pos += vel
            reloj.tick(40)
