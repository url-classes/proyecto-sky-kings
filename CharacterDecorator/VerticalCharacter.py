from CharacterDecorator.FisicCharacter import FisicCharacter
from pygame import Rect
from Colisioner import Colisioner
from CharacterDecorator.Character import Character


class VerticalCharacter(FisicCharacter):
    def __init__(self, character: Character):
        super().__init__(character)
        self.jump_distance = 0
        self.double_jump = True
        self.momentum = True

    def move(self, walls: list[Rect], movement: [int, int] = None):
        movement[1] += Colisioner.gravity()
        if self.jump_distance < -6 and (Colisioner.tocar_suelo(self.get_hitbox(), walls) or self.double_jump) and movement[1] < Colisioner.gravity():
            print(Colisioner.tocar_suelo(self.get_hitbox(), walls))
            self.jump_distance = 8
            if self.double_jump and not Colisioner.tocar_suelo(self.get_hitbox(), walls):
                self.double_jump = False
        if Colisioner.tocar_suelo(self.get_hitbox(), walls):
            self.double_jump = True
        if self.jump_distance > 0:
            movement[1] -= 30
        self.jump_distance -= 1
        self.vertical_lineal_move(walls, movement)
        self.character.move(walls, movement)
        self.update_coordinate()
        
    def vertical_lineal_move(self, walls: list[Rect], movement: [int, int] = None):
        self.set_y_coordinate(self.get_y_coordinate() + movement[1])
        colisiones = Colisioner.get_colisiones(self.get_hitbox(), walls)
        for colision in colisiones:
            if movement[1] > 0:
                self.set_down(colision.top)
            elif movement[1] < 0:
                self.set_up(colision.bottom)
        
