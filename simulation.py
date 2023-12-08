import pandas as pd

from agents import ShortTermAgent
from mechanism import AMM, CDA
from utils import *

if __name__ == '__main__':
    mech_type = "CDA"
    player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)
    num_players = 8

    agents = []
    if mech_type == "AMM":
        mech = AMM()
        for i in range(num_players):
            vals = valuation_generation(player_df)
            agents.append(ShortTermAgent(mech, vals))
            team = team_selection_amm(agents[i].get_valuation(), player_df)
            agents[i].set_team(team)
    else:
        mech = CDA()
        for i in range(num_players):
            vals = valuation_generation(player_df)
            agents.append(ShortTermAgent(mech, vals))
        
        teams = team_selection_draft(agents, player_df)

        for i in range(num_players):
            agents[i].set_team(teams[i])

    print(agents[0].team)
