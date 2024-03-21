import pygame 

from paths import Paths
from window import Window
import ClickableSprite as ClickableSprite
import Case as C
import Matrix as Matrix

class Game(Window):
    def __init__(self, WIDTH, HEIGHT, bomb_number):
        self.matrix_size = 20

        super().__init__((matrix_size * 32, matrix_size * 32 + 64))

        self.bomb_number = bomb_number

        self.not_clicked = pygame.image.load(Paths().select_sprite("grid.png")).convert()
        self.sprite = ClickableSprite.ClickableSprite(not_clicked, 50, 50, on_left_click, on_right_click)


        self.group = pygame.sprite.Group(sprite)
        self.group.remove(sprite)

        self.matrix = Matrix.Matrix((5, 10), matrix_size, group)

        for i in range(self.matrix.get_matrix_size()) :
            for j in range(self.matrix.get_matrix_size()) :
                group.add(self.matrix.get_case((i,j)).get_sprite())

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if self.matrix.check_lose() :
                    print("lose")
                if self.matrix.check_win() :
                    print("win")


            self.group.update(events)
            self.screen.fill((255, 255, 255))
            self.group.draw(screen)
            pygame.display.update()
        
        pygame.quit()

 
    def on_left_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("empty.png")).convert()

    def on_right_click(self):
        sprite.image = pygame.image.load(Paths().select_sprite("flag.png")).convert()
