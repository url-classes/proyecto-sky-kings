from pygame import surface
import pygame


class Img:
    def __init__(self, screen: surface):
        self.screen: surface = screen
        self.img: surface = None

    def add_img(self, path: str, x: int, y: int, scale_x: float, scale_y: float):
        self.img = pygame.image.load(path)
        width = self.img.get_width()
        height = self.img.get_height()
        self.img = pygame.transform.scale(self.img, (int(scale_x * width), int(scale_y * height)))
        self.screen.blit(self.img, (x, y))
        return self.img
