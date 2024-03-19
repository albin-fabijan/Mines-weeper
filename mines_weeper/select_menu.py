import sys

import pygame

from . import paths
from .window import Window


class SelectMenu(Window):
    def __init__(self):
        super().__init__(350, 350)
        pygame.display.set_caption("Menu de Sélection de Difficulté")
        self.font = pygame.font.Font(None, 36)

        self.main_loop()

    def main_loop(self):
        while self.running:
            easy_button_rect, normal_button_rect, expert_button_rect = self.get_rects()
            self.input_loop(easy_button_rect, normal_button_rect, expert_button_rect)
            self.display(easy_button_rect, normal_button_rect, expert_button_rect)

    def load_images(self):
        image = pygame.image.load(paths.select_sprite("menu_background.png"))
        scale = image.get_size()
        background_img = pygame.transform.scale(image , (350,350))

        image = pygame.image.load(paths.select_sprite("button.png"))
        scale = image.get_size()
        button_img = pygame.transform.scale(image , (int(scale [0] * 2), int(scale [1]* 2)))

        return background_img, button_img

    def get_rects(self):
        background_img, button_img = self.load_images()

        easy_button_rect = button_img.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 - 50))
        normal_button_rect = button_img.get_rect(center=(self.WIDTH//2, self.HEIGHT//2))
        expert_button_rect = button_img.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + 50))

        return easy_button_rect, normal_button_rect, expert_button_rect

    def input_loop(self, easy_button_rect, normal_button_rect, expert_button_rect):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if easy_button_rect.collidepoint(mouse_x, mouse_y):
                    print("Difficulté sélectionnée : 1")
                    self.running = False
                    break
                elif normal_button_rect.collidepoint(mouse_x, mouse_y):
                    print("Difficulté sélectionnée : 1")
                    self.running = False
                    break
                elif expert_button_rect.collidepoint(mouse_x, mouse_y):
                    print("Difficulté sélectionnée : 1")
                    self.running = False
                    break

    def display(self, easy_button_rect, normal_button_rect, expert_button_rect):
        DARK = (0, 0, 0)
        BRUN = (200, 173, 127)

        background_img, button_img = self.load_images()

        self.screen.fill(BRUN)
        self.screen.blit(background_img, (0, 0))

        self.screen.blit(button_img, easy_button_rect)
        self.draw_text("Facile", self.font, DARK, self.screen, self.WIDTH//2, self.HEIGHT//2 - 50)

        self.screen.blit(button_img, normal_button_rect)
        self.draw_text("Normal", self.font, DARK, self.screen, self.WIDTH//2, self.HEIGHT//2)

        self.screen.blit(button_img, expert_button_rect)
        self.draw_text("Expert", self.font, DARK, self.screen, self.WIDTH//2, self.HEIGHT//2 + 50)

        pygame.display.flip()