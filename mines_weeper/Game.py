import pygame
from .paths import Paths
from .window import Window
from .ClickableSprite import ClickableSprite
from . import Case as C
from .Matrix import Matrix
#from .scores import scores

class Game(Window):
    def __init__(self, matrix_size, bomb_number_range):
        super().__init__(matrix_size * 32, matrix_size * 32 + 64)

        self.matrix_size = matrix_size
        self.bomb_number_range = bomb_number_range
        self.start_time = pygame.time.get_ticks()

        self.background_image = pygame.image.load("background_ingame.png")
        self.background_image = pygame.transform.scale(self.background_image, (matrix_size * 32 , 64))

        self.not_clicked = pygame.image.load(Paths().select_sprite("grid.png")).convert()

        self.sprite = ClickableSprite(
            self.not_clicked,
            50,
            50,
            self.on_left_click,
            self.on_right_click
        )

        self.group = pygame.sprite.Group(self.sprite)
        self.group.remove(self.sprite)

        self.matrix = Matrix(
            self.bomb_number_range,
            self.matrix_size,
            self.group
        )

        for i in range(self.matrix.get_matrix_size()):
            for j in range(self.matrix.get_matrix_size()):
                self.group.add(self.matrix.get_case((i,j)).get_sprite())

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    break

                if self.matrix.check_lose():
                    #pygame.time.wait(3000)
                    print("lose")
                    #pygame.quit()
                    #scores( False , elapsed_time)
                if self.matrix.check_win():
                    #pygame.time.wait(3000)
                    print("win")
                    #pygame.quit()
                    #scores( True , elapsed_time)
                
            self.group.update(events)
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background_image, (0, 0))
            self.group.draw(self.screen)
            elapsed_time = self.display_timer()
            pygame.display.flip()
        
        pygame.quit()
    
    def display_timer(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        font = pygame.font.SysFont(None, 30)
        timer_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, (0, 0, 0))
        self.screen.blit(timer_text, (5, 10))
        return elapsed_time

    def on_left_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("empty.png")).convert()

    def on_right_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("flag.png")).convert()
