from i_platform import Platform
from pygame import Surface
from img import Img


class CollidePlatform(Platform):
    def __init__(self, path: str, screen: Surface, walls: list[list[int]]):
        self.path = path
        self.screen = screen
        self.walls = walls

    def draw_platform(self, vel: int):
        img = Img(self.screen)
        for wall in self.walls:
            # rectangle = pygame.draw.rect(self.screen, (0, 0, 0), pared)
            wall[1] += vel
            if not self.path == '':
                img.add_img(self.path, wall[0] - 10, wall[1], 1, 1)
