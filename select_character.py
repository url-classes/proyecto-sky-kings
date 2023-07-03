from pygame import surface
import pygame
import sys
from label import Label
from img import Img
from button import Button
from play import Play


class SelectCharacter:
    def __init__(self, screen: surface):
        self.screen = screen

    def play_screen(self):
        pygame.mixer.music.load('Sounds/punch.mp3')
        pygame.mixer.music.play()
        # buttons
        menu = Button(5, 0, "img/buttons/menu_button.png", "img/buttons/menu_button_pressed.png",
                      self.screen, 6, 1, 1, '', 1, 0, 0)
        character1_button = Button(350, 355, "img/characters/character1_frame.png",
                                   "img/characters/character1_frame_selected.png", self.screen, 0, 3, 3, '', 1, 0, 0)
        character2_button = Button(450, 355, "img/characters/character2_frame.png",
                                   "img/characters/character2_frame_selected.png", self.screen, 0, 3, 3, '', 1, 0, 0)
        character3_button = Button(550, 355, "img/characters/character3_frame.png",
                                   "img/characters/character3_frame_selected.png", self.screen, 0, 3, 3, '', 1, 0, 0)
        play_button = Button(390, 440, "img/buttons/playbutton.png", "img/buttons/playbutton_pressed.png",
                             self.screen, 15, 0.75, 0.75, 'Empezar', 50, 15, 10)
        # images
        pixel_label = Label()
        player1_label = Label()
        player2_label = Label()
        # menu
        img_menu = Img(self.screen)
        player1_character = ''
        player2_character = ''
        character1_bool = False
        character2_bool = False
        character3_bool = False
        while True:

            # add background image
            img_menu.add_img('img/background/select_character_bg.png', 0, 0, 1, 1)
            # add 'menu' text on menu
            pixel_label.draw_text(self.screen, "Seleccion de personaje", (255, 255, 255), 250, 60, 60)
            player1_label.draw_text(self.screen, "Jugador1", (255, 255, 255), 90, 380, 60)
            player2_label.draw_text(self.screen, "Jugador2", (255, 255, 255), 650, 380, 60)
            if character1_button.draw_button():
                character1_bool = True
                if player1_character == '':
                    player1_character = 'img/characters/personaje 1.png'
                else:
                    player2_character = 'img/characters/personaje 1.png'
            if character2_button.draw_button():
                character2_bool = True
                if player1_character == '':
                    player1_character = 'img/characters/personaje 2.png'
                else:
                    player2_character = 'img/characters/personaje 2.png'
            if character3_button.draw_button():
                character3_bool = True
                if player1_character == '':
                    player1_character = 'img/characters/personaje 3.png'
                else:
                    player2_character = 'img/characters/personaje 3.png'
            if character1_bool:
                pos_x = 600
                if player1_character == 'img/characters/personaje 1.png':
                    pos_x = 30
                img_menu.add_img('img/characters/character1_animation.gif', pos_x, 90, 10, 10)
            if character2_bool:
                pos_x = 600
                if player1_character == 'img/characters/personaje 2.png':
                    pos_x = 30
                img_menu.add_img('img/characters/character2_animation.gif', pos_x, 90, 10, 10)
            if character3_bool:
                pos_x = 600
                if player1_character == 'img/characters/personaje 3.png':
                    pos_x = 30
                img_menu.add_img('img/characters/character3_animation.gif', pos_x, 90, 10, 10)

            if play_button.draw_button():
                print("Jugando")
                pygame.mixer.music.pause()
                play = Play(self.screen)
                if player1_character != '':
                    play.play_screen(player1_character, player2_character)
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