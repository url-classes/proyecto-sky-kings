import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, platform_type):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        new_width = self.original_image.get_width() * 3 // 4  # Reducing width to 3/4
        new_height = self.original_image.get_height() * 3 // 4  # Reducing height to 3/4
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.platform_type = platform_type

    def update_vertical_position(self, new_y):
        self.rect.y = new_y

    def can_pass_through(self):
        return self.platform_type.can_pass_through()
