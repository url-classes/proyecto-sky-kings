from CharacterDecorator.FisicCharacter import FisicCharacter
from pygame import Rect
from Colisioner import Colisioner


class HorizontalCharacter(FisicCharacter):
    def move(self, walls: list[Rect], movement: [int, int] = None):
        if movement is None:
            movement = [0, 0]
        self.set_x_coordinate(self.get_x_coordinate() + movement[0])
        colisiones = Colisioner.get_colisiones(self.get_hitbox(), walls)
        for colision in colisiones:
            if movement[0] > 0:
                self.set_right(colision.left)
            elif movement[0] < 0:
                self.set_left(colision.right)
        self.character.move(walls, movement)
        self.update_coordinate()
