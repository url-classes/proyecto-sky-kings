import pygame

class Bar:
    def __init__(self, width, height, max_value, color):
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = max_value
        self.color = color

    def set_value(self, value):
        self.current_value = value
        if self.current_value < 0:
            self.current_value = 0
        elif self.current_value > self.max_value:
            self.current_value = self.max_value

    def draw(self, screen, x, y):
        bar_width = int((self.current_value / self.max_value) * self.width)
        pygame.draw.rect(screen, self.color, (x, y, bar_width, self.height))
