import sys
import math
from utils import *
from constants import *

class ShortTermAgent:
    '''
    Agent that makes reactionary decisions, i.e. values players based on their performance in just the past week
    '''
    def __init__(self, vals):
        self.vals = vals

    def player_prices(self, history):
        '''
        Should return a dict of players -> prices that this agent values each player on their team at.
        '''
        return {}

    def player_bids(self, history):
        '''
        Should return a dict of players -> prices that this agent wants to buy.
        '''
        return {}

    ## Delete this. Implement the strategy in player_prices and player_bids. Each round, player_prices() is called first for all agents,
    ## then, player_bids is called for all agents, then the mechanism performs trading/buying. For AMM, if you don't want to sell a player,
    ## set the price value to very high. If you definitely want to sell a player, set it to 0. A player will be sold back to the market 
    ## if the ask price is lower than the market price (you will get the market price back) (haha jk keep track of your own budget).
    def run():

        # PSEUDOCODE:

        # get this round's history

        # update self.vals based on this round's performance
            # exactly how you update depends on the type of agent. more reactionary agent = more weight on this round's performance

        # sort players by valuation

        # make transactions accordingly, depending on whether it's budget or draft, as long as you can pay transaction fee

        # update team
        pass

class LongTerm:
    '''
    Agent that makes decisions based on long-term performance, i.e. sticks to past season's performance for valuation
    '''
class AFK:
    '''
    Agent that participates in the draft but does not make any decisions
    '''
class Random:
    '''
    Makes quirky decisions
    '''

class SmartAgent:
    '''
    ?
    '''