from enum import Enum
import copy

size = 15

'''
An enumerate class for the player side and the game state
BLACK and WHITE stands for the two sides
NONE stands for the state that there's no winner yet
'''
class Side(Enum):
    BLACK = "1"
    WHITE = "2"
    NONE = "3"


'''
The Game class that holds the components for the game
'''
class Game:
    """
    The __init__() function that sets up an empty game
    """
    def __init__(self, the_size=size, board=None, side=Side.BLACK, winner=Side.NONE):
        self.__board = board
        self.__size = the_size
        self.__currSide = side
        self.__winner = winner

    '''
    To make this class unable to be inherited
    '''
    def __init_subclass__(cls):
        raise TypeError("This class cannot be inherited!")

    '''
    The init() function that fills the board 
    '''
    def init(self):
        if self.__board is None:
            self.__board = [["_" for _ in range(size)] for _ in range(size)]
        return self.getGameState(size, self.__board, self.__currSide, self.__winner)

    '''
    A class method that returns a Game object with updated states
    '''
    @classmethod
    def getGameState(cls, the_size, board, curr_side, curr_winner):
        return cls(the_size, board, curr_side, curr_winner)

    '''
    The getter of the size
    '''
    def getSize(self):
        return self.__size

    '''
    The getter of the board that returns a deep copy of the board
    '''
    def getBoard(self):
        newBoard = copy.deepcopy(self.__board)
        return newBoard

    '''
    The getter of the current side
    '''
    def getCurrSide(self):
        return self.__currSide

    '''
    The getter of the winner
    '''
    def getWinner(self):
        return self.__winner

    '''
    A private helper function that sets the current side to be the winner
    '''
    def __setWinner(self, side):
        self.__winner = side

    '''
    A helper function that checks whether the input row/column is within the bound
    the board
    '''
    def isPosValid(self, i):
        return 0 <= i < size

    '''
    Used for checking whether the input position is within the bound of the board
    and the input position on the board is not occupied
    '''
    def isValid(self, i, j):
        return self.isPosValid(i) and self.isPosValid(j) and self.__board[i][j] == "_"

    '''
    Used for switching the current side
    '''
    def switchSide(self):
        if self.__currSide == Side.BLACK:
            self.__currSide = Side.WHITE
        else:
            self.__currSide = Side.BLACK

    '''
    Used for updating the board according to the new input
    Check the validity of the input position before really making a change
    After changing the board, check if the change produces a winner
    If so, declare the winner. If not, switch the current side
    '''
    def updateBoard(self, i, j):
        if self.isValid(i, j):
            self.__board[i][j] = self.__currSide.value
            if self.hasWon(i, j):
                self.__declareWinner()
            else:
                self.switchSide()
        else:
            pass

    '''
    Declaring the winner by returning the corresponding side
    '''
    def __declareWinner(self):
        self.__setWinner(self.__currSide)
        return self.__winner

    '''
    A private helper function that checks whether there are 5 consecutive positions 
    in the same column that are occupied by the same side. 
    '''
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

    '''
    A private helper function that checks whether there are 5 consecutive positions in the same row
    that are occupied by the same side. 
    '''
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

    '''
    A private helper function that checks whether there are 5 consecutive positions in the same diagonal
    (from top left to bottom right) that are occupied by the same side.  
    '''
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

    '''
    A private helper function that checks whether there are 5 consecutive positions in the same diagonal
    (from top right to bottom left) that are occupied by the same side.  
    '''
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

    '''
    Used for checking whether the new input produces a winner in one of the following ways:
    horizontal, vertical, diagonal
    '''
    def hasWon(self, i, j):
        return (self.__hasWonVertical(i, j)
                or self.__hasWonHorizontal(i, j)
                or self.__hasWonDiagonal1(i, j)
                or self.__hasWonDiagonal2(i, j))

    '''
    A function that resets the game state to the beginning
    Called when the winner arises and the game ends 
    '''
    def clear(self):
        self.__board = None
        self.__currSide = Side.BLACK
        self.__winner = Side.NONE
