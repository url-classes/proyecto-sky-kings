import pygame
from pygame import surface


class Button:
    def __init__(self, x: int, y: int, path: str, path2: str, screen: surface, disp: int):
        self.image = []
        self.image.append(pygame.image.load(path).convert_alpha())
        self.image.append(pygame.image.load(path2).convert_alpha())
        self.x: int = x
        self.y: int = y
        self.rect = self.image[0].get_rect()
        self.rect.topleft = (x, y)
        self.screen: surface = screen
        self.clicked: bool = False
        self.disp: int = disp

    def draw_button(self):
        pos = pygame.mouse.get_pos()
        image_index = 0
        disp = 0
        # check mouseiver and clicked conditions
        if self.rect.collidepoint(pos):
            image_index = 1
            disp = self.disp
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                return True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.screen.blit(self.image[image_index], (self.rect.x, self.rect.y + disp))
