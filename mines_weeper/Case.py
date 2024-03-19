import pygame
import ClickableSprite

pygame.init()

screen = pygame.display.set_mode((20*32, 20*32))
not_clicked = pygame.image.load("grid.png").convert()

def on_left_click(self, num_bombs:int):
    self.set_clicked(True)
    if (num_bombs == -1) :
        self.set_sprite(pygame.image.load("mine.png").convert())
    if (num_bombs == 0) :
        self.set_sprite(pygame.image.load("empty.png").convert())
    if (num_bombs >= 1) :
        self.set_sprite(pygame.image.load("grid" + str(num_bombs) + ".png").convert())
    

def on_right_click(self, clicked:bool, flag:int) :
    if (not clicked) :        
        self.set_flag((self.get_flag() + 1)%3)
        if (self.get_flag() == 0) :
            self.set_sprite(pygame.image.load("Grid.png").convert())
        if (self.get_flag() == 1) :
            self.set_sprite(pygame.image.load("flag.png").convert())
        if (self.get_flag() == 2) :
            self.set_sprite(pygame.image.load("question.png").convert())

class Case(pygame.sprite.Sprite) :
    __bomb = False
    __clicked = False
    __flag = 0
    __num_bombs = -1
    __grid_pos = (0,1)
    __sprite = ClickableSprite.ClickableSprite(not_clicked, 0, 0, on_left_click, on_right_click)

    def __init__(self, bomb:bool, grid_pos:tuple, clicked=False, flag=0, num_bombs=-1):
        self.__bomb = bomb
        self.__grid_pos = grid_pos
        self.__clicked = clicked
        self.__flag = flag
        self.__num_bombs = num_bombs
        self.__sprite = ClickableSprite.ClickableSprite(not_clicked, grid_pos[0]*32, grid_pos[1]*32, lambda : on_left_click(self, self.__num_bombs), lambda : on_right_click(self, self.__clicked, self.__flag))

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
        if (flag >= 0 and flag <= 2) :
            self.__flag = flag

    def set_num_bombs(self, num:int) :
        if (num >= -1 and num <= 8) :
            self.__num_bombs = num

    def set_sprite(self, image) :
        self.__sprite.image = image