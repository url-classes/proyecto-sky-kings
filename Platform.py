from pygame import Surface


class Platform:
    def __init__(self, screen: Surface, path: str, walls):
        self.screen = screen
        self.path = path
        self.walls = walls
