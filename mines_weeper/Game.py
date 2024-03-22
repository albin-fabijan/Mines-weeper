import pygame
from .paths import Paths
from .window import Window
from .ClickableSprite import ClickableSprite
from . import Case as C
from .Matrix import Matrix
from .scores import ScoreScreen

class Game(Window):
    def __init__(self, matrix_size, bomb_number_range, difficulty):
        super().__init__(matrix_size * 32, matrix_size * 32 + 64)

        self.matrix_size = matrix_size
        self.bomb_number_range = bomb_number_range
        self.difficulty = difficulty
        self.start_time = pygame.time.get_ticks()

        self.background_image = pygame.image.load("background_ingame.png")
        self.background_image = pygame.transform.scale(self.background_image, (matrix_size * 32 , 64))

        self.not_clicked = pygame.image.load(Paths().select_sprite("grid.png")).convert()

        self.sprite = self.sprite_initialization()

        self.group = self.group_initialization()

<<<<<<< HEAD
        self.matrix = self.matrix_initialization()
=======
        self.matrix = Matrix(
            self.bomb_number_range,
            self.matrix_size,
            self.group
        )

        self.win = False
        self.restart = False

        for i in range(self.matrix.get_matrix_size()):
            for j in range(self.matrix.get_matrix_size()):
                self.group.add(self.matrix.get_case((i,j)).get_sprite())
>>>>>>> feature/timer

        self.final_time = 0

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.start_time = pygame.time.get_ticks()
                        self.sprite = self.sprite_initialization()
                        self.group = self.group_initialization()
                        self.matrix = self.matrix_initialization()

                if self.matrix.check_lose():
                    self.final_time = elapsed_time
                    pygame.time.wait(3000)
                    print("lose")
                    self.running = False
                    self.win = False
                    #ScoreScreen(False , elapsed_time)
                if self.matrix.check_win():
                    self.final_time = elapsed_time
                    pygame.time.wait(3000)
                    print("win")
                    self.running = False
                    self.win = True
                    #ScoreScreen(True , elapsed_time)
                
            self.group.update(events)
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background_image, (0, 0))
            self.group.draw(self.screen)
            elapsed_time = self.display_timer()
            self.display_numbombs()
            self.display_numflags()
            self.display_numinterro()
            pygame.display.flip()
        
        pygame.quit()

        score = ScoreScreen()
        while (not self.restart) :
            restart = score.run(self.final_time, self.difficulty ,self.win)
            if (restart == True) :
                self.restart = True
        print("choose to restart")
    
    def display_timer(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, (0, 0, 0))
        self.screen.blit(timer_text, (5, 10))
        return elapsed_time
    
    def display_numbombs(self):
        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(f"Bombs: {self.num_bombs()- self.num_flags()}", True, (0, 0, 0))
        self.screen.blit(timer_text, (5, 30))
        return

    def display_numflags(self):
        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(f"Flags: {self.num_flags()}", True, (0, 0, 0))
        self.screen.blit(timer_text, (self.matrix_size * 15, 10))
        return
    
    def display_numinterro(self):
        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(f"?: {self.num_interrogations()}", True, (0, 0, 0))
        self.screen.blit(timer_text, (self.matrix_size * 15, 30))
        return

    def num_bombs(self) :
        bombs = 0
        for c in self.matrix.get_cases() :
            if (c.bomb) :
                bombs += 1
        return bombs
    
    def num_flags(self) :
        flags = 0
        for c in self.matrix.get_cases() :
            if (c.flag == 1) :
                flags += 1
        return flags
    
    def num_interrogations(self) :
        interro = 0
        for c in self.matrix.get_cases() :
            if (c.flag == 2) :
                interro += 1
        return interro

    def on_left_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("empty.png")).convert()

    def on_right_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("flag.png")).convert()

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
        matrix = Matrix(
            self.bomb_number_range,
            self.matrix_size,
            self.group
        )

        for i in range(matrix.get_matrix_size()):
            for j in range(matrix.get_matrix_size()):
                self.group.add(matrix.get_case((i,j)).get_sprite())

        return matrix