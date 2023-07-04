from pygame import Surface, Rect
import pygame
from CharacterDecorator.Character import Character
from CharacterDecorator.SpriteCharacter import SpriteCharacter


class FisicCharacter(Character):
    def __init__(self, character: Character, life_points: int = 100):
        self.character = character
        if type(self.character) == SpriteCharacter:
            self.hitbox = pygame.Rect(self.character.get_x_coordinate(), self.character.get_y_coordinate(), self.get_actual_frame().get_width() - 30, self.get_actual_frame().get_height() - 20)
            self.life_points = life_points
        else:
            self.hitbox = self.character.get_hitbox()
            self.life_points = self.character.get_life_points()

    def get_life_points(self):
        if type(self.character) == SpriteCharacter:
            return self.life_points
        else:
            return self.character.get_life_points()

    def update_pose(self):
        self.character.update_pose()

    def get_actual_frame(self) -> Surface:
        return self.character.get_actual_frame()

    def set_state(self, estado: int):
        self.character.set_state(estado)

    def get_hitbox(self) -> Rect:
        if type(self.character) == SpriteCharacter:
            return self.hitbox
        else:
            return self.character.get_hitbox()

    def set_up(self, coordinate: int):
        if type(self.character) == SpriteCharacter:
            self.hitbox.top = coordinate
        else:
            self.character.set_up(coordinate)

    def set_down(self, coordinate: int):
        if type(self.character) == SpriteCharacter:
            self.hitbox.bottom = coordinate
        else:
            self.character.set_down(coordinate)

    def set_left(self, coordinate: int):
        if type(self.character) == SpriteCharacter:
            self.hitbox.left = coordinate
        else:
            self.character.set_left(coordinate)

    def set_right(self, coordinate: int):
        if type(self.character) == SpriteCharacter:
            self.hitbox.right = coordinate
        else:
            self.character.set_right(coordinate)

    def set_hitbox(self, hitbox: Rect):
        if type(self.character) == SpriteCharacter:
            self.hitbox = hitbox
        else:
            self.character.set_hitbox(hitbox)

    def get_x_coordinate(self) -> int:
        if type(self.character) == SpriteCharacter:
            return self.hitbox.x
        else:
            return self.character.get_x_coordinate()

    def get_y_coordinate(self) -> int:
        if type(self.character) == SpriteCharacter:
            return self.hitbox.y
        else:
            return self.character.get_y_coordinate()

    def set_x_coordinate(self, coordinate: int):
        if type(self.character) == SpriteCharacter:
            self.hitbox.x = coordinate
        else:
            self.character.set_x_coordinate(coordinate)

    def set_y_coordinate(self, coordinate: int):
        if type(self.character) == SpriteCharacter:
            self.hitbox.y = coordinate
        else:
            self.character.set_y_coordinate(coordinate)

    def update_coordinate(self):
        if type(self.character) == SpriteCharacter:
            self.character.set_x_coordinate(self.hitbox.x - 15)
            self.character.set_y_coordinate(self.hitbox.y - 10)
        else:
            self.character.update_coordinate()

    def move(self, walls: list[Rect], movement: [int, int] = None):
        if movement is None:
            movement = [0, 0]
        self.character.move(walls, movement)

    def die(self):
        if self.get_hitbox().bottom > 540:
            self.life_points = 0
        if self.life_points <= 0:
            return True
        else:
            return False



