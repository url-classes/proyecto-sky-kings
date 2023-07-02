import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() // 1,
                                                                  self.original_image.get_height() // 1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_vertical_position(self, new_y):
        self.rect.y = new_y