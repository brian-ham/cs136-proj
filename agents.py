import sys
import math
from utils import *
from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def run(self):
        pass

class ShortTermAgent(Agent):
    '''
    Agent that makes reactionary decisions, i.e. values players based on their performance in just the past week
    '''
    def __init__(self, mech, vals):
        self.vals = valuation_generation()
        self.mech = mech

    def run():
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