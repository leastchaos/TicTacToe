from src.Board import TicTacToe
from src.Agents.CommonAgent import RandomAgent, HumanAgent
from src.Agents.QLearningAgent import QLearningAgent

win, lose, draw = 0, 0, 0

for i in range(100000):
    z = TicTacToe(board_size=3,show_win=False)
    p1 = QLearningAgent(z,1,training=True)
    p2 = HumanAgent(z,-1)
    agents = [p1, p2]
    i = 0
    while z.game_end == False:
        agents[i].action()
        i = (i+1) % 2
