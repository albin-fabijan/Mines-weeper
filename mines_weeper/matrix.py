from .case import Case
import random
import pygame

class Matrix :
    def __init__(self, bombs:tuple, matrix_size:int, group:pygame.sprite.Group) :
        self.__first_click = True
        self.__bombs = random.randint(bombs[0], bombs[1])
        self.__lost = False
        self.__group = group
        self.__matrix_size = matrix_size
        self.matrix = []
        for i in range(self.__matrix_size) :
            newL = []
            for j in range(self.__matrix_size) :
                newCase = Case(False, (i, j), self, self.__group)
                newL.append(newCase)
            self.matrix.append(newL)
        
    def first_click(self, clicked:tuple):
        bombs_placed = 0
        pos1 = 0
        pos2 = 0
        for i in range(self.__matrix_size) :
            for j in range(self.__matrix_size) :
                if (i == clicked[0] and j == clicked[1]) :
                    newCase = Case(False, (i, j), self, self.__group)
                else :
                    rand = random.randint(0, (self.__matrix_size*self.__matrix_size)-((i*self.__matrix_size)+j))
                    if (rand < self.__bombs - bombs_placed) :
                        newCase = Case(True, (i, j), self, self.__group)
                        pos1 = i
                        pos2 = j
                        bombs_placed += 1
                    else :
                        newCase = Case(False, (i, j), self, self.__group)
                self.matrix[i][j] = newCase
        for i in range(self.__matrix_size) :
            for j in range(self.__matrix_size) :
                neighbors = self.get_neighbors(self.matrix[i][j].grid_pos)
                bombs = 0
                if (self.matrix[i][j].bomb) :
                    bombs = -1
                else :
                    for n in neighbors :
                        if (n.bomb) :
                            bombs += 1
                self.matrix[i][j].set_num_bombs(bombs)
        self.click((clicked[0], clicked[1]))

    def has_lost(self) :
        return self.__lost

    def get_first_click(self):
        return self.__first_click

    def get_neighbors(self, pos:tuple) :
        neighbors = []
        if (pos[0]>0 and pos[1]> 0) :
            neighbors.append(self.matrix[pos[0]-1][pos[1]-1])
        if (pos[0]>0) :
            neighbors.append(self.matrix[pos[0]-1][pos[1]])
        if (pos[0]>0 and pos[1]< self.get_matrix_size()-1) :
            neighbors.append(self.matrix[pos[0]-1][pos[1]+1])
        if (pos[1]> 0) :
            neighbors.append(self.matrix[pos[0]][pos[1]-1])
        if (pos[1]< self.get_matrix_size()-1) :
            neighbors.append(self.matrix[pos[0]][pos[1]+1])
        if (pos[0]< self.get_matrix_size()-1 and pos[1]> 0) :
            neighbors.append(self.matrix[pos[0]+1][pos[1]-1])
        if (pos[0]< self.get_matrix_size()-1) :
            neighbors.append(self.matrix[pos[0]+1][pos[1]])
        if (pos[0]< self.get_matrix_size()-1 and pos[1]< self.get_matrix_size()-1) :
            neighbors.append(self.matrix[pos[0]+1][pos[1]+1])
        return neighbors

    def click(self, pos:tuple) :
        if (self.__first_click) :
            self.__first_click = False
            self.first_click(pos)
        if (self.matrix[pos[0]][pos[1]].bomb) :
            self.matrix[pos[0]][pos[1]].set_clicked(True)
            self.__lost = True
        else : 
            neighbors = self.get_neighbors(pos)
            num_bombs = 0
            for n in neighbors :
                if (n.bomb) :
                    num_bombs += 1
            self.matrix[pos[0]][pos[1]].set_clicked(True)
            if (num_bombs == 0) :
                if (pos[0]>0 and pos[1]> 0) :
                    if (not self.matrix[pos[0]-1][pos[1]-1].clicked) :
                        self.click((pos[0]-1, pos[1]-1))
                if (pos[0]>0) :
                    if (not self.matrix[pos[0]-1][pos[1]].clicked) :
                        self.click((pos[0]-1, pos[1]))
                if (pos[0]>0 and pos[1]< self.get_matrix_size()-1) :
                    if (not self.matrix[pos[0]-1][pos[1]+1].clicked) :
                        self.click((pos[0]-1, pos[1]+1))
                if (pos[1]> 0) :
                    if (not self.matrix[pos[0]][pos[1]-1].clicked) :
                        self.click((pos[0], pos[1]-1))
                if (pos[1]< self.get_matrix_size()-1) :
                    if (not self.matrix[pos[0]][pos[1]+1].clicked) :
                        self.click((pos[0], pos[1]+1))
                if (pos[0]< self.get_matrix_size()-1 and pos[1]> 0) :
                    if (not self.matrix[pos[0]+1][pos[1]-1].clicked) :
                        self.click((pos[0]+1, pos[1]-1))
                if (pos[0]< self.get_matrix_size()-1) :
                    if (not self.matrix[pos[0]+1][pos[1]].clicked) :
                        self.click((pos[0]+1, pos[1]))
                if (pos[0]< self.get_matrix_size()-1 and pos[1]< self.get_matrix_size()-1) :
                    if (not self.matrix[pos[0]+1][pos[1]+1].clicked) :
                        self.click((pos[0]+1, pos[1]+1))

    def check_win(self) :
        bombs = []
        for c in self.get_cases() :
            if (c.bomb) :
                bombs.append(c)
            if (not c.bomb and not c.clicked) :
                return False
        for b in bombs :
            if (not self.get_case(b.grid_pos).flag == 1) : # c'est ça qu'il faut regarder
                return False
        return True
    
    def check_lose(self) :
        if (self.__lost) :
            return True
        return False
    
    def get_matrix_size(self) :
        return self.__matrix_size
    
    def get_case(self, pos:tuple) :
        return self.matrix[pos[0]][pos[1]]
    
    def get_cases(self) :
        list = []
        for l in self.matrix :
            for l2 in l :
                list.append(l2)
        return list
