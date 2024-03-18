import pygame

class Case(pygame.sprite.Sprite) :
    __bomb = False
    __clicked = False
    __flag = 0
    __num_bombs = -1
    
    def __init__(self, bomb:bool, clicked=False, flag=0, num_bombs=-1):
        self.__bomb = bomb
        self.__clicked = clicked
        self.__flag = flag
        self.__num_bombs = num_bombs

    def get_bomb(self) :
        return self.__bomb
    
    def get_clicked(self) :
        return self.__clicked
    
    def get_flag(self) :
        return self.__flag
    
    def get_num_bombs(self) :
        return self.__num_bombs
    
    def set_clicked(self, click:bool) :
        self.__clicked = click

    def set_flag(self, flag:int) :
        if (flag >= 0 and flag <= 2) :
            self.__flag = flag

    def set_num_bombs(self, num:int) :
        if (num >= -1 and num <= 8) :
            self.__num_bombs = num