import sys
import json

import pygame

from .paths import Paths
from .window import Window


class ScoreScreen(Window):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__(WIDTH, HEIGHT)

        self.SCREEN_WIDTH = WIDTH
        self.SCREEN_HEIGHT = HEIGHT
        pygame.display.set_caption("Affichage des Scores")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BROWN = (200, 173, 127)
        self.BEIGE = (63, 34, 4)

        self.font = pygame.font.SysFont(None, 40)

    def display_score(self, timer):
        # Loading background image 
        self.screen.fill(self.BROWN)
        image = pygame.image.load(
                Paths().select_sprite("menu_background.png")
        )
        background_img = pygame.image.load(
                Paths().select_sprite("menu_background.png")
        )
        background_img = pygame.transform.scale(
                background_img,
                (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )

        # Loading score buttons 
        button_img = pygame.image.load(Paths().select_sprite('button.png'))
        button_img = pygame.transform.scale(button_img, (450, 100))

        # Score display 
        text_score = self.font.render(
                f"Votre timer: {timer}",
                True,
                self.BLACK
        )
        score_rect = text_score.get_rect(
                center=(
                    button_img.get_width() // 2,
                    button_img.get_height() // 2
            )
        )
        button_img.blit(text_score, score_rect)

        # Background image display 
        self.screen.blit(background_img, (0, 0))

        # Display buttons
        self.screen.blit(
                button_img,
                (self.SCREEN_WIDTH // 2 - button_img.get_width() // 2, 50)
        )

        # Display restart button with text 
        restart_button_img = pygame.image.load(
            Paths().select_sprite('select.png')
        )
        restart_button_img = pygame.transform.scale(
                restart_button_img,
                (200, 100)
        )
        restart_text = self.font.render("Recommencer", True, self.BEIGE)
        restart_rect = restart_text.get_rect(
            center=(
                    restart_button_img.get_width() // 2,
                    restart_button_img.get_height() // 2
            )
        )
        restart_button_img.blit(restart_text, restart_rect)
        self.screen.blit(
                restart_button_img,
                (self.SCREEN_WIDTH - 250, self.SCREEN_HEIGHT - 150)
        )

        # Display quit button with text 
        quit_button_img = pygame.image.load(
                Paths().select_sprite('select.png')
        )
        quit_button_img = pygame.transform.scale(quit_button_img, (200, 100))
        quit_text = self.font.render("Quitter", True, self.BEIGE)
        quit_rect = quit_text.get_rect(
            center=(
                    quit_button_img.get_width() // 2,
                    quit_button_img.get_height() // 2
            )
        )
        quit_button_img.blit(quit_text, quit_rect)
        self.screen.blit(quit_button_img, (50, self.SCREEN_HEIGHT - 150))

        pygame.display.flip()

    def display_result_and_difficulty(self, result, niveau):
        result_text = "Gagné !" if result else "Perdu..."
        if niveau == 1:
            niveau_text = f"difficulté: facile"
        elif niveau == 2:
            niveau_text = f"difficulté: normale"
        elif niveau == 3:
            niveau_text = f"difficulté: difficile"
        
        result_font = pygame.font.SysFont(None, 60)
        result_surface = result_font.render(result_text, True, self.BLACK)
        result_rect = result_surface.get_rect(
            center=(
                self.SCREEN_WIDTH // 2,
                self.SCREEN_HEIGHT // 4 + 20
            )
        )

        niveau_font = pygame.font.SysFont(None, 40)
        niveau_surface = niveau_font.render(niveau_text, True, self.BLACK)
        niveau_rect = niveau_surface.get_rect(
            center=(
                    self.SCREEN_WIDTH // 2,
                    self.SCREEN_HEIGHT // 4 + 70
            )
        )
        
        self.screen.blit(result_surface, result_rect)
        self.screen.blit(niveau_surface, niveau_rect)
        pygame.display.flip()

    def save_time_in_json(self, timer):
        data = {"timer": timer}
        with open("save.json", "a") as json_file:
            json.dump(data, json_file)
            json_file.write("\n")

    def run(self, game_timer, level, game_result):
        timer = game_timer
        niveau = level
        result = game_result

        self.display_score(timer)
        self.display_result_and_difficulty(result, niveau)

        self.save_time_in_json(timer)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if (
                        50 <= mouse_pos[0] <= 250
                        and (
                            self.SCREEN_HEIGHT - 150
                            <= mouse_pos[1]
                            <= self.SCREEN_HEIGHT - 50
                        )
                    ):
                        pygame.quit()
                        sys.exit()
                    elif (
                            (
                                self.SCREEN_WIDTH - 250
                                <= mouse_pos[0]
                                <= self.SCREEN_WIDTH - 50
                        )
                            and (
                                self.SCREEN_HEIGHT - 150
                                <= mouse_pos[1]
                                <= self.SCREEN_HEIGHT - 50
                        )
                    ):
                        pygame.quit()
                        return True
