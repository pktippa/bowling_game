import unittest

from bowling.game import Game

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_strike(self):
        self.game(3)
        self.game.add_throw(10)
        self.game.add_throw(5)
        self.game.add_throw(4)
        self.game.add_throw(10)
        self.assertEqual(self.game.get_total(), 58)
    
    def test_exception(self):
        self.game(3)
        self.game.add_throw(5)
        self.game.add_throw(4)
        # Adding exception case scenario
        self.game.add_throw(11)
        self.game.add_throw(1)
        self.game.add_throw(8)
        self.assertRaises(Exception, self.game.get_total)

    def test_sparse(self):
        self.game(3)
        self.game.add_throw(5)
        self.game.add_throw(4)
        self.game.add_throw(9)
        self.game.add_throw(1)
        self.game.add_throw(8)
        self.game.add_throw(2)
        self.assertEqual(self.game.get_total(), 45)


if __name__ == '__main__':
    unittest.main()
