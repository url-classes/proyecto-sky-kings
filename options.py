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
        menu = Button(0, 0, "img/buttons/menu_button.png",
                      "img/buttons/menu_button_pressed.png", self.screen, 6, 1, 1, '', 0, 0, 0)
        # images
        pixel_label = Label()

        # menu
        img_menu = Img(self.screen)
        while True:
            # add background image
            img_menu.add_img('img/background/menu_bg.png', 0, 0, 1, 1)
            # add 'menu' text on menu
            pixel_label.draw_text(self.screen, "Instrucciones", (255, 255, 255), 200, 100, 120)
            pixel_label.draw_text(self.screen, "Jugador 1", (255, 255, 255), 70, 210, 80)
            pixel_label.draw_text(self.screen, "Tecla W: Arriba ", (255, 255, 255), 50, 280, 60)
            pixel_label.draw_text(self.screen, "Tecla A: Abajo ", (255, 255, 255), 50, 320, 60)
            pixel_label.draw_text(self.screen, "Tecla S: Izquierda ", (255, 255, 255), 50, 360, 60)
            pixel_label.draw_text(self.screen, "Tecla D: Derecha ", (255, 255, 255), 50, 400, 60)
            pixel_label.draw_text(self.screen, "Tecla G: Golpe ", (255, 255, 255), 50, 440, 60)
            pixel_label.draw_text(self.screen, "Jugador 2", (255, 255, 255), 550, 210, 80)
            pixel_label.draw_text(self.screen, "Mover con flechas", (255, 255, 255), 530, 280, 60)
            pixel_label.draw_text(self.screen, "del teclado. ", (255, 255, 255), 530, 320, 60)
            pixel_label.draw_text(self.screen, "Tecla K: Golpe ", (255, 255, 255), 530, 360, 60)
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
