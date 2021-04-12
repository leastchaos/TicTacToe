import random
import numpy as np


class BaseAgent():
    def __init__(self, game, player):
        self.player = player
        self.game = game

    def strategy(self):
        return (0, 0)

    def action(self):
        x, y = self.strategy()
        self.game.place_turn(self.player, x, y)

    def get_board(self):
        return self.game.board

    def get_empty_spaces(self):
        return self.game.get_empty_spaces()

    def print_board(self):
        self.game.print_board()


class HumanAgent(BaseAgent):
    def strategy(self):
        self.print_board()
        while True:
            x = int(input('input x coordinate: '))
            y = int(input('input y coordinate: '))
            if (x, y) in self.get_empty_spaces():
                return x, y


class RandomAgent(BaseAgent):
    def strategy(self):
        empty_spaces = self.game.get_empty_spaces()
        return empty_spaces[random.randint(0, np.max([len(empty_spaces)-1, 0]))]
