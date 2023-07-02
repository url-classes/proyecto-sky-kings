import pygame
import sys
from pygame import *
from Colisioner import Colisioner
from img import Img
from platform import Platform
from scrollmap import ScrollMap
from CharacterDecorator.SpriteCharacter import SpriteCharacter
from CharacterDecorator.HorizontalCharacter import HorizontalCharacter
from CharacterDecorator.VerticalCharacter import VerticalCharacter
from CharacterDecorator.ControlCharacter import ControlCharacter


class Play:
    def __init__(self, screen: surface):
        self.screen = screen

    def play_screen(self, character1_path: str, character2_path: str):
        # Game Soundtrack
        pygame.mixer.music.load('Sounds/epic-dramatic-action-trailer-99525.mp3')
        pygame.mixer.music.play(3)

        # Auxiliary Variables
        back_ground_color = (0, 0, 0)
        clock = pygame.time.Clock()

        # Game Characters and Elements
        # Declaration of game characters
        personaje = SpriteCharacter(character1_path, 3, 7, 1024, 1024, 0.1, back_ground_color)
        personaje1 = SpriteCharacter(character2_path, 3, 7, 1024, 1024, 0.1, back_ground_color)
        personaje = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje)), K_w, K_s, K_a, K_d)
        personaje1 = ControlCharacter(VerticalCharacter(HorizontalCharacter(personaje1)), K_UP, K_DOWN, K_LEFT, K_RIGHT)
        paredes = [pygame.Rect(0, 350, 50, 50), pygame.Rect(260, 350, 50, 50)]
        up = down = left = rigth = False
        distancia_salto = 0
        doble_salto = True
        index = 0
        img_menu = Img(self.screen)

        # Variables for map scrolling
        map_y_position = -1080
        bottom_map = False
        time_until_touch_bottom = 0

        # Platform information
        platforms = []
        platform_positions = [(50, 175), (250, 275), (450, 375), (650, 75), (150, 425),
                              (350, 125), (550, 225), (750, 325), (200, 25), (400, 475)]
        for position in platform_positions:
            platform = Platform(position[0], position[1], "img/map/platform(0.2).png")
            platforms.append(platform)

        while True:
            # Character movements
            eventos = pygame.event.get()
            personaje.control_move(eventos)
            personaje1.control_move(eventos)
            personaje.move(paredes)
            personaje1.move(paredes)
            for pared in paredes:
                pygame.draw.rect(self.screen, (255, 0, 0), pared)

            # map movement
            # Load map image
            if not bottom_map:
                img_menu.add_img('img/map/map.png', 0, map_y_position, 1, 1)
                for platform in platforms:
                    self.screen.blit(platform.image, platform.rect)

            # Check if characters touch the ground before moving the map and platforms
            if Colisioner.tocar_suelo(personaje.get_hitbox(), paredes):
                if not bottom_map:
                    time_until_touch_bottom = pygame.time.get_ticks()
                bottom_map = True

            # Flag to activate MapScroll
            if bottom_map:
                # Map Scroll
                scroll_info = ScrollMap()
                tiempo: int = int((pygame.time.get_ticks() - time_until_touch_bottom)/40)
                # Update Scroll information
                if scroll_info.get_scroll() < tiempo*2:
                    scroll_info.update_scroll(tiempo*2)
                img_menu.add_img('img/map/map.png', 0, map_y_position, 1, 1)
                # Plataforms
                for platform in platforms:
                    self.screen.blit(platform.image, platform.rect)
                    if platform.rect.y > 540:
                        platform.update_vertical_position(0)
                    else:
                        platform.update_vertical_position(platform.rect.y + 3)  # Move platforms down by 3px
                if -1080 + scroll_info.get_scroll() <= 0:
                    map_y_position = -1080 + scroll_info.get_scroll()  # Reposition platforms when reaching the bottom

            if index == 10:
                # Change character sprites
                personaje.update_pose()
                personaje1.update_pose()

            # Draw characters on screen
            self.screen.blit(personaje.get_actual_frame(),
                             (personaje.get_x_coordinate(), personaje.get_y_coordinate()))
            self.screen.blit(personaje1.get_actual_frame(),
                             (personaje1.get_x_coordinate(), personaje1.get_y_coordinate()))

            # Quit the game
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if index < 10:
                index += 1
            else:
                index = 0
            pygame.display.update()
            clock.tick(40)
