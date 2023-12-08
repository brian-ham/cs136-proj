import random
import numpy as np
import pandas as pd
from constants import *
budget = 20

def valuation_generation(player_df):
    '''
    list -> list: Creates initial valuations for agents
    
    uses performance from past year as a mean + adds some variance to each player
    '''
    # first column: ID, second column: PERCEIVED value
    vals = {}

    # create Dict of perceived values
    for (idx, row) in player_df.iterrows():
        vals[idx] = row.Price + np.random.normal(0, 1)
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
    # Select players greedily while staying within budget and position limits
    for (idx, player) in players.iterrows():
        if (
            player["Price"] <= remaining_budget and
            remaining_positions[player["Position"]] > 0
        ):
            # append player's index
            team.append(idx)

            remaining_budget -= player["Price"]
            remaining_positions[player["Position"]] -= 1

        if len(team) == 14:
            break

    return team

def team_selection_draft(agents, players):
    '''
    list -> list: Creates team selection for agents using draft

    uses valuation generation to get initial valuations for players
    selects players greedily by value-per-dollar
    '''

    available_players = players.copy()
    agent_prefs = []
    remaining_positions = []
    teams = []
    for agent in agents:
        teams.append([])
        remaining_positions.append(positions_limit.copy())
        # Add perceived values to the players df (which is indexed by the Player name)
        # initialize new column Perceived Value
        players["Perceived Value"] = 0
        for name in players.index:
            players.loc[name, "Perceived Value"] = agent.vals[name]

        agent_prefs.append(players.sort_values(by="Perceived Value", ascending=False))

    # Generate a random draft order.
    draft_order = list(range(len(agents)))
    random.shuffle(draft_order)
    num_rounds = sum(positions_limit.values())

    # Assumes there will be enough players to fill all positions in all teams.
    for _ in range(num_rounds):
        for agent_idx in draft_order:
            # Let agent j in the draft order get their currently top pick
            for (idx, player) in agent_prefs[agent_idx].iterrows():
                if idx in available_players.index and remaining_positions[agent_idx][player["Position"]] > 0:
                    teams[agent_idx].append(idx)
                    available_players.drop(idx, inplace=True)
                    remaining_positions[agent_idx][player["Position"]] -= 1
                    agent_prefs[agent_idx].drop(idx, inplace=True)
                    break

    return teams

def price_fluc():
    '''
    list -> list: Creates price fluctuations for players based on week's performance
    '''
    # TODO
    pass

if __name__ == "__main__":
    # Just for testing purposes. Can delete 
    # later
    player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)
    vals = valuation_generation(player_df)
    # print("vals:",vals)
    
    print("vals_adjusted:",vals+vals+vals)
    print(player_df)
    team = team_selection_amm(vals, player_df)
    print("Team:")
    for player in team:
        print("Player: " + str(player), "Position: " + player_df.loc[player]["Position"])
    print(team)