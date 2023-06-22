import pygame
from pygame import surface


class Button:
    def __init__(self, x: int, y: int, path: str, scale: float, screen: surface):

        self.image = pygame.image.load(path).convert_alpha()
        width: int = self.image.get_width()
        height: int = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.x: int = x
        self.y: int = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen: surface = screen
        self.clicked: bool = False

    def draw_button(self):
        pos = pygame.mouse.get_pos()
        # check mouseiver and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
