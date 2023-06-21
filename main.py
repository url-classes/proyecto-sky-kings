import pygame
import sys
from label import Label
from img import Img
import button

# init pygame
pygame.init()
# set screen
screen_width = 960
screen_height = 540
pygame.display.set_caption("SKY KINGS")
icon = pygame.image.load("img/background/robot.png")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# images
pixel_label = Label()
#menu bg
img_menu = Img(screen)
# buttons
play_button = Img(screen)
option_button = Img(screen)
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # add background image
    img_menu.add_img('img/background/menu_bg.png', 0, 0)
    # add 'menu' text on menu
    pixel_label.draw_text(screen, "MENU", (255, 255, 255), 360, 130, 120)
    # add menu buttons
    # play
    play_button.add_img("img/buttons/playbutton.png", 360, 260)
    pixel_label.draw_text(screen, "PLAY", (255, 255, 255), 380, 270, 100)
    # options
    option_button.add_img("img/buttons/option_button.png", 360, 400)
    pixel_label.draw_text(screen, "Options", (255, 255, 255), 375, 410, 75)
    pygame.display.update()
    clock.tick(60)

