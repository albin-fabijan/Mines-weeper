import Case as C
import random
import pygame

class Matrix :
    __bombs = 0
    __lost = False
    __first_click = True
    __matrix_size = 0

    def __init__(self, bombs:tuple, matrix_size:int, group:pygame.sprite.Group) :
        self.__bombs = random.randint(bombs[0], bombs[1])
        self.__lost = False
        self.__group = group
        self.__matrix_size = matrix_size
        self.__matrix = []
        # print(self.__matrix_size)
        for i in range(self.__matrix_size) :
            newL = []
            for j in range(self.__matrix_size) :
                newCase = C.Case(False, (i, j), self, group)
                newL.append(newCase)
            self.__matrix.append(newL)
        
    def first_click(self, clicked:tuple) :
        bombs_placed = 0
        pos1 = 0
        pos2 = 0
        for i in range(self.__matrix_size) :
            # newL = []
            # self.__matrix.append(newL)
            for j in range(self.__matrix_size) :
                # print(bombs_placed, end="")
                if (i == clicked[0] and j == clicked[1]) :
                    newCase = C.Case(False, (i, j), self, self.__group)
                else :
                    rand = random.randint(0, (self.__matrix_size*self.__matrix_size)-((i*self.__matrix_size)+j))
                    if (rand < self.__bombs - bombs_placed) :
                        newCase = C.Case(True, (i, j), self, self.__group)
                        # print(newCase.get_bomb(), end="")
                        pos1 = i
                        pos2 = j
                        bombs_placed += 1
                    else :
                        newCase = C.Case(False, (i, j), self, self.__group)
                self.__matrix[i][j] = newCase
                # self.__matrix[i].append(newCase)
                
                # print(self.__matrix[i][j].get_grid_pos(), end="")
                # print(self.__matrix[i][j].get_bomb())
        # print(f"Number of bombs : {bombs_placed}, {self.__matrix[pos1][pos2].get_bomb()}, {pos1}, {pos2}")
        for i in range(self.__matrix_size) :
            for j in range(self.__matrix_size) :
                neighbors = self.get_neighbors(self.__matrix[i][j].get_grid_pos())
                bombs = 0
                if (self.__matrix[i][j].get_bomb()) :
                    bombs = -1
                    # print("bomb")
                else :
                    for n in neighbors :
                        if (n.get_bomb()) :
                            bombs += 1
                self.__matrix[i][j].set_num_bombs(bombs)
        self.click((clicked[0], clicked[1]))

    def has_lost(self) :
        return self.__lost

    def get_neighbors(self, pos:tuple) :
        neighbors = []
        if (pos[0]>0 and pos[1]> 0) :
            neighbors.append(self.__matrix[pos[0]-1][pos[1]-1])
        if (pos[0]>0) :
            neighbors.append(self.__matrix[pos[0]-1][pos[1]])
        if (pos[0]>0 and pos[1]< self.get_matrix_size()-1) :
            neighbors.append(self.__matrix[pos[0]-1][pos[1]+1])
        if (pos[1]> 0) :
            neighbors.append(self.__matrix[pos[0]][pos[1]-1])
        if (pos[1]< self.get_matrix_size()-1) :
            neighbors.append(self.__matrix[pos[0]][pos[1]+1])
        if (pos[0]< self.get_matrix_size()-1 and pos[1]> 0) :
            neighbors.append(self.__matrix[pos[0]+1][pos[1]-1])
        if (pos[0]< self.get_matrix_size()-1) :
            neighbors.append(self.__matrix[pos[0]+1][pos[1]])
        if (pos[0]< self.get_matrix_size()-1 and pos[1]< self.get_matrix_size()-1) :
            neighbors.append(self.__matrix[pos[0]+1][pos[1]+1])
        return neighbors

    def click(self, pos:tuple) :
        # print("click " + str(pos), end="")
        if (self.__first_click) :
            self.__first_click = False
            # print("first")
            self.first_click(pos)
        if (self.__matrix[pos[0]][pos[1]].get_bomb()) :
            # print("bomb")
            self.__matrix[pos[0]][pos[1]].set_clicked(True)
            self.__lost = True
        else : 
            neighbors = self.get_neighbors(pos)
            num_bombs = 0
            for n in neighbors :
                if (n.get_bomb()) :
                    num_bombs += 1
            self.__matrix[pos[0]][pos[1]].set_clicked(True)
            # print(num_bombs)
            if (num_bombs == 0) :
                if (pos[0]>0 and pos[1]> 0) :
                    if (not self.__matrix[pos[0]-1][pos[1]-1].get_clicked()) :
                        self.click((pos[0]-1, pos[1]-1))
                if (pos[0]>0) :
                    if (not self.__matrix[pos[0]-1][pos[1]].get_clicked()) :
                        self.click((pos[0]-1, pos[1]))
                if (pos[0]>0 and pos[1]< self.get_matrix_size()-1) :
                    if (not self.__matrix[pos[0]-1][pos[1]+1].get_clicked()) :
                        self.click((pos[0]-1, pos[1]+1))
                if (pos[1]> 0) :
                    if (not self.__matrix[pos[0]][pos[1]-1].get_clicked()) :
                        self.click((pos[0], pos[1]-1))
                if (pos[1]< self.get_matrix_size()-1) :
                    if (not self.__matrix[pos[0]][pos[1]+1].get_clicked()) :
                        self.click((pos[0], pos[1]+1))
                if (pos[0]< self.get_matrix_size()-1 and pos[1]> 0) :
                    if (not self.__matrix[pos[0]+1][pos[1]-1].get_clicked()) :
                        self.click((pos[0]+1, pos[1]-1))
                if (pos[0]< self.get_matrix_size()-1) :
                    if (not self.__matrix[pos[0]+1][pos[1]].get_clicked()) :
                        self.click((pos[0]+1, pos[1]))
                if (pos[0]< self.get_matrix_size()-1 and pos[1]< self.get_matrix_size()-1) :
                    if (not self.__matrix[pos[0]+1][pos[1]+1].get_clicked()) :
                        self.click((pos[0]+1, pos[1]+1))

    def check_win(self) :
        bombs = []
        for c in self.get_cases() :
            if (c.get_bomb()) :
                bombs.append(c)
            if (not c.get_bomb() and not c.get_clicked()) :
                return False
        for b in bombs :
            print(b.get_grid_pos())
            print(self.get_case(b.get_grid_pos()).get_flag())
            if (self.get_case(b.get_grid_pos()) == 1) :
                return True
        return False
    
    def check_lose(self) :
        if (self.__lost) :
            return True
        return False
    
    def get_matrix_size(self) :
        return self.__matrix_size
    
    def get_case(self, pos:tuple) :
        return self.__matrix[pos[0]][pos[1]]
    
    def get_cases(self) :
        list = []
        for l in self.__matrix :
            for l2 in l :
                list.append(l2)
        return list

    def show(self) :
        for l in range(len(self.__matrix)) :
            for l2 in range(len(self.__matrix)) :
                if (self.__matrix[l][l2].get_bomb()) :
                    print("B ", end="")
                elif (l == 3 and l2 == 6) :
                    print("X ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 0) :
                    print("0 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 1) :
                    print("1 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 2) :
                    print("2 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 3) :
                    print("3 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 4) :
                    print("4 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 5) :
                    print("5 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 6) :
                    print("6 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 7) :
                    print("7 ", end="")
                elif (self.__matrix[l][l2].get_num_bombs() == 8) :
                    print("8 ", end="")
                elif (self.__matrix[l][l2].get_flag() == 1) :
                    print("F ", end="")
                elif (self.__matrix[l][l2].get_flag() == 2) :
                    print("? ", end="")
                else :
                    print(". ", end="")
            print("")
        print("")
