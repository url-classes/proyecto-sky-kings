import pygame
import sys
from label import Label
from img import Img
from button import Button
from progress_bar import ProgressBar
from select_character import SelectCharacter
from options import Options

# init pygame
pygame.init()
# set screen
screen_width = 960
screen_height = 540
progress_bar = ProgressBar(screen_width, screen_height, (0, 0, 0), (0, 0, 255), (255, 255, 255), "Sounds/gun.wav")
progress_bar.run()
pygame.display.set_caption("SKY KINGS")
icon = pygame.image.load("img/background/robot.png")


def main_menu():
    pygame.mixer.music.load('Sounds/playing-instant-long-154860.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    # images
    pixel_label = Label()
    # menu
    img_menu = Img(screen)
    # buttons
    play_button = Button(360, 230, "img/buttons/playbutton.png", "img/buttons/playbutton_pressed.png",
                         screen, 15, 1, 1, "Jugar", 85, 25, 10)
    option_button = Button(360, 370, "img/buttons/option_button.png", "img/buttons/option_button_pressed.png",
                           screen, 16, 1, 1, "Opciones", 65, 15, 10)
    play = SelectCharacter(screen)
    options = Options(screen)
    while True:
        # add background image
        img_menu.add_img('img/background/menu_bg.png', 0, 0, 1, 1)
        # add 'menu' text on menu
        pixel_label.draw_text(screen, "MENU", (255, 255, 255), 360, 100, 120)
        # add menu buttons
        # play

        if play_button.draw_button():
            pygame.mixer.music.pause()
            play.play_screen()
        # options
        if option_button.draw_button():
            options.option_screen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(40)


main_menu()
