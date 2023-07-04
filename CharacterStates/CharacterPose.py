from abc import ABCMeta, abstractmethod


class CharacterPose(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        raise NotImplementedError
