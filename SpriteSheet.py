import pygame
from pygame import Surface


class SpriteSheet:
    def __init__(self, ruta_imagen: str):
        self.ruta_imagen = pygame.image.load(ruta_imagen).convert_alpha()

    def get_image(self, frame1: int, frame: int, width: int, heigth: int, scale: float, color: (int, int, int)):
        image = pygame.Surface((width, heigth)).convert_alpha()
        image.blit(self.ruta_imagen, (0, 0), ((frame * width), (frame1 * heigth), width, heigth))
        image = pygame.transform.scale(image, (width * scale, heigth * scale))
        image.set_colorkey(color)
        return image
