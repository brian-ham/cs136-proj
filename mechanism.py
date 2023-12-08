import random
import pandas as pd
from constants import *

player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)

class AMM:
    def __init__(self, players):
        self.players = players

    def buy_player(self, player, bid):
        if bid >= self.players.loc[player]:
            return True

        return False
    
    def sell_player(self, player, ask):
        if ask <= self.players.loc[player]:
            return True
        
        return False
    
class CDA:
    def __init__(self, agents):
        self.player_bids = {}
        self.player_asks = {}
        self.agents = agents
        self.iters = 7 # number of random trade partners assigned to each agent

    def buy_player(self, agent, player, bid):

        if agent not in self.player_bids:
            self.player_bids[agent] = []
        self.player_bids[agent].append((player, bid))

    def sell_player(self, agent, player, ask):
        if agent not in self.player_asks:
            self.player_asks[agent] = []
        self.player_asks[agent].append((player, ask))

    def resolve_trades(self):
        '''
        Returns list of tuples of the form (agent1, player1, ask, agent2, player2, bid),
        where agent1 trades 
        '''
        for i in range(self.iters):
            random.shuffle(self.agents)
            for (i, agent1) in enumerate(self.agents):
                # don't do for the last agent
                if i == len(self.agents) - 1:
                    break
                for player_1 in agent1.team:
                    agent2 = self.agents[i+1]
                    for player_2 in agent2.team:

                        #if value of player_1 to agent is greater than value of player_2 to agent and vice versa
                        if player_1 not in player_df.index() or player_2 not in player_df.index():
                            continue

                        # if there is an agreement on price
                        if (
                            self.player_bids[agent1][player_2] > self.player_asks[agent2][player_2] and 
                            self.player_bids[agent2][player_1] > self.player_asks[agent1][player_1]
                        ):
                            # Check that the position requirements are still satisfied
                            pos1, pos2 = player_df[player_1]["Position"], player_df[player_2]["Position"]
                            agent1_pos_num = len([player for player in agent1.team if player_df[player]["Position"] == pos1])
                            agent2_pos_num = len([player for player in agent2.team if player_df[player]["Position"] == pos2])

                            if (
                                agent1.positions_lower_bound[pos1] <= agent1_pos_num - 1 and
                                agent2.positions_lower_bound[pos2] <= agent2_pos_num - 1
                            ):
                                agent1.team.remove(player_1)
                                agent1.team.append(player_2)
                                agent2.team.remove(player_2)
                                agent2.team.append(player_1)

        return