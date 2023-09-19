from enum import Enum
import copy

size = 15


class Side(Enum):
    BLACK = "1"
    WHITE = "2"
    NONE = "3"


class Game:
    def __init__(self, the_size=size, board=None, side=Side.BLACK, winner=Side.NONE):
        self.__board = board
        self.__size = the_size
        self.__currSide = side
        self.__winner = winner

    def __init_subclass__(cls):
        raise TypeError("This class cannot be inherited!")

    def init(self):
        if self.__board is None:
            self.__board = [["_" for _ in range(size)] for _ in range(size)]
        return self.getGameState(size, self.__board, self.__currSide, self.__winner)

    @classmethod
    def getGameState(cls, the_size, board, curr_side, curr_winner):
        return cls(the_size, board, curr_side, curr_winner)

    def getSize(self):
        return self.__size

    def getBoard(self):
        newBoard = copy.deepcopy(self.__board)
        return newBoard

    def getCurrSide(self):
        return self.__currSide

    def getWinner(self):
        return self.__winner

    def setWinner(self, side):
        self.__winner = side

    def isPosValid(self, i):
        return 0 <= i < size

    def isValid(self, i, j):
        return self.isPosValid(i) and self.isPosValid(j) and self.__board[i][j] == "_"

    def switchSide(self):
        if self.__currSide == Side.BLACK:
            self.__currSide = Side.WHITE
        else:
            self.__currSide = Side.BLACK

    def updateBoard(self, i, j):
        if self.isValid(i, j):
            self.__board[i][j] = self.__currSide.value
            if self.hasWon(i, j):
                self.__declareWinner()
            else:
                self.switchSide()
        else:
            pass
        # return self.getGameState(self.getSize(), self.getBoard(), self.getCurrSide(), self.getWinner())

        # give a signal to view

    def __declareWinner(self):
        self.setWinner(self.__currSide)
        return self.__winner

    def __hasWonVertical(self, i, j):
        consecutive = 0
        startRow = i
        while startRow >= 0 and self.__board[startRow][j] == self.__currSide.value:
            consecutive += 1
            startRow -= 1
            if consecutive == 5:
                return True
        startRow = i
        while startRow < self.__size and self.__board[startRow][j] == self.__currSide.value:
            if startRow != i:
                consecutive += 1
            startRow += 1
            if consecutive == 5:
                return True
        return consecutive == 5

    def __hasWonHorizontal(self, i, j):
        consecutive = 0
        startCol = j
        while startCol >= 0 and self.__board[i][startCol] == self.__currSide.value:
            consecutive += 1
            startCol -= 1
            if consecutive == 5:
                return True
        startCol = j
        while startCol < self.__size and self.__board[i][startCol] == self.__currSide.value:
            if startCol != j:
                consecutive += 1
            startCol += 1
            if consecutive == 5:
                return True
        return consecutive == 5

    def __hasWonDiagonal1(self, i, j):
        consecutive = 0
        startRow = i
        startCol = j
        while (startRow >= 0 and startCol >= 0
               and self.__board[startRow][startCol] == self.__currSide.value):
            consecutive += 1
            startRow -= 1
            startCol -= 1
            if consecutive == 5:
                return True
        startRow = i
        startCol = j
        while (startRow < self.__size and startCol < self.__size
               and self.__board[startRow][startCol] == self.__currSide.value):
            if startRow != i and startCol != j:
                consecutive += 1
            startRow += 1
            startCol += 1
            if consecutive == 5:
                return True
        return consecutive == 5

    def __hasWonDiagonal2(self, i, j):
        consecutive = 0
        startRow = i
        startCol = j
        while (startRow >= 0 and startCol < self.__size
               and self.__board[startRow][startCol] == self.__currSide.value):
            consecutive += 1
            startRow -= 1
            startCol += 1
            if consecutive == 5:
                return True
        startRow = i
        startCol = j
        while (startRow < self.__size and startCol >= 0
               and self.__board[startRow][startCol] == self.__currSide.value):
            consecutive += 1
            startRow += 1
            startCol -= 1
            if consecutive == 5:
                return True
        return consecutive == 5

    def hasWon(self, i, j):
        return (self.__hasWonVertical(i, j)
                or self.__hasWonHorizontal(i, j)
                or self.__hasWonDiagonal1(i, j)
                or self.__hasWonDiagonal2(i, j))

    def clear(self):
        self.__board = None
        self.__currSide = Side.BLACK
        self.__winner = Side.NONE
