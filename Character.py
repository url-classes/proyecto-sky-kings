from pygame import *
import pygame
from SpriteSheet import SpriteSheet
from Colisioner import Colisioner


class Character:
    def __init__(self, ruta_sprite: str, no_estados: int, no_poses: int, resolucion_x: int, resolucion_y: int,
                 escala: float, color_fondo: (int, int, int)):
        self.frames: list[list[Surface]] = []
        self.pose_actual = 0
        self.pose_anterior = 0
        self.estado = 0
        sprite = SpriteSheet(ruta_sprite)
        for index1 in range(no_estados):
            self.frames.append([])
            for index in range(no_poses):
                self.frames[index1].append(sprite.get_image(
                    index1, index, resolucion_x, resolucion_y, escala, color_fondo))
        self.hitbox = pygame.Rect(0, 0, self.get_actual_frame().get_width() - 30,
                                  self.get_actual_frame().get_height() - 20)
        self.x = 0
        self.y = 0
        self.distance_jump = 0
        self.double_jump = True

    def actualizar_posee_correr(self):
        if self.pose_actual < 6:
            ant = self.pose_actual
            if self.pose_actual == 5:
                self.pose_actual = 4
            elif self.pose_actual < self.pose_anterior:
                if self.pose_actual == 3:
                    self.pose_actual += 1
                else:
                    self.pose_actual -= 1
            else:
                self.pose_actual += 1
            self.pose_anterior = ant

    def get_actual_frame(self) -> Surface:
        return self.frames[self.estado][self.pose_actual]

    def set_etado(self, estado: int):
        self.estado = estado

    def get_hitbox(self):
        return self.hitbox

    def set_hitbox(self, hitbox: Rect):
        self.hitbox = hitbox

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def update_position(self):
        self.x = self.hitbox.x - 15
        self.y = self.hitbox.y - 10

    def move_position(self, move: [int, int], walls: list[Rect]):
        if self.distance_jump == 0 and (Colisioner.tocar_suelo(self.get_hitbox(), walls) or self.double_jump):
            self.distance_jump = 8
            if self.double_jump and not Colisioner.tocar_suelo(self.get_hitbox(), walls):
                self.double_jump = False
        self.set_hitbox(Colisioner.move_gravity(self.get_hitbox(), walls, move))
        self.update_position()
