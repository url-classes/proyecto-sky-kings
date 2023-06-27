from pygame import *
import pygame
from SpriteSheet import SpriteSheet


class Character:
    def __init__(self, ruta_sprite: str, no_estados: int, no_poses: int, resolucion_x: int, resolucion_y: int,
                 escala: float, color_fondo: (int, int, int)):
        self.sprite = SpriteSheet(ruta_sprite)
        self.frames: list[list[Surface]] = []
        self.masks: list[list[Surface]] = []
        self.no_poses = no_poses
        self.no_estados = no_estados
        self.pose_actual = 0
        self.pose_anterior = 0
        self.estado = 0
        for index1 in range(no_estados):
            self.frames.append([])
            self.masks.append([])
            for index in range(no_poses):
                self.frames[index1].append(self.sprite.get_image(
                    index1, index, resolucion_x, resolucion_y, escala, color_fondo))
                self.masks[index1].append(pygame.mask.from_surface(self.frames[index1][index]).to_surface())

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

    def get_actual_mask(self) -> Surface:
        return self.masks[self.estado][self.pose_actual]