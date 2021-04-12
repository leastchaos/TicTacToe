import numpy as np
from itertools import product
import random

class TicTacToe():
    def __init__(self, board_size=3, win=3, first_player=1):
        self.board = [[0 for i in range(board_size)]
                      for j in range(board_size)]
        self.board_size = int(board_size)
        self.win = win
        self.player_turn = first_player
        self.game_end = False
        self.winner = None

    def place_turn(self, player, x, y):
        if self.board[y][x]!=0:
            raise ValueError('InvalidMove')

        if self.player_turn !=player:
            raise ValueError('Not player turn')

        self.board[y][x] = player
        #self.print_board()
        self.player_turn = self.player_turn*-1
        self.check_game_state()
        return self.game_end


    def check_game_state(self):
        self.game_end = True
        if(self.check_victory() != 0):
            self.print_board()
            return
        if (self.check_draw()):
            self.print_board()
            return
        self.game_end = False

    def check_victory(self):
        col = np.sum(self.board, axis=0)
        row = np.sum(self.board, axis=1)
        diagonal_1 = np.trace(self.board)
        diagonal_2 = np.trace(np.fliplr(self.board))
        total = [*col, *row, diagonal_1, diagonal_2]
        if self.board_size in total:
            print('player 1 win')
            self.winner=1
            return 1
        if -self.board_size in total:
            print('player 2 win')
            self.winner=-1
            return -1
        return 0

    def get_empty_spaces(self):
        empty_spaces = [(x,y) for x,y in product(range(self.board_size),repeat=2) if self.board[y][x]==0 ]
        return empty_spaces
    
    def check_draw(self):
        all_board=[self.board[y][x] for x,y in product(range(self.board_size),repeat=2)]
        if 0 not in all_board:
            self.winner=0
            return True
        return False

    def print_board(self):
        print('game board:')
        for i in range(self.board_size):
            print('|'+'|'.join(str(x).zfill(2) for x in self.board[i])+'|')
    def reset(self, first_player=1):
        self.board = [[0 for i in range(self.board_size)]
                      for j in range(self.board_size)]
        self.player_turn = first_player
        self.game_end = False
        self.winner = None