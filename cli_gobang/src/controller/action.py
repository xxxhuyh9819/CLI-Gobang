from src.model.game import Game
from src.view.interface import Panel
import re


class PlayAction(object):
    def __init__(self, game: Game, panel: Panel):
        self.__game = game
        self.__panel = panel

    def getGame(self):
        return self.__game

    def getPanel(self):
        return self.__panel

    def receiveStartAndEndInput(self):
        self.__panel.startPrompt()
        option = input()
        while option != "1" and option != "2":
            self.__panel.invalidInputPrompt([1, 2])
            option = input()
        if option == "1":
            self.__game.init()
            self.__panel.render(self.__game.getBoard())

    def receivePosInput(self, coordinate):
        self.__panel.movePrompt(self.__game.getCurrSide().name, coordinate)
        pos = input()
        pattern = "^\d+$"
        while not re.match(pattern, pos) or not self.__game.isPosValid(int(pos)):
            self.__panel.invalidInputPrompt([0, 15])
            pos = input()
        return int(pos)

    def place(self):
        row = self.receivePosInput("row")
        col = self.receivePosInput("column")
        while not self.__game.isValid(row, col):
            print("invalid")
            row = self.receivePosInput("row")
            col = self.receivePosInput("column")
        self.__game.updateBoard(row, col)
        self.__panel.render(self.__game.getBoard())

    def endGame(self):
        self.__panel.endPrompt(self.__game.getWinner().name)
        self.__game.clear()
        option = input()
        while option != "1" and option != "2":
            self.__panel.invalidInputPrompt([1, 2])
        if option == "1":
            self.__game.init()
            self.__panel.render(self.__game.getBoard())
        else:
            self.__panel.goodbyePrompt()
        return int(option)
