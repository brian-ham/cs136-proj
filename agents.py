import sys
import math
from utils import *
from constants import *
from abc import ABC, abstractmethod

player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)

class Agent(ABC):
    @abstractmethod
    def get_valuation(self):
        pass

    @abstractmethod
    def run(self):
        pass

class ShortTermAgent(Agent):
    '''
    Agent that makes reactionary decisions, i.e. values players based on their performance in just the past week
    '''
    def __init__(self, mech, vals):
        self.vals = vals
        self.mech = mech

    def get_valuation(self):
        '''
        Should only be used for drafting initialization.
        '''
        return self.vals

    def set_team(self, team):
        '''
        Should only be used for drafting initialization.
        '''
        self.team = team

    def run():

        # PSEUDOCODE:

        # get this round's history

        # update self.vals based on this round's performance
            # exactly how you update depends on the type of agent. more reactionary agent = more weight on this round's performance

        # sort players by valuation

        # make transactions accordingly, depending on whether it's budget or draft, as long as you can pay transaction fee

        # update team
        pass
    
    def __repr__(self) -> str:
        return str(self.team)

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