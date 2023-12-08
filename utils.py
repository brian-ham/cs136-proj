import numpy as np
import pandas as pd
from constants import *
budget = 20

player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)

def valuation_generation():
    '''
    list -> list: Creates initial valuations for agents
    
    uses performance from past year as a mean + adds some variance to each player
    '''
    # first column: ID, second column: PERCEIVED value, third column: ACTUAL value
    vals = {}

    # create Dict of perceived values
    for (idx, row) in player_df.iterrows():
        vals[idx] = row.Value + np.random.normal(0, 5)
    return vals

def team_selection_amm(vals, players):
    '''
    list -> list: Creates team selection for agents using AMM

    uses valuation generation to get initial valuations for players
    selects players greedily by value-per-dollar
    '''

    # Add perceived values to the players df (which is indexed by the Player name)
    # initialize new column Perceived Value
    players["Perceived Value"] = 0
    for name in players.index:
        players.loc[name, "Perceived Value"] = vals[name]

    players = players.sort_values(by="Perceived Value", ascending=False)

    # for row in players:
    #     print(row.name, row.position, row.price)
    team = []
    remaining_budget = budget
    remaining_positions = positions_limit.copy()
    print("index:", players.index)
    # Select players greedily while staying within budget and position limits
    for (idx, player) in players.iterrows():
        if (
            player["Price"] <= remaining_budget
            and remaining_positions[player["Position"]] > 0
        ):
            # append player's index
            team.append(idx)

            remaining_budget -= player["Price"]
            remaining_positions[player["Position"]] -= 1

        if len(team) == 14:
            break

    return team

def team_selection_draft(agents, values, players):
    '''
    #NOTE: need to do in the simulation? since we need to divide up the players among all the agents;
            can't be independently decided for each agent.
    #NOTE: or pass in the agents here
    '''


def price_fluc():
    '''
    list -> list: Creates price fluctuations for players based on week's performance
    '''
    # TODO
    pass

if __name__ == "__main__":
    # Just for testing purposes. Can delete later
    vals = valuation_generation()
    print(vals)
    team = team_selection_amm(vals, player_df)
    print("Team:")
    for player in team:
        print("Player:" + str(player))
    print(team)