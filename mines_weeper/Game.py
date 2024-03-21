import pygame 

from .paths import Paths
from .window import Window
from .ClickableSprite import ClickableSprite
from . import Case as C
from .Matrix import Matrix

class Game(Window):
    def __init__(self, matrix_size, bomb_number_range):
        super().__init__(matrix_size * 32, matrix_size * 32 + 64)

        self.matrix_size = matrix_size
        self.bomb_number_range = bomb_number_range
        self.start_time = pygame.time.get_ticks()

        self.not_clicked = pygame.image.load(
            Paths().select_sprite("grid.png")
        ).convert()
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

        for i in range(self.matrix.get_matrix_size()) :
            for j in range(self.matrix.get_matrix_size()) :
                self.group.add(self.matrix.get_case((i,j)).get_sprite())

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    break

                if self.matrix.check_lose() :
                    print("lose")
                if self.matrix.check_win() :
                    print("win")
                
            self.group.update(events)
            self.screen.fill((255, 255, 255))
            self.group.draw(self.screen)
            print((pygame.time.get_ticks() - self.start_time) / 1000)
            pygame.display.flip()
        
        pygame.quit()
 
    def on_left_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("empty.png")).convert()

    def on_right_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("flag.png")).convert()


