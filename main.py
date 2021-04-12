from src.Board import TicTacToe
from src.Agents.CommonAgent import RandomAgent, HumanAgent

win, lose, draw = 0, 0, 0

for i in range(100):
    z = TicTacToe(board_size=5)
    p1 = RandomAgent(z, 1)
    p2 = HumanAgent(z, -1)
    agents = [p1, p2]
    i = 0
    while z.game_end == False:
        1
        agents[i].place_turn()
        i = (i+1) % 2
    if(z.winner == 1):
        win = win+1
    if(z.winner == -1):
        lose = lose+1
    if(z.winner == 0):
        draw = draw+1
print(win, lose, draw)
