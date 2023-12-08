import sys
import math
from utils import *
from constants import *
from abc import ABC, abstractmethod

player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)
class Agent(ABC):
    @abstractmethod
    def run(self):
        pass

class ShortTermAgent(Agent):
    '''
    Agent that makes reactionary decisions, i.e. values players based on their performance in just the past week
    '''
    def __init__(self, mech, vals):
        self.vals = valuation_generation() # a dictionary indexed by player name
        self.team = team_selection_amm(self.vals, player_df) # list of player names
        self.mech = mech

    def run():

        # PSEUDOCODE:

        # get this round's history

        # update self.vals based on this round's performance
            # exactly how you update depends on the type of agent. more reactionary agent = more weight on this round's performance

        # sort players by valuation

        # make transactions accordingly, depending on whether it's budget or draft, as long as you can pay transaction fee

        # update team
        pass

class LongTerm(Agent):
    '''
    Agent that makes decisions based on long-term performance, i.e. sticks to past season's performance for valuation
    '''
class AFK(Agent):
    '''
    Agent that participates in the draft but does not make any decisions
    '''
class Random(Agent):
    '''
    Makes quirky decisions
    '''

class SmartAgent(Agent):
    '''
    ?
    '''