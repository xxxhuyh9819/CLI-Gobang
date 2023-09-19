class Panel(object):

    def render(self, board):
        print(end=" ")
        for i in range(len(board) + 1):
            for j in range(len(board[0]) + 1):
                if i == 0 and j != len(board[0]):
                    if j < 10:
                        print("   " + f"{j}", end='')
                    else:
                        print("  " + f"{j}", end='')
                    continue
                if j == 0 and i > 0:
                    if i <= 10:
                        print(f"{i - 1}", end='  ')
                    else:
                        print(f"{i - 1}", end=' ')
                if j == len(board[0]):
                    continue
                print(" " + str(board[i - 1][j - 1]), end='  ')
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

