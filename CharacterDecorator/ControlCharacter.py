from CharacterDecorator.FisicCharacter import FisicCharacter
from CharacterDecorator.Character import Character
from pygame import *
import pygame


class ControlCharacter(FisicCharacter):
    def __init__(self, character: Character, up: int, down: int, left: int, right: int):
        super().__init__(character)
        self.up_key = up
        self.down_key = down
        self.left_key = left
        self.right_key = right
        self.press_up = False
        self.press_down = False
        self.press_left = False
        self.press_right = False

    def move(self, walls: list[Rect], movement: [int, int] = None):
        movement = [0, 0]
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                if evento.key == self.up_key:
                    self.press_up = True
                if evento.key == self.down_key:
                    self.press_down = True
                if evento.key == self.left_key:
                    self.press_left = True
                if evento.key == self.right_key:
                    self.press_right = True

            elif evento.type == KEYUP:
                if evento.key == self.up_key:
                    self.press_up = False
                if evento.key == self.down_key:
                    self.press_down = False
                if evento.key == self.left_key:
                    self.press_left = False
                if evento.key == self.right_key:
                    self.press_right = False
        if self.press_up:
            movement[1] -= 1
        if self.press_down:
            movement[1] += 5
        if self.press_right:
            movement[0] += 5
        if self.press_left:
            movement[0] -= 5
        print(movement[0])
        self.character.move(walls, movement)

