import pygame


class Screen:
    def __init__(self, width: int, heigth: int, titulo: str, color: (int, int, int)):
        self.width = width
        self.heigth = heigth
        self.view = pygame.display.set_mode((self.width, self.heigth))
        self.titulo = titulo
        self.color = color
        pygame.display.set_caption(self.titulo)

    def set_width(self, width: int):
        self.width = width
        self.view = pygame.display.set_mode((self.width, self.heigth))

    def set_heigth(self, heigth: int):
        self.heigth = heigth
        self.view = pygame.display.set_mode((self.width, self.heigth))

    def set_title(self, title: str):
        self.titulo = title
        pygame.display.set_caption(self.titulo)

    def fondear(self):
        self.view.fill(self.color)

