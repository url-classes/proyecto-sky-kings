from pygame import Surface, Rect

from CharacterDecorator.Character import Character


class FisicCharacter(Character):
    def __init__(self, character: Character):
        self.character = character

    def update_pose(self):
        self.character.update_pose()

    def get_actual_frame(self) -> Surface:
        return self.character.get_actual_frame()

    def set_state(self, estado: int):
        self.character.set_state(estado)

    def get_hitbox(self) -> Rect:
        return self.character.get_hitbox()

    def set_up(self, coordinate: int):
        self.character.set_up(coordinate)

    def set_down(self, coordinate: int):
        self.character.set_down(coordinate)

    def set_left(self, coordinate: int):
        self.character.set_left(coordinate)

    def set_right(self, coordinate: int):
        self.character.set_right(coordinate)

    def set_hitbox(self, hitbox: Rect):
        self.character.set_hitbox(hitbox)

    def get_hitbox_x_coordinate(self) -> int:
        return self.character.get_hitbox_x_coordinate()

    def get_hitbox_y_coordinate(self) -> int:
        return self.character.get_hitbox_y_coordinate()

    def set_hitbox_x_coordinate(self, coordinate: int):
        self.character.set_hitbox_x_coordinate(coordinate)

    def set_hitbox_y_coordinate(self, coordinate: int):
        self.character.set_hitbox_y_coordinate(coordinate)

    def update_coordinate(self):
        self.character.update_coordinate()

    def move(self, walls: list[Rect], movement: [int, int] = None):
        if movement is None:
            movement = [0, 0]
        self.character.move(walls, movement)

    def get_x_coordinate(self) -> int:
        return self.character.get_x_coordinate()

    def get_y_coordinate(self) -> int:
        return self.character.get_y_coordinate()
