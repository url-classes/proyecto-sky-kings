import pygame
import sys
from pygame import *

from Screen import Screen
from Colisioner import Colisioner

from CharacterDecorator.SpriteCharacter import SpriteCharacter
from CharacterDecorator.HorizontalCharacter import HorizontalCharacter
from CharacterDecorator.VerticalCharacter import VerticalCharacter
from CharacterDecorator.ControlCharacter import ControlCharacter
from img import Img
from collide_platform import CollidePlatform


class Play:
    def __init__(self, screen: Surface):
        self.screen = screen

    def play_screen(self, path1: str, path2: str):
        pygame.mixer.music.load('Sounds/punch.mp3')
        pygame.mixer.music.play(3)
        back_ground_color = (0, 0, 0)
        personaje = SpriteCharacter(path1, 3, 7, 1024, 1024, 0.1, back_ground_color)
        personaje1 = SpriteCharacter(path2, 3, 7, 1024, 1024, 0.1, back_ground_color)
        personaje = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje)), K_w, K_s, K_a, K_d)
        personaje1 = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje1)), K_UP, K_DOWN, K_LEFT, K_RIGHT)
        paredes = [pygame.Rect(0, 500, 960, 50),
                   pygame.Rect(270, 350, 170, 50), pygame.Rect(570, 350, 170, 50),
                   pygame.Rect(65, 100, 170, 50), pygame.Rect(800, 100, 170, 50),
                   pygame.Rect(300, -150, 170, 50), pygame.Rect(700, -150, 170, 50),
                   pygame.Rect(250, -350, 170, 50), pygame.Rect(625, -350, 170, 50),
                   pygame.Rect(250, -550, 170, 50), pygame.Rect(625, -550, 170, 50),
                   pygame.Rect(250, -750, 170, 50), pygame.Rect(625, -750, 170, 50)]
        kill_collide = [pygame.Rect(0, 500, 960, 2)]
        up = down = left = rigth = False
        distancia_salto = 0
        doble_salto = True

        index = 0
        img_play = Img(self.screen)
        y_pos = -1080
        vel = 5
        collide_platform = CollidePlatform('img/map/platform(0.2)col.png', self.screen, paredes)
        while True:
            img_play.add_img('img/map/map.png', 0, y_pos, 1, 1)
            eventos = pygame.event.get()
            personaje.control_move(eventos)
            personaje1.control_move(eventos)
            personaje.move(paredes)
            personaje1.move(paredes)
            collide_platform.draw_platform(vel)
            #pygame.draw.rect(ventana.view, (255, 0, 0), personaje.get_hitbox())
            if not personaje.die():
                self.screen.blit(personaje.get_actual_frame(), (personaje.get_x_coordinate(), personaje.get_y_coordinate()))
            if not personaje1.die():
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

