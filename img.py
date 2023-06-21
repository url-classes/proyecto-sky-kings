from pygame import surface
import pygame


class Img:
    def __init__(self, screen: surface):
        self.screen: surface = screen
        self.img: surface = None
    def add_img(self, path, x, y):
        self.img = pygame.image.load(path)
        self.screen.blit(self.img, (x, y))
