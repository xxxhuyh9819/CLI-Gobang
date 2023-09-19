import unittest

from ..src.model.game import Game, Side


class TestGame(unittest.TestCase):
    game = Game()

    def test_board_size(self):
        g = Game()
        g.init()
        self.assertEqual(len(g.getBoard()), 15)

    def test_current_side(self):
        g = Game()
        g.init()
        self.assertEqual(g.getCurrSide(), Side.BLACK)

    def test_board_all_empty(self):
        g = Game()
        g.init()
        for i in range(g.getSize()):
            for j in range(g.getSize()):
                self.assertEqual(g.getBoard()[i][j], "_")

    def test_switch_side(self):
        g = Game()
        g.init()
        g.switchSide()
        self.assertEqual(g.getCurrSide(), Side.WHITE)
        g.switchSide()
        self.assertEqual(g.getCurrSide(), Side.BLACK)

    def test_update_valid(self):
        g = Game()
        g.init()
        g.updateBoard(0, 2)
        self.assertEqual(g.getBoard()[0][2], "1")
        self.assertEqual(g.getCurrSide(), Side.WHITE)
        g.updateBoard(1, 2)
        self.assertEqual(g.getBoard()[1][2], "2")
        self.assertEqual(g.getCurrSide(), Side.BLACK)

    def test_update_out_of_range(self):
        g = Game()
        g.init()
        g.updateBoard(-1, 2)
        self.assertEqual(g.getCurrSide(), Side.BLACK)

    def test_update_occupied(self):
        g = Game()
        g.init()
        g.updateBoard(0, 2)
        self.assertEqual(g.getCurrSide(), Side.WHITE)
        g.updateBoard(0, 2)
        self.assertEqual(g.getBoard()[0][2], "1")
        self.assertEqual(g.getCurrSide(), Side.WHITE)

    def test_hasWon_vertical(self):
        g = Game()
        g.init()
        g.updateBoard(4, 2)
        g.updateBoard(0, 4)
        g.updateBoard(2, 2)
        g.updateBoard(10, 2)
        g.updateBoard(3, 2)
        g.updateBoard(10, 7)
        g.updateBoard(0, 2)
        self.assertEqual(g.hasWon(0, 2), False)
        g.updateBoard(2, 7)
        g.updateBoard(1, 2)
        self.assertEqual(g.hasWon(1, 2), True)

    def test_hasWon_horizontal(self):
        g = Game()
        g.init()
        g.updateBoard(4, 2)
        g.updateBoard(0, 4)
        g.updateBoard(4, 1)
        g.updateBoard(10, 2)
        g.updateBoard(4, 4)
        g.updateBoard(10, 7)
        g.updateBoard(4, 5)
        self.assertEqual(g.hasWon(4, 5), False)
        g.updateBoard(2, 7)
        g.updateBoard(4, 3)
        self.assertEqual(g.hasWon(4, 3), True)

    def test_hasWon_diagonal1(self):
        g = Game()
        g.init()
        g.updateBoard(2, 3)
        g.updateBoard(0, 4)
        g.updateBoard(4, 5)
        g.updateBoard(10, 2)
        g.updateBoard(5, 6)
        g.updateBoard(10, 7)
        g.updateBoard(6, 7)
        self.assertEqual(g.hasWon(6, 7), False)
        g.updateBoard(2, 7)
        g.updateBoard(3, 4)
        self.assertEqual(g.hasWon(3, 4), True)

    def test_hasWon_diagonal2(self):
        g = Game()
        g.init()
        g.updateBoard(5, 3)
        g.updateBoard(0, 4)
        g.updateBoard(4, 4)
        g.updateBoard(10, 2)
        g.updateBoard(1, 7)
        g.updateBoard(10, 7)
        g.updateBoard(3, 5)
        self.assertEqual(g.hasWon(3, 5), False)
        g.updateBoard(2, 7)
        g.updateBoard(2, 6)
        self.assertEqual(g.hasWon(2, 6), True)
        self.assertEqual(g.getWinner(), Side.BLACK)
