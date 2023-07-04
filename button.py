import pygame
from pygame import surface
from label import Label


class Button:
    def __init__(self, x: int, y: int, path: str, path2: str, screen: surface,
                 disp: int, scale_x: float, scale_y: float, text: str, size: int, x_text: int, y_text: int):
        self.image = []
        self.image.append(pygame.image.load(path).convert_alpha())
        self.image.append(pygame.image.load(path2).convert_alpha())
        width = self.image[0].get_width()
        height = self.image[1].get_height()
        self.image[0] = pygame.transform.scale(self.image[0], (int(scale_x * width), int(scale_y * height)))
        self.image[1] = pygame.transform.scale(self.image[1], (int(scale_x * width), int(scale_y * height)))
        self.x: int = x
        self.y: int = y
        self.rect = self.image[0].get_rect()
        self.rect.topleft = (x, y)
        self.screen: surface = screen
        self.clicked: bool = False
        self.disp: int = disp
        self.text: str = text
        self.label: Label = Label()
        self.size = size
        self.x_text = x_text
        self.y_text = y_text

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
            self.label.draw_text(self.screen, self.text, (255, 255, 255),  self.rect.x+self.x_text,
                                 self.rect.y + disp+self.y_text, self.size)
