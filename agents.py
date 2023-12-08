import sys
import math
from utils import *
from constants import *
from history import History

class ShortTermAgent:
    '''
    Agent that makes reactionary decisions, i.e. values players based on their performance in just the past week
    '''
    def __init__(self, vals):
        # first column: ID, second column: PERCEIVED value
        self.vals = vals
        self.team = team
        self.remaining_budget = 20
        self.total_score = 0

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
        player_df = pd.read_csv(f"data/2022/by_weeks/week_{history.round()}.csv", index_col=0)

        learning_rate = 0.9
        for player in self.vals:
            if player in player_df.index():
                self.vals[player] = (1 - learning_rate)*self.vals[player] + learning_rate*player_df.loc[player]["FPTS"]/20.0
            else:
                self.vals[player] = 0

        players_with_roles = {}
        for player in self.team:
            if player in player_df.index():
                players_with_roles[player] = player_df.loc[player]["Position"]

        bids = {}
        for player in self.vals:
            bid = False
            if player in player_df.index():
                comparable_players = [players_with_roles[owned_player] == player_df.loc[player]["Position"] for owned_player in players_with_roles]
                for comparable_player in comparable_players:
                    if self.vals[player] > self.vals[comparable_player]:
                        if history[-1].loc[player]["Price"] < history[-1].loc[comparable_player]["Price"]:
                            bid = True
                bids[player] = self.vals[player]

        return bids

    def calculate_points(self, history):
        '''
        list -> None: Calculates the total perofrmance scores in the past week for all players on self.team
        automatically adds this to self.total_score
        '''
        week_results = pd.read_csv(f"data/2022/by_weeks/week_{history.round()}.csv", index_col=0)
        weekly_score = 0
        for player in self.team:
            if player in week_results["Player"]:
                weekly_score += week_results.loc[player]["FPTS"]
                self.vals[player] = player_df.loc[player]["FPTS"]/20.0
        self.total_score += weekly_score

    ## Delete run function. Implement the strategy in player_prices and player_bids. Each round, player_prices() is called first for all agents,
    ## then, player_bids is called for all agents, then the mechanism performs trading/buying. For AMM, if you don't want to sell a player,
    ## set the price value to very high. If you definitely want to sell a player, set it to 0. A player will be sold back to the market 
    ## if the ask price is lower than the market price (you will get the market price back) (haha jk keep track of your own budget).


        

class LongTermAgent:
    '''
    Agent that makes decisions based on long-term performance, i.e. sticks to past season's performance for valuation
    '''

    def __init__(self, vals, team):
        # first column: ID, second column: PERCEIVED value
        self.vals = vals
        self.team = team
        self.remaining_budget = 20

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
        player_df = pd.read_csv("data/2022/by_weeks/week_"+str(history.round()), index_col=0)

        learning_rate = 0.05
        for player in self.vals:
            if player in player_df.index():
                self.vals[player] = (1 - learning_rate)*self.vals[player] + learning_rate*player_df.loc[player]["FPTS"]/20.0
            else:
                self.vals[player] = 0

        players_with_roles = {}
        for player in self.team:
            if player in player_df.index(): 
                players_with_roles[player] = player_df.loc[player]["Position"]

        bids = {}
        for player in self.vals:
            bid = False
            if player in player_df.index():
                comparable_players = [players_with_roles[owned_player] == player_df.loc[player]["Position"] for owned_player in players_with_roles]
                for comparable_player in comparable_players:
                    if self.vals[player] > self.vals[comparable_player]:
                        if history[-1].loc[player]["Price"] < self.remaining_budget + history[-1].loc[comparable_player]["Price"]:
                            bid = True
                bids[player] = self.vals[player]

        return bids

class AFKAgent:
    '''
    Agent that participates in the draft but does not make any decisions
    '''
    def __init__(self, vals, team):
        # first column: ID, second column: PERCEIVED value
        self.vals = vals
        self.team = team
        self.remaining_budget = 20

    def player_prices(self, history):
        player_prices = {}
        for player in self.team:
            player_prices[player] = 1000
        return player_prices

    def player_bids(self, history):
        return {}


class RandomAgent:
    '''
    Makes quirky decisions
    '''
    def __init__(self, vals, team):
        # first column: ID, second column: PERCEIVED value
        self.vals = vals
        self.team = team
        self.remaining_budget = 20

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
        player_df = pd.read_csv("data/2022/by_weeks/week_"+str(round), index_col=0)

        self.vals[player] = np.random.uniform(0, 2)*self.vals[player]

        players_with_roles = {}
        for player in self.team:
            if player in player_df.index():
                players_with_roles[player] = player_df.loc[player]["Position"]

        bids = {}
        for player in self.vals:
            bid = False
            if player in player_df.index():
                comparable_players = [players_with_roles[owned_player] == player_df.loc[player]["Position"] for owned_player in players_with_roles]
                for comparable_player in comparable_players:
                    if self.vals[player] > self.vals[comparable_player]:
                        if history[-1].loc[player]["Price"] < history[-1].loc[comparable_player]["Price"]:
                            bid = True
                bids[player] = self.vals[player]

        return bids

class SmartAgent:
    '''
    Similar to short term agent but more reasonable weights for a longer number of weeks
    '''
    def __init__(self, vals, team):
        # first column: ID, second column: PERCEIVED value
        self.vals = vals
        self.team = team
        self.remaining_budget = 20

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
        player_df = pd.read_csv("data/2022/by_weeks/week_"+str(history.round()), index_col=0)

        learning_rate = 0.7
        self.vals[player] = (1 - learning_rate)*self.vals[player]
        for player in self.vals:
            if player in player_df.index():
                for i in range(history.round()):
                    self.vals[player] = self.vals[player] + learning_rate/(history.round())*pd.read_csv("data/2022/by_weeks/week_"+str(i+1)).loc[player]["FPTS"]/20.0

        players_with_roles = {}
        for player in self.team:
            if player in player_df.index():
                players_with_roles[player] = player_df.loc[player]["Position"]

        bids = {}
        for player in self.vals:
            bid = False
            if player in player_df.index():
                comparable_players = [players_with_roles[owned_player] == player_df.loc[player]["Position"] for owned_player in players_with_roles]
                for comparable_player in comparable_players:
                    if self.vals[player] > self.vals[comparable_player]:
                        if history[-1].loc[player]["Price"] < self.remaining_budget + history[-1].loc[comparable_player]["Price"]:
                            bid = True
                bids[player] = self.vals[player]

        return bids