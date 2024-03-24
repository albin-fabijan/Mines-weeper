import random

import pygame

from .Case import Case

class Matrix:
    def __init__(
            self,
            bombs:tuple,
            matrix_size:int,
            group:pygame.sprite.Group
        ):
        self.__first_click = True
        self.__bombs = random.randint(bombs[0], bombs[1])
        self.__lost = False
        self.__group = group
        self.__matrix_size = matrix_size
        self.matrix = []
        for i in range(self.__matrix_size):
            newL = []
            for j in range(self.__matrix_size):
                new_case = Case(False, (i, j), self, self.__group)
                newL.append(new_case)
            self.matrix.append(newL)
        
    def first_click(self, clicked:tuple):
        bombs_placed = 0
        position_1 = 0
        position_2 = 0
        for i in range(self.__matrix_size):
            for j in range(self.__matrix_size):
                if (i == clicked[0] and j == clicked[1]):
                    new_case = Case(False, (i, j), self, self.__group)
                else:
                    random_value = random.randint(
                            0,
                            (self.__matrix_size*self.__matrix_size)
                            - ((i * self.__matrix_size) + j)
                    )
                    if (random_value < self.__bombs - bombs_placed):
                        new_case = Case(True, (i, j), self, self.__group)
                        position_1 = i
                        position_2 = j
                        bombs_placed += 1
                    else:
                        new_case = Case(False, (i, j), self, self.__group)
                self.matrix[i][j] = new_case
        for i in range(self.__matrix_size):
            for j in range(self.__matrix_size):
                neighbors = self.get_neighbors(
                        self.matrix[i][j].grid_position
                )
                bombs = 0
                if (self.matrix[i][j].bomb):
                    bombs = -1
                else:
                    for n in neighbors:
                        if (n.bomb):
                            bombs += 1
                self.matrix[i][j].set_bomb_number(bombs)
        self.click((clicked[0], clicked[1]))

    def has_lost(self):
        return self.__lost

    def get_first_click(self):
        return self.__first_click

    def get_neighbors(self, position:tuple):
        neighbors = []
        if (position[0] > 0 and position[1] > 0):
            neighbors.append(self.matrix[position[0] - 1][position[1] - 1])

        if (position[0] > 0):
            neighbors.append(self.matrix[position[0] - 1][position[1]])

        if (position[0] > 0 and position[1] < self.get_matrix_size() - 1):
            neighbors.append(self.matrix[position[0] - 1][position[1] + 1])

        if (position[1] > 0):
            neighbors.append(self.matrix[position[0]][position[1] - 1])

        if (position[1] < self.get_matrix_size() -1):
            neighbors.append(self.matrix[position[0]][position[1] + 1])

        if (position[0] < self.get_matrix_size() -1 and position[1] > 0):
            neighbors.append(self.matrix[position[0]+1][position[1] - 1])

        if (position[0] < self.get_matrix_size() -1):
            neighbors.append(self.matrix[position[0]+1][position[1]])

        if (
            (position[0] < self.get_matrix_size() -1
             and position[1]< self.get_matrix_size() -1)
        ):
            neighbors.append(self.matrix[position[0] + 1][position[1] + 1])

        return neighbors

    def click(self, position:tuple):
        if (self.__first_click):
            self.__first_click = False
            self.first_click(position)
        if (self.matrix[position[0]][position[1]].bomb):
            self.matrix[position[0]][position[1]].set_clicked(True)
            self.__lost = True
        else: 
            neighbors = self.get_neighbors(position)
            bomb_number = 0
            for n in neighbors:
                if (n.bomb):
                    bomb_number += 1
            self.matrix[position[0]][position[1]].set_clicked(True)
            if (bomb_number == 0):
                if (position[0] > 0 and position[1] > 0):
                    if not self.matrix[position[0] - 1][position[1] - 1].clicked:
                        self.click((position[0] - 1, position[1] - 1))

                if (position[0] > 0):
                    if (not self.matrix[position[0] - 1][position[1]].clicked):
                        self.click((position[0] - 1, position[1]))

                if (position[0]>0 and position[1]< self.get_matrix_size() - 1):
                    if (not self.matrix[position[0] - 1][position[1] + 1].clicked):
                        self.click((position[0] - 1, position[1] + 1))
                if (position[1]> 0):
                    if (not self.matrix[position[0]][position[1] - 1].clicked):
                        self.click((position[0], position[1] - 1))

                if (position[1]< self.get_matrix_size() - 1):
                    if (not self.matrix[position[0]][position[1] + 1].clicked):
                        self.click((position[0], position[1] + 1))

                if (position[0]< self.get_matrix_size() - 1 and position[1] > 0):
                    if (not self.matrix[position[0] + 1][position[1] - 1].clicked):
                        self.click((position[0] + 1, position[1] - 1))

                if (position[0]< self.get_matrix_size() - 1):
                    if (not self.matrix[position[0] + 1][position[1]].clicked):
                        self.click((position[0] + 1, position[1]))

                if (
                    (position[0]< self.get_matrix_size() - 1
                     and position[1]< self.get_matrix_size() - 1)
                ):
                    if (not self.matrix[position[0] + 1][position[1] + 1].clicked):
                        self.click((position[0] + 1, position[1] + 1))

    def check_win(self):
        bombs = []
        for c in self.get_cases():
            if (c.bomb):
                bombs.append(c)
            if not c.bomb and not c.clicked:
                return False
        for b in bombs:
            if (not self.get_case(b.grid_position).flag == 1):
                return False
        return True
    
    def check_lose(self):
        if self.__lost:
            return True
        return False
    
    def get_matrix_size(self):
        return self.__matrix_size
    
    def get_case(self, position:tuple):
        return self.matrix[position[0]][position[1]]
    
    def get_cases(self):
        list = []
        for l in self.matrix:
            for l2 in l:
                list.append(l2)
        return list
