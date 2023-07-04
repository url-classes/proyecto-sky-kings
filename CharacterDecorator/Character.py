from abc import ABCMeta, abstractmethod
from pygame import Surface, Rect


class Character(metaclass=ABCMeta):
    @abstractmethod
    def update_pose(self):
        raise NotImplementedError

    @abstractmethod
    def get_actual_frame(self) -> Surface:
        raise NotImplementedError

    @abstractmethod
    def set_state(self, estado: int):
        raise NotImplementedError

    @abstractmethod
    def get_hitbox(self) -> Rect:
        raise NotImplementedError

    @abstractmethod
    def set_up(self, coordinate: int):
        raise NotImplementedError

    @abstractmethod
    def set_down(self, coordinate: int):
        raise NotImplementedError

    @abstractmethod
    def set_left(self, coordinate: int):
        raise NotImplementedError

    @abstractmethod
    def set_right(self, coordinate: int):
        raise NotImplementedError

    @abstractmethod
    def set_hitbox(self, hitbox: Rect):
        raise NotImplementedError

    @abstractmethod
    def update_coordinate(self):
        raise NotImplementedError

    @abstractmethod
    def move(self, walls: list[Rect], movement: [int, int] = None):
        raise NotImplementedError

    @abstractmethod
    def get_x_coordinate(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_y_coordinate(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def set_x_coordinate(self, coordinate: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def set_y_coordinate(self, coordinate: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_life_points(self) -> int:
        raise NotImplementedError

