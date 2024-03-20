import pygame
import ClickableSprite
import Matrix

pygame.init()

screen = pygame.display.set_mode((20*32, 20*32))
not_clicked = pygame.image.load("grid.png").convert()

def on_left_click(self, click_func, reset_func):
    click_func()
    reset_func()

def on_right_click(self) :
    if (not self.get_clicked()) :
        print(self.get_grid_pos())
        self.set_flag((self.get_flag() + 1)%3)
        if (self.get_flag() == 0) :
            self.set_sprite(pygame.image.load("Grid.png").convert())
        if (self.get_flag() == 1) :
            self.set_sprite(pygame.image.load("flag.png").convert())
        if (self.get_flag() == 2) :
            self.set_sprite(pygame.image.load("question.png").convert())

class Case(pygame.sprite.Sprite) :
    #__bomb = False
    #__clicked = False
    #__flag = 0
    #__num_bombs = -1
    #__grid_pos = (0,1)
    #__sprite = ClickableSprite.ClickableSprite(not_clicked, 0, 0, on_left_click, on_right_click)

    def __init__(self, bomb:bool, grid_pos:tuple, matrix:Matrix.Matrix, group:pygame.sprite.Group, clicked=False, flag=0, num_bombs=-1):
        self.__bomb = bomb
        self.__grid_pos = grid_pos
        self.__clicked = clicked
        self.__flag = flag
        self.__num_bombs = num_bombs
        self.__sprite = ClickableSprite.ClickableSprite(not_clicked, grid_pos[0]*32, grid_pos[1]*32, lambda : on_left_click(self, lambda : matrix.click(pos=grid_pos), lambda : self.reset_sprites(matrix, group)), lambda : [on_right_click(self), print(self.get_flag())])

    def get_bomb(self) :
        return self.__bomb
    
    def get_clicked(self) :
        return self.__clicked
    
    def get_flag(self) :
        return self.__flag
    
    def get_num_bombs(self) :
        return self.__num_bombs
    
    def get_grid_pos(self) :
        return self.__grid_pos
    
    def get_sprite(self) :
        return self.__sprite
    
    def set_clicked(self, click:bool) :
        self.__clicked = click

    def set_flag(self, flag:int) :
        self.__flag = flag

    def set_num_bombs(self, num:int) :
        if (num >= -1 and num <= 8) :
            self.__num_bombs = num

    def set_sprite(self, image) :
        self.__sprite.image = image

    def get_clicked_sprite(self, num_bombs:int) :
        if (self.__clicked) :
            if (num_bombs == -1) :
                self.set_flag(0)
                return pygame.image.load("mine.png").convert()
            if (num_bombs == 0) :
                self.set_flag(0)
                return pygame.image.load("empty.png").convert()
            if (num_bombs >= 1) :
                self.set_flag(0)
                return pygame.image.load("grid" + str(num_bombs) + ".png").convert()
        else :
            if (self.get_flag() == 0) :
                return pygame.image.load("Grid.png").convert()
            if (self.get_flag() == 1) :
                return pygame.image.load("flag.png").convert()
            if (self.get_flag() == 2) :
                return pygame.image.load("question.png").convert()
            
    def reset_sprites(self, matrix, group) :
        sprites = []
        for sprite in group :
            sprites.append(sprite)
        for i in range(len(matrix.get_cases())) :
            mat_case = matrix.get_cases()[i]
            if (mat_case.get_clicked()) :
                sprites[i].image = mat_case.get_clicked_sprite(mat_case.get_num_bombs())
        for sprite in group :
            group.remove(sprite)
        for sprite in sprites :
            group.add(sprite)