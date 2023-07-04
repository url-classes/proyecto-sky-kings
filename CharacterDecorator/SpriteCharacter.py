from pygame import *
from SpriteSheet import SpriteSheet
from Colisioner import Colisioner
from CharacterDecorator.Character import Character
from CharacterStates.PoseStatic import PoseStatic
from CharacterStates.PoseJump import PoseJump
from CharacterStates.PoseRun import PoseRun


class SpriteCharacter(Character):
    def move(self, walls: list[Rect], movement=None):
        if movement is None:
            movement = [0, 0]
        if movement == [0, 0] or movement == [0, Colisioner.gravity()]:
            self.pose = PoseStatic(self, self.pose.previous_pose, self.pose.current_pose, self.pose.delay)
        elif movement[1] != Colisioner.gravity():
            self.pose = PoseJump(self, self.pose.previous_pose, self.pose.current_pose, self.pose.delay)
        # elif movement[0] != 0:
        else:
            self.pose = PoseRun(self, self.pose.current_pose, self.pose.current_pose, self.pose.delay)

    def __init__(self, ruta_sprite: str, no_estados: int, no_poses: int, x_coordinate: int, y_coordinate: int,
                 resolucion_x: int, resolucion_y: int, escala: float, color_fondo: (int, int, int)):
        self.frames: list[list[Surface]] = []
        self.previous_pose = 0
        self.current_pose = 0
        self.pose = PoseStatic(self)
        # self.state = StateNeutral(self)
        spriter = SpriteSheet(ruta_sprite)
        for index1 in range(no_estados):
            self.frames.append([])
            for index in range(no_poses):
                self.frames[index1].append(spriter.get_image(
                    index1, index, resolucion_x, resolucion_y, escala, color_fondo))
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

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
        self.pose.move()
        return self.frames[0][self.pose.current_pose]

    def set_state(self, estado: int):
        self.state = estado

    def get_hitbox(self):
        pass

    def set_up(self, coordinate: int):
        pass

    def set_down(self, coordinate: int):
        pass

    def set_left(self, coordinate: int):
        pass

    def set_right(self, coordinate: int):
        pass

    def set_hitbox(self, hitbox: Rect):
        self.x_coordinate = hitbox.x
        self.y_coordinate = hitbox.y

    def update_coordinate(self):
        pass

    def move_position(self, move: [int, int], walls: list[Rect]):
        self.set_hitbox(Colisioner.move_gravity(self.get_hitbox(), walls, move))
        self.update_coordinate()

    def get_x_coordinate(self) -> int:
        return self.x_coordinate

    def get_y_coordinate(self) -> int:
        return self.y_coordinate

    def set_x_coordinate(self, coordinate: int):
        self.x_coordinate = coordinate

    def set_y_coordinate(self, coordinate: int):
        self.y_coordinate = coordinate

    def get_life_points(self) -> int:
        return 0

    def set_life_points(self, damage: int):
        pass