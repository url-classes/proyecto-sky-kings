import pygame
import sys
from pygame import *
from Screen import Screen
from Character import Character
from Colisioner import Colisioner


class Play:
    def __init__(self, screen: surface):
        self.screen = screen

    def play_screen(self):
        personaje = Character('personaje 1.png', 3, 7, 1024, 1024, 0.1, (0, 0, 0))
        paredes = [pygame.Rect(200, 350, 50, 50), pygame.Rect(260, 350, 50, 50)]
        jugador_hb = personaje.get_actual_frame().get_rect()
        up = down = left = rigth = False
        distancia_salto = 0
        doble_salto = True
        index = 0
        while True:
            self.screen.fill((0, 255, 0))

            movimiento = [0, 8]
            if distancia_salto > 0:
                movimiento[1] -= 30
                distancia_salto -= 1
            if down:
                movimiento[1] += 5
            if rigth:
                movimiento[0] += 5
            if left:
                movimiento[0] -= 5
            jugador_hb = Colisioner.moviminento_prueba(jugador_hb, paredes, movimiento)

            for pared in paredes:
                pygame.draw.rect(self.screen, (255, 0, 0), pared)
            pygame.draw.rect(self.screen, (255, 0, 0), jugador_hb)
            if index == 10:
                personaje.actualizar_posee_correr()
            self.screen.blit(personaje.get_actual_mask(), jugador_hb)
            self.screen.blit(personaje.get_actual_frame(), jugador_hb)

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == KEYDOWN:
                    if evento.key == K_w:
                        if distancia_salto == 0 and (Colisioner.tocar_suelo(jugador_hb, paredes) or doble_salto):
                            distancia_salto = 8
                            if doble_salto and not Colisioner.tocar_suelo(jugador_hb, paredes):
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
            if Colisioner.tocar_suelo(jugador_hb, paredes):
                doble_salto = True
            if index < 10:
                index += 1
            else:
                index = 0
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(40)
