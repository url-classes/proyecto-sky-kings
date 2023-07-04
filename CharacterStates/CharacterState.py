from abc import ABCMeta, abstractmethod


class CharacterState(metaclass=ABCMeta):
    @abstractmethod
    def get_actual_frame(self):
        raise NotImplementedError
