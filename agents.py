import sys
import math
from utils import *
from constants import *
from history import History

class ShortTermAgent:
    '''
    Agent that makes reactionary decisions, i.e. values players based on their performance in just the past week
    '''
    def __init__(self, vals, team):
        # first column: ID, second column: PERCEIVED value
        self.vals = vals
        self.team = team
        self.budget = 20

    def player_prices(self, history):
        '''
        Should return a dict of players -> prices that this agent values each player on their team at.
        '''
        player_prices = {}
        for player in self.team:
            player_prices[player] = self.vals[player]
        return player_prices

    def player_bids(self, history):
        '''
        Should return a dict of players -> prices that this agent wants to buy.
        '''
        player_df = pd.read_csv("data/2022/by_weeks/week_"+str(len(history) + 1), index_col=0)

        learning_rate = 0.9
        for player in self.vals:
            self.vals[player] = (1 - learning_rate)*self.vals[player] + learning_rate*player_df.loc[player]["FPTS"]/20.0

        bids = {}
        for player in self.vals:
            if self.vals[player] > history[player]:
                bids[player] = self.vals[player]

        return bids

    ## Delete run function. Implement the strategy in player_prices and player_bids. Each round, player_prices() is called first for all agents,
    ## then, player_bids is called for all agents, then the mechanism performs trading/buying. For AMM, if you don't want to sell a player,
    ## set the price value to very high. If you definitely want to sell a player, set it to 0. A player will be sold back to the market 
    ## if the ask price is lower than the market price (you will get the market price back) (haha jk keep track of your own budget).


        

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