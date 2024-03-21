import pygame

from .paths import Paths
from .ClickableSprite import ClickableSprite

class Case(pygame.sprite.Sprite) :

    def __init__(self, bomb, grid_pos, matrix, group, clicked=False, flag=0, num_bombs=-1):
        self.bomb = bomb
        self.grid_pos = grid_pos
        self.clicked = clicked
        self.flag = flag
        self.num_bombs = num_bombs
        self.not_clicked = pygame.image.load(Paths().select_sprite("Grid.png"))
        self.sprite = ClickableSprite(
            self.not_clicked,
            grid_pos[0]*32,
            grid_pos[1]*32+64,
            lambda : self.on_left_click(
                lambda : matrix.click(pos=grid_pos),
                lambda : self.reset_sprites(matrix, group)
            ),
            lambda : self.on_right_click(matrix)
        )

    def get_sprite(self):
        return self.sprite

    def set_clicked(self, click:bool) :
        self.clicked = click

    def set_flag(self, flag:int) :
        self.flag = flag

    def set_num_bombs(self, num:int) :
        if (num >= -1 and num <= 8) :
            self.num_bombs = num

    def set_sprite(self, image) :
        self.sprite.image = image

    def get_clicked_sprite(self, num_bombs:int) :
        if (self.clicked) :
            if (num_bombs == -1) :
                self.set_flag(0)
                return pygame.image.load(Paths().select_sprite("mine.png")).convert()
            if (num_bombs == 0) :
                self.set_flag(0)
                return pygame.image.load(Paths().select_sprite("empty.png")).convert()
            if (num_bombs >= 1) :
                self.set_flag(0)
                return pygame.image.load(Paths().select_sprite("grid" + str(self.num_bombs) + ".png")).convert()
        else :
            if (self.flag() == 0) :
                return pygame.image.load(Paths().select_sprite("Grid.png")).convert()
            if (self.flag() == 1) :
                return pygame.image.load(Paths().select_sprite("flag.png")).convert()
            if (self.flag() == 2) :
                return pygame.image.load(Paths().select_sprite("question.png")).convert()
            
    def reset_sprites(self, matrix, group) :
        sprites = []
        for sprite in group :
            sprites.append(sprite)
        for i in range(len(matrix.get_cases())) :
            mat_case = matrix.get_cases()[i]
            if (mat_case.clicked) :
                sprites[i].image = mat_case.get_clicked_sprite(mat_case.num_bombs)
        for sprite in group :
            group.remove(sprite)
        for sprite in sprites :
            group.add(sprite)

    def on_left_click(self, click_func, reset_func):
        click_func()
        reset_func()

    def on_right_click(self, matrix) :
        mat_case = matrix.get_case(self.grid_pos)
        if (not mat_case.clicked) :
            if (self.flag == 0) :
                self.set_flag(1)
                mat_case.set_flag(1)
            elif (self.flag == 1) :
                self.set_flag(2)
                mat_case.set_flag(2)
            elif (self.flag == 2) :
                self.set_flag(0)
                mat_case.set_flag(0)

            if (self.flag == 0) :
                self.set_sprite(pygame.image.load(Paths().select_sprite("Grid.png")).convert())
            if (self.flag == 1) :
                self.set_sprite(pygame.image.load(Paths().select_sprite("flag.png")).convert())
            if (self.flag == 2) :
                self.set_sprite(pygame.image.load(Paths().select_sprite("question.png")).convert())

pygame.quit()