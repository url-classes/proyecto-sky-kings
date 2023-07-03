import pygame


class HealthBar:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.max_health = 100
        self.current_health = 50
        self.health_color = (0, 255, 255)  # Color de la barra de salud

    def set_health(self, health):
        self.current_health = health

    def decrease_health(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0

    def increase_health(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, (255, 0, 0),
                         (x, y, self.width, self.height))  # Dibujar el contorno de la barra de salud
        health_width = int((self.current_health / self.max_health) * self.width)
        pygame.draw.rect(screen, self.health_color,
                         (x, y, health_width, self.height))  # Dibujar la barra de salud actual
