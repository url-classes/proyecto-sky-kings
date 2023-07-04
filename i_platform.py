from abc import ABCMeta, abstractmethod


class Platform(metaclass=ABCMeta):
    @abstractmethod
    def draw_platform(self, vel: int):
        raise NotImplementedError
