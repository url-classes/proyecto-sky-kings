from abc import ABCMeta, abstractmethod
from pygame import Rect


class CharacterPose(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        raise NotImplementedError
