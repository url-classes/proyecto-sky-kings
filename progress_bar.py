import sys
import pygame
from bar import Bar

class ProgressBar(Bar):
    def __init__(self, width, height, background_color, bar_color, text_color, sound_file):
        super().__init__(width, height, 100, bar_color)
        self.background_color = background_color
        self.text_color = text_color
        self.sound_file = sound_file

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        # fuente del texto
        self.font = pygame.font.Font("files/aansa.ttf", 40)

        # cargar sonindo
        pygame.mixer.init()
        self.start_sound = pygame.mixer.Sound(self.sound_file)

    def show(self, progress):
        bar_width = 300
        bar_height = 30
        bar_x = (self.width - bar_width) // 2
        bar_y = (self.height - bar_height) // 2
        progress_width = progress * bar_width

        # Dibujar el fondo
        self.screen.fill(self.background_color)

        # Dibujar la barra de carga vacía
        pygame.draw.rect(self.screen, self.color, (bar_x, bar_y, bar_width, bar_height), 2)

        # Dibujar la barra de progreso
        pygame.draw.rect(self.screen, self.color, (bar_x, bar_y, progress_width, bar_height))

        text = self.font.render("Loading...", True, self.text_color)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(text, text_rect)

        # Actualizar la pantalla
        pygame.display.flip()

    def run(self):
        self.play_start_sound()
        loading_progress = 0.0
        while loading_progress <= 1.0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Simulación de carga
            loading_progress += 0.01

            # Mostrar la barra de carga
            self.show(loading_progress)

            # Controlar la velocidad de actualización
            self.clock.tick(30)

    def play_start_sound(self):
        self.start_sound.play()
