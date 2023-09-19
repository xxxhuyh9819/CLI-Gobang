from src.model.game import Game, Side
from src.view.interface import Panel
from src.controller.action import PlayAction

g = Game()
panel = Panel()
action = PlayAction(g, panel)

action.receiveStartAndEndInput()


def run():
    while g.getWinner() == Side.NONE:
        # panel.render(g.getBoard())
        # action.receivePosInput("row")
        # action.receivePosInput("column")
        action.place()
    if action.endGame() == 1:
        run()
    else:
        pass


if __name__ == "__main__":
    run()

