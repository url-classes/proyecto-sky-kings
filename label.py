from pygame import surface
import pygame


class Label:
    def __init__(self):
        self.font = pygame.font.Font("files/aansa.ttf", 120)

    def draw_text(self, screen: surface, text, text_col, x, y, size):
        self.font = pygame.font.Font("files/aansa.ttf", size)
        img = self.font.render(text, True, text_col)
        return screen.blit(img, (x, y))
