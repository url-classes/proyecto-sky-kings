from pygame import surface
import pygame
import sys
from label import Label
from img import Img
from button import Button


class Options:
    def __init__(self, screen: surface):
        self.screen = screen

    def option_screen(self):
        # buttons
        menu = Button(0, 0, "img/buttons/menu_button.png", "img/buttons/menu_button_pressed.png", self.screen, 6)
        # images
        pixel_label = Label()
        # menu
        img_menu = Img(self.screen)
        while True:
            # add background image
            img_menu.add_img('img/background/menu_bg.png', 0, 0)
            # add 'menu' text on menu
            pixel_label.draw_text(self.screen, "Opciones", (255, 255, 255), 360, 100, 120)
            if menu.draw_button():
                break
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_SPACE:
                        self.screen.fill((0, 0, 0))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(60)
