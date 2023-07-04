import pygame
import sys
from pygame import *

from Screen import Screen
from Colisioner import Colisioner

from CharacterDecorator.SpriteCharacter import SpriteCharacter
from CharacterDecorator.HorizontalCharacter import HorizontalCharacter
from CharacterDecorator.VerticalCharacter import VerticalCharacter
from CharacterDecorator.ControlCharacter import ControlCharacter
from health_bar import HealthBar
from img import Img
from collide_platform import CollidePlatform


class Play:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.health_bar1 = HealthBar(200, 20)
        self.health_bar2 = HealthBar(200, 20)
        self.num_players_fallen = 0

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
                   pygame.Rect(250, -650, 170, 50), pygame.Rect(625, -650, 170, 50)]
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
            # pygame.draw.rect(ventana.view, (255, 0, 0), personaje.get_hitbox())

            # verificar si caen de las plataformas
            if personaje.get_hitbox().collidelist(kill_collide) != -1:
                self.health_bar1.current_value = 0
                self.num_players_fallen += 1
            if personaje1.get_hitbox().collidelist(kill_collide) != -1:
                self.health_bar2.current_value = 0
                self.num_players_fallen += 1

            # dibujar barras de salud
            if self.health_bar1.current_value > 0:
                pygame.draw.rect(self.screen, (0, 255, 255), (10, 10, self.health_bar1.current_value * 2, 20))
            else:
                pygame.draw.rect(self.screen, (255, 0, 0), (10, 10, self.health_bar1.max_value * 2, 20))

            if self.health_bar2.current_value > 0:
                pygame.draw.rect(self.screen, (0, 255, 255), (
                    self.screen.get_width() - 10 - self.health_bar2.current_value * 2, 10,
                    self.health_bar2.current_value * 2, 20))
            else:
                pygame.draw.rect(self.screen, (255, 0, 0), (
                    self.screen.get_width() - 10 - self.health_bar2.max_value * 2, 10, self.health_bar2.max_value * 2,
                    20))

            # game over cuando ambos personajes caen
            if self.health_bar1.current_value == 0 and self.health_bar2.current_value == 0:
                self.show_game_over_message()
                break  # Salir del bucle principal

            # nombre de jugaores
            font = pygame.font.Font("files/aansa.ttf", 40)
            text_surface1 = font.render("Jugador 1", True, (255, 255, 255))
            text_surface2 = font.render("Jugador 2", True, (255, 255, 255))
            self.screen.blit(text_surface1, (10, 35))
            self.screen.blit(text_surface2, (self.screen.get_width() - text_surface2.get_width() - 10, 35))

            self.screen.blit(personaje.get_actual_frame(), (personaje.get_x_coordinate(), personaje.get_y_coordinate()))
            self.screen.blit(personaje1.get_actual_frame(),
                             (personaje1.get_x_coordinate(), personaje1.get_y_coordinate()))
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

    def show_game_over_message(self):
        font = pygame.font.Font("files/aansa.ttf", 80)
        text_surface = font.render("Game Over", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(5000)  # Pausa de 5 sec antes de salir del juego
        pygame.quit()
        sys.exit()
