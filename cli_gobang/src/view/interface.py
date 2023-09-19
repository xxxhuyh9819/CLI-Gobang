class Panel(object):

    def render(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(str(board[i][j]), end='  ')
            print()

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

