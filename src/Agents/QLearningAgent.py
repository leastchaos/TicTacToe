import numpy as np
import random
import pickle
import itertools
import copy
class QLearningAgent():
    def __init__(self, game, player, policy_file=r'.\models\qlearning_policy.pkl',qlearning_dict=None,training=True):
        self.game=game
        self.file=policy_file
        self.player=player
        
        self.states=[]
        # default q learning
        self.lr=0.2
        self.exp_rate=0.3
        if not training:
            self.exp_rate=0
        self.decay_gamma=0.9
        self.win_value=1
        self.draw_value=0.1
        self.states_value = {}
        self.loadPolicy()

    def reset(self):
        self.states=[]

    def convert_to_hash(self,board):
        return ''.join(str(board[y][x]).zfill(2) for x,y in itertools.product(range(self.game.board_size),repeat=2))

    def get_player_turn(self):
        return self.game.player_turn

    def get_empty_spaces(self):
        return self.game.get_empty_spaces()

    def update_state(self):
        self.states.append(self.convert_to_hash(self.game.board))

    def strategy(self):
        empty_spaces = self.get_empty_spaces()
        
        if np.random.uniform(0, 1) <= self.exp_rate:
            return empty_spaces[random.randint(0, np.max([len(empty_spaces)-1, 0]))]
        value_max=-999
        
        for space in empty_spaces:
            x,y=space
            next_state=copy.deepcopy(self.game.board)
            next_state[y][x]=self.player
            next_state_hash=self.convert_to_hash(next_state)
            value=0 if self.states_value.get(next_state_hash) is None else self.states_value.get(next_state_hash)
            if value >= value_max:
                value_max=value
                next_action=space
            
        return next_action
    
    def action(self):
        x, y = self.strategy()
        self.game.place_turn(self.player, x, y)
        self.update()

    def get_reward(self):
        if self.game.game_end:
            victory=self.game.check_victory()
            if victory==self.player:
                return self.win_value
            if victory==-self.player:
                return -self.win_value
            if victory==0:
                return self.draw_value
        return False

    def update(self):
        self.update_state()
        reward=self.get_reward()
        if not reward:
            return
        self.loadPolicy()
        self.update_state_values(reward)
        self.savePolicy()

    def update_state_values(self,reward):

        for st in reversed(self.states):
            if self.states_value.get(st) is None:
                self.states_value[st] = 0
            self.states_value[st] += self.lr * (self.decay_gamma * reward - self.states_value[st])
            reward = self.states_value[st]

    def savePolicy(self):
        fw = open(self.file, 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def loadPolicy(self, file=None):
        if file is None:
            file=self.file
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()

if __name__=="__main__":
    z=QLearningAgent(None,1)