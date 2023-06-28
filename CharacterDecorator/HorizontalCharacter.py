from CharacterDecorator.FisicCharacter import FisicCharacter
from pygame import Rect
from Colisioner import Colisioner


class HorizontalCharacter(FisicCharacter):
    def move(self, walls: list[Rect], movement: [int, int] = None):
        self.character.move(walls, movement)
        if movement is None:
            movement = [0, 0]
        self.character.set_hitbox_x_coordinate(self.character.get_hitbox_x_coordinate() + movement[0])
        colisiones = Colisioner.get_colisiones(self.character.get_hitbox(), walls)
        for colision in colisiones:
            if movement[0] > 0:
                self.character.set_right(colision.left)
            elif movement[0] < 0:
                self.character.set_left(colision.right)
        self.character.update_coordinate()
