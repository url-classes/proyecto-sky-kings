import pygame
import sys
from label import Label
from img import Img
from button import Button

# init pygame
pygame.init()
# set screen
screen_width = 960
screen_height = 540
pygame.display.set_caption("SKY KINGS")
icon = pygame.image.load("img/background/robot.png")


def play_screen():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    # images
    pixel_label = Label()
    # menu
    img_menu = Img(screen)
    while True:
        # add background image
        img_menu.add_img('img/background/menu_bg.png', 0, 0)
        # add 'menu' text on menu
        pixel_label.draw_text(screen, "jugando", (255, 255, 255), 360, 100, 120)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def options_screen():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    # images
    pixel_label = Label()
    # menu
    img_menu = Img(screen)
    while True:
        # add background image
        img_menu.add_img('img/background/menu_bg.png', 0, 0)
        # add 'menu' text on menu
        pixel_label.draw_text(screen, "Opciones", (255, 255, 255), 360, 100, 120)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


def main_menu():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    # images
    pixel_label = Label()
    # menu
    img_menu = Img(screen)
    # buttons
    play_button = Button(360, 230, "img/buttons/playbutton.png", 1, screen)
    option_button = Button(360, 370, "img/buttons/option_button.png", 1, screen)
    while True:
        # add background image
        img_menu.add_img('img/background/menu_bg.png', 0, 0)
        # add 'menu' text on menu
        pixel_label.draw_text(screen, "MENU", (255, 255, 255), 360, 100, 120)
        # add menu buttons
        # play

        if play_button.draw_button():
            play_screen()
        pixel_label.draw_text(screen, "Jugar", (255, 255, 255), 390, 235, 85)
        # options
        if option_button.draw_button():
           options_screen()
        pixel_label.draw_text(screen, "Opciones", (255, 255, 255), 375, 380, 65)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
main_menu()