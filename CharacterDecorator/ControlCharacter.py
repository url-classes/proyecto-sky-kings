from CharacterDecorator.FisicCharacter import FisicCharacter
from CharacterDecorator.Character import Character
from pygame import *
from pygame import Rect


class ControlCharacter(FisicCharacter):
    def __init__(self, character: Character, up: int, down: int, left: int, right: int, hit: int):
        super().__init__(character)
        self.up_key = up
        self.down_key = down
        self.left_key = left
        self.right_key = right
        self.hit_key = hit
        self.press_up = False
        self.press_down = False
        self.press_left = False
        self.press_right = False
        self.press_hit = False

    def move(self, walls: list[Rect], movement: [int, int] = None):
        movement = [0, 0]
        if self.press_up:
            movement[1] -= 1
        if self.press_down:
            movement[1] += 5
        if self.press_right:
            movement[0] += 5
        if self.press_left:
            movement[0] -= 5
        self.character.move(walls, movement)

    def attack(self, enemy: Rect):
        if self.press_hit:
            character_hitbox = self.character.get_hitbox()
            if character_hitbox.x + 40 >= enemy.x >= character_hitbox.x - 50:
                if character_hitbox.y + 30 >= enemy.y >= character_hitbox.y - 50:
                    if character_hitbox.x > enemy.x:
                        enemy.x -= 100
                    elif character_hitbox.x < enemy.x:
                        enemy.x += 100
                    print("ataque")

    def control_move(self, eventos: event):
        # for evento in pygame.event.get():
        for evento in eventos:
            if evento.type == KEYDOWN:
                if evento.key == self.up_key:
                    self.press_up = True
                if evento.key == self.down_key:
                    self.press_down = True
                if evento.key == self.left_key:
                    self.press_left = True
                if evento.key == self.right_key:
                    self.press_right = True
                if evento.key == self.hit_key:
                    self.press_hit = True
            elif evento.type == KEYUP:
                if evento.key == self.up_key:
                    self.press_up = False
                if evento.key == self.down_key:
                    self.press_down = False
                if evento.key == self.left_key:
                    self.press_left = False
                if evento.key == self.right_key:
                    self.press_right = False
                if evento.key == self.hit_key:
                    self.press_hit = False
