import pygame
import sys

from . import paths
from .window import Window


# Couleurs
class SelectMenu(Window):
    def __init__(self):
        super().__init__(350, 350)

        self.DARK = (0, 0, 0)
        self.BRUN = (200, 173, 127)

        self.background_img, self.button_img = self.load_images()

        self.difficulty = self.main_loop()
        print("Difficulté sélectionnée :", self.difficulty)

    def load_images(self):
        image = pygame.image.load(paths.select_sprite("menu_background.png"))
        scale = image.get_size()
        background_img = pygame.transform.scale(image , (350,350))

        # Chargement des images des boutons
        image = pygame.image.load(paths.select_sprite("button.png"))
        scale = image.get_size()
        button_img = pygame.transform.scale(image , (int(scale [0] * 2), int(scale [1]* 2)))

        return background_img, button_img

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Récupérer les coordonnées de la souris au moment du clic
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Vérifier si le clic est sur un des boutons
                    if easy_button_rect.collidepoint(mouse_x, mouse_y):
                        return 1
                    elif normal_button_rect.collidepoint(mouse_x, mouse_y):
                        return 2
                    elif expert_button_rect.collidepoint(mouse_x, mouse_y):
                        return 3

            # Dessiner l'arrière-plan
            self.screen.fill(self.BRUN)
            self.screen.blit(self.background_img, (0, 0))

            # Dessiner les boutons
            easy_button_rect = self.button_img.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 - 50))
            self.screen.blit(self.button_img, easy_button_rect)
            self.draw_text("Facile", self.font, self.DARK, self.screen, self.WIDTH//2, self.HEIGHT//2 - 50)

            normal_button_rect = self.button_img.get_rect(center=(self.WIDTH//2, self.HEIGHT//2))
            self.screen.blit(self.button_img, normal_button_rect)
            self.draw_text("Normal", self.font, self.DARK, self.screen, self.WIDTH//2, self.HEIGHT//2)

            expert_button_rect = self.button_img.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + 50))
            self.screen.blit(self.button_img, expert_button_rect)
            self.draw_text("Expert", self.font, self.DARK, self.screen, self.WIDTH//2, self.HEIGHT//2 + 50)

            # Mettre à jour l'affichage
            pygame.display.flip()