class Panel(object):

    def __renderRowNumber(self, board):
        print('    ', end='')
        for i in range(len(board)):
            if i < 10:
                print(f"{i}", end='   ')
            else:
                print(f"{i}", end='  ')
        print()

    def render(self, board):
        self.__renderRowNumber(board)
        for i in range(len(board)):
            if i < 10:
                print(i, end='  ')
            else:
                print(i, end=' ')
            for j in range(len(board[0])):
                print(" " + str(board[i][j]), end='  ')
            print(f" {i}")
            print()
        self.__renderRowNumber(board)

    def startPrompt(self):
        print("----------------------")
        print("Welcome to CLI-Gobang!")
        print("----------------------")
        print("Press: ")
        print("1 - Start New Game")
        print("2 - Exit")

    def movePrompt(self, curr_side, coordinate):
        print(f"Current side: {curr_side} Please choose a position({coordinate}) for your move: ")

    def invalidInputPrompt(self, validRange):
        print(f"Invalid input. Please enter a number ({validRange[0]} to {validRange[1]}).")

    def endPrompt(self, winner):
        print("----------------------")
        print(f"The winner is: {winner}!")
        print("Press: ")
        print("1 - Restart New Game")
        print("2 - Exit")

    def goodbyePrompt(self):
        print("Thank you for playing!")

