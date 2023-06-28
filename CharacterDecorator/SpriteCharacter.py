from pygame import *
import pygame
from SpriteSheet import SpriteSheet
from Colisioner import Colisioner
from CharacterDecorator.Character import Character


class SpriteCharacter(Character):
    def move(self, walls: list[Rect], movement=None):
        if movement is None:
            movement = [0, 0]

    def __init__(self, ruta_sprite: str, no_estados: int, no_poses: int, resolucion_x: int, resolucion_y: int,
                 escala: float, color_fondo: (int, int, int)):
        self.frames: list[list[Surface]] = []
        self.previous_pose = 0
        self.current_pose = 0
        self.state = 0
        spriter = SpriteSheet(ruta_sprite)
        for index1 in range(no_estados):
            self.frames.append([])
            for index in range(no_poses):
                self.frames[index1].append(spriter.get_image(
                    index1, index, resolucion_x, resolucion_y, escala, color_fondo))
        self.hitbox = pygame.Rect(0, 0, self.get_actual_frame().get_width() - 30,
                                  self.get_actual_frame().get_height() - 20)
        self.x_coordinate = 0
        self.y_coordinate = 0

    def update_pose(self):
        if self.current_pose < 6:
            ant = self.current_pose
            if self.current_pose == 5:
                self.current_pose = 4
            elif self.current_pose < self.previous_pose:
                if self.current_pose == 3:
                    self.current_pose += 1
                else:
                    self.current_pose -= 1
            else:
                self.current_pose += 1
            self.previous_pose = ant

    def get_actual_frame(self) -> Surface:
        return self.frames[self.state][self.current_pose]

    def set_state(self, estado: int):
        self.state = estado

    def get_hitbox(self):
        return self.hitbox

    def set_up(self, coordinate: int):
        self.hitbox.top = coordinate

    def set_down(self, coordinate: int):
        self.hitbox.bottom = coordinate

    def set_left(self, coordinate: int):
        self.hitbox.left = coordinate

    def set_right(self, coordinate: int):
        self.hitbox.right = coordinate

    def set_hitbox(self, hitbox: Rect):
        self.hitbox = hitbox

    def get_hitbox_x_coordinate(self) -> int:
        return self.hitbox.x

    def get_hitbox_y_coordinate(self) -> int:
        return self.hitbox.y

    def set_hitbox_x_coordinate(self, coordinate: int):
        self.hitbox.x = coordinate

    def set_hitbox_y_coordinate(self, coordinate: int):
        self.hitbox.y = coordinate

    def update_coordinate(self):
        self.x_coordinate = self.hitbox.x - 15
        self.y_coordinate = self.hitbox.y - 10

    def move_position(self, move: [int, int], walls: list[Rect]):
        self.set_hitbox(Colisioner.move_gravity(self.get_hitbox(), walls, move))
        self.update_coordinate()

    def get_x_coordinate(self) -> int:
        return self.x_coordinate

    def get_y_coordinate(self) -> int:
        return self.y_coordinate

    def control_move(self, eventos: event):
        raise NotImplementedError