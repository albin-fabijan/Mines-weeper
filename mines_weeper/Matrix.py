import Case
import random

class Matrix :
    __bombs = 0
    __matrix = []
    __lost = False

    def __init__(self, bombs:tuple, matrix_size:int, clicked:tuple) :
        self.__bombs = random.randint(bombs[0], bombs[1])
        bombs_placed = 0
        x = 0
        for i in range(matrix_size) :
            newL = []
            for j in range(matrix_size) :
                if (i == clicked[0] and j == clicked[1]) :
                    newCase = Case.Case(False)
                    x = -1
                else :
                    rand = random.randint(0, (matrix_size*matrix_size)-((i*matrix_size)+j))
                    if (rand < self.__bombs - bombs_placed) :
                        newCase = Case.Case(True)
                        x = 1
                        bombs_placed += 1
                    else :
                        newCase = Case.Case(False)
                        x = 2
                newL.append(newCase)
            self.__matrix.append(newL)
        self.click((clicked[0], clicked[1]))

    def has_lost(self) :
        return self.__lost

    def flag(self, pos:tuple) :
        self.__matrix[pos[0]][pos[1]].set_flag((self.__matrix[pos[0]][pos[1]].get_flag()+1)%3)

    def get_neighbors(self, pos:tuple) :
        neighbors = []
        if (pos[0]>0 and pos[1]> 0) :
            neighbors.append(self.__matrix[pos[0]-1][pos[1]-1])
        if (pos[0]>0) :
            neighbors.append(self.__matrix[pos[0]-1][pos[1]])
        if (pos[0]>0 and pos[1]< len(self.__matrix)-1) :
            neighbors.append(self.__matrix[pos[0]-1][pos[1]+1])
        if (pos[1]> 0) :
            neighbors.append(self.__matrix[pos[0]][pos[1]-1])
        if (pos[1]< len(self.__matrix)-1) :
            neighbors.append(self.__matrix[pos[0]][pos[1]+1])
        if (pos[0]< len(self.__matrix[0])-1 and pos[1]> 0) :
            neighbors.append(self.__matrix[pos[0]+1][pos[1]-1])
        if (pos[0]< len(self.__matrix[0])-1 and pos[1]> 0) :
            neighbors.append(self.__matrix[pos[0]+1][pos[1]])
        if (pos[0]< len(self.__matrix[0])-1 and pos[1]< len(self.__matrix)-1) :
            neighbors.append(self.__matrix[pos[0]+1][pos[1]+1])
        return neighbors

    def click(self, pos:tuple) :
        if (self.__matrix[pos[0]][pos[1]].get_bomb()) :
            self.__lost = True
        else : 
            neighbors = self.get_neighbors(pos)
            num_bombs = 0
            for n in neighbors :
                if (n.get_bomb()) :
                    num_bombs += 1
            self.__matrix[pos[0]][pos[1]].set_clicked(True)
            self.__matrix[pos[0]][pos[1]].set_num_bombs(num_bombs)
            if (num_bombs == 0) :
                if (pos[0]>0 and pos[1]> 0) :
                    if (not self.__matrix[pos[0]-1][pos[1]-1].get_clicked()) :
                        self.click((pos[0]-1, pos[1]-1))
                if (pos[0]>0) :
                    if (not self.__matrix[pos[0]-1][pos[1]].get_clicked()) :
                        self.click((pos[0]-1, pos[1]))
                if (pos[0]>0 and pos[1]< len(self.__matrix)-1) :
                    if (not self.__matrix[pos[0]-1][pos[1]+1].get_clicked()) :
                        self.click((pos[0]-1, pos[1]+1))
                if (pos[0]>0 and pos[1]> 0) :
                    if (not self.__matrix[pos[0]][pos[1]-1].get_clicked()) :
                        self.click((pos[0], pos[1]-1))
                if (pos[0]>0 and pos[1]< len(self.__matrix)-1) :
                    if (not self.__matrix[pos[0]][pos[1]+1].get_clicked()) :
                        self.click((pos[0], pos[1]+1))
                if (pos[0]< len(self.__matrix[0])-1 and pos[1]> 0) :
                    if (not self.__matrix[pos[0]+1][pos[1]-1].get_clicked()) :
                        self.click((pos[0]+1, pos[1]-1))
                if (pos[0]< len(self.__matrix[0])-1) :
                    if (not self.__matrix[pos[0]+1][pos[1]].get_clicked()) :
                        self.click((pos[0]+1, pos[1]))
                if (pos[0]< len(self.__matrix[0])-1 and pos[1]< len(self.__matrix)-1) :
                    if (not self.__matrix[pos[0]+1][pos[1]+1].get_clicked()) :
                        self.click((pos[0]+1, pos[1]+1))

    def check_win(self) :
        if (self.__lost) :
            return True
        for l in self.__matrix :
            for c in l :
                if (not c.get_bomb() and c.get_clicked()) :
                    return False
        return True

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

mat = Matrix((30, 50), 20, (3, 6))
mat.show()
mat.flag((5, 6))
mat.show()
mat.flag((5, 6))
mat.show()
mat.flag((5, 6)) 
mat.show()
while (not mat.check_win()) :
    input_x = input("X: ")
    input_y = input("Y: ")
    mat.click((int(input_x), int(input_y)))
    mat.show()