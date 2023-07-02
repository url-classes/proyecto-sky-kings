from abc import ABC, abstractmethod


class PlatformType(ABC):
    @abstractmethod
    def can_pass_through(self):
        pass
