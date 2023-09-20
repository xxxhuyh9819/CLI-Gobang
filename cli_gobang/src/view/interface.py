class Panel(object):
    """
    A private helper function that prints the column number of the board
    """
    def __renderColNumber(self, board):
        print('    ', end='')
        for i in range(len(board)):
            if i < 10:
                print(f"{i}", end='   ')
            else:
                print(f"{i}", end='  ')
        print()

    """
    A function that prints the entire board
    Gets called after every change on the board is made
    """
    def render(self, board):
        self.__renderColNumber(board)
        for i in range(len(board)):
            if i < 10:
                print(i, end='  ')
            else:
                print(i, end=' ')
            for j in range(len(board[0])):
                print(" " + str(board[i][j]), end='  ')
            print(f" {i}")
        self.__renderColNumber(board)

    """
    A function that prints the welcome interface once starts the application
    """
    def startPrompt(self):
        print("----------------------")
        print("Welcome to CLI-Gobang!")
        print("----------------------")
        print("Press: ")
        print("1 - Start New Game")
        print("2 - Exit")

    """
    A function that prints the interface that guides the player to input a new position
    """
    def movePrompt(self, curr_side, coordinate):
        print(f"Current side: {curr_side} Please choose a position({coordinate}) for your move: ")

    """
    A function that prints the interface when the input is invalid
    """
    def invalidInputPrompt(self, validRange):
        print(f"Invalid input. Please enter a number ({validRange[0]} to {validRange[1]}).")

    """
    A function that prints the interface once a winner arises
    """
    def endPrompt(self, winner):
        print("----------------------")
        print(f"The winner is: {winner}!")
        print("Press: ")
        print("1 - Restart New Game")
        print("2 - Exit")

    """
    A function that prints the words when exiting the game
    """
    def goodbyePrompt(self):
        print("Thank you for playing. See you next time!")

