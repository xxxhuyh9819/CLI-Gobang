from src.model.game import Game, Side
from src.view.interface import Panel
from src.controller.action import PlayAction

g = Game()
panel = Panel()
action = PlayAction(g, panel)

action.receiveStartAndEndInput()

"""
A function that runs the game
Gets recursively called if the players continues to play after one game ends
"""


def run():
    while g.getWinner() == Side.NONE:
        action.place()
    if action.endGame() == 1:
        run()
    else:
        pass


if __name__ == "__main__":
    run()
