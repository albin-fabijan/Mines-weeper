import sys

import pygame

from .Paths import Paths
from .Window import Window
from .ClickableSprite import ClickableSprite
from .Matrix import Matrix
from .ScoreScreen import ScoreScreen

class Game(Window):
    def __init__(self, matrix_size, bomb_number_range, difficulty):
        super().__init__(matrix_size * 32, matrix_size * 32 + 64)

        self.matrix_size = matrix_size
        self.bomb_number_range = bomb_number_range
        self.difficulty = difficulty
        self.start_time = 0
        self.game_started = False

        self.background_image = pygame.image.load(
                Paths().select_sprite("background_ingame.png")
        )
        self.background_image = pygame.transform.scale(
                self.background_image,
                (matrix_size * 32 , 64)
        )

        self.not_clicked = pygame.image.load(
                Paths().select_sprite("Grid.png")
        ).convert()

        self.sprite = self.sprite_initialization()
        self.group = self.group_initialization()
        self.matrix = self.matrix_initialization()

        self.restart = False
        self.final_time = 0

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if restart_button_rect.collidepoint(mouse_x, mouse_y):
                        self.start_time = 0
                        self.game_started = False
                        self.sprite = self.sprite_initialization()
                        self.group = self.group_initialization()
                        self.matrix = self.matrix_initialization()

                if self.matrix.check_lose():
                    self.final_time = elapsed_time
                    pygame.time.wait(2000)
                    self.running = False
                    self.win = False

                if self.matrix.check_win():
                    self.final_time = elapsed_time
                    pygame.time.wait(1000)
                    self.running = False
                    self.win = True

            if not self.matrix.get_first_click() and not self.game_started:
                self.start_time = pygame.time.get_ticks()
                self.game_started = True
                
            self.group.update(events)

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background_image, (0, 0))
            self.group.draw(self.screen)

            elapsed_time = self.display_timer()
            self.display_bomb_number()
            self.display_flag_number()
            self.display_question_number()

            button_img, restart_button_rect = self.get_restart_button()
            self.screen.blit(button_img, restart_button_rect)
            self.draw_text(
                "R",
                pygame.font.Font(None, 16),
                (0, 0, 0),
                self.screen,
                self.WIDTH - 24,
                48
            )

            pygame.display.flip()
        
        pygame.quit()

        score = ScoreScreen(800, 600)
        while not self.restart:
            restart = score.run(self.final_time, self.difficulty ,self.win)
            if (restart == True):
                self.restart = True
    
    def display_timer(self):
        if self.matrix.get_first_click() == True:
            elapsed_time = 0
        else:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(
                f"Time: {minutes:02}:{seconds:02}",
                True,
                (0, 0, 0)
        )
        self.screen.blit(timer_text, (5, 10))
        return elapsed_time
    
    def display_bomb_number(self):
        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(
                f"Bombs: {self.bomb_number()- self.flag_number()}",
                True,
                (0, 0, 0)
        )
        self.screen.blit(timer_text, (5, 30))
        return

    def display_flag_number(self):
        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(
                f"Flags: {self.flag_number()}",
                True,
                (0, 0, 0)
        )
        self.screen.blit(timer_text, (self.matrix_size * 15, 10))
        return
    
    def display_question_number(self):
        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(
                f"?: {self.question_number()}",
                True,
                (0, 0, 0)
        )
        self.screen.blit(timer_text, (self.matrix_size * 15, 30))
        return

    def bomb_number(self):
        bombs = 0
        for c in self.matrix.get_cases() :
            if (c.bomb) :
                bombs += 1
        return bombs
    
    def flag_number(self):
        flags = 0
        for c in self.matrix.get_cases() :
            if (c.flag == 1) :
                flags += 1
        return flags
    
    def question_number(self):
        interro = 0
        for c in self.matrix.get_cases() :
            if (c.flag == 2) :
                interro += 1
        return interro

    def on_left_click(self):
        sprite.image = pygame.image.load(
                Paths().select_sprite("empty.png")
        ).convert()

    def on_right_click(self):
        sprite.image = pygame.image.load(
                Paths().select_sprite("flag.png")
        ).convert()

    def get_restart_button(self):
        image = pygame.image.load(Paths().select_sprite("select.png"))
        scale = image.get_size()
        button_img = pygame.transform.scale(
            image,
            (24, 24)
        )

        restart_button_rect = button_img.get_rect(
            center = (
                self.WIDTH - 24,
                48
            )
        )
        return button_img, restart_button_rect

    def sprite_initialization(self):
        sprite = ClickableSprite(
            self.not_clicked,
            50,
            50,
            self.on_left_click,
            self.on_right_click
        )

        return sprite

    def group_initialization(self):
        group = pygame.sprite.Group(self.sprite)
        group.remove(self.sprite)

        return group

    def matrix_initialization(self):
        matrix = Matrix(self.bomb_number_range, self.matrix_size, self.group)

        for i in range(matrix.get_matrix_size()):
            for j in range(matrix.get_matrix_size()):
                self.group.add(matrix.get_case((i,j)).get_sprite())

        return matrix
