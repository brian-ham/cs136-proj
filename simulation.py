import pandas as pd

from agents import ShortTermAgent
from mechanism import AMM, CDA
from history import History
from utils import *

def run_amm(agents):
    history = History()
    for i in range(1, 15):
        ### TODO: Make csv's with prices for all the weeks.
        player_df = pd.read_csv(f"data/2022/by_weeks/week_{i}.csv", index_col=0)
        mech = AMM(player_df)
        for agent in agents:
            asks = agent.player_prices(history)
            for (player, ask) in asks:
                if mech.sell_player(player, ask):
                    agent.team.remove(player)
            bids = agent.player_bids(history)
            for (player, bid) in bids:
                if mech.buy_player(player, bid):
                    agent.team.append(player)
            
            history.prices.append(player_df["Price"])

            ### TODO: Figure out who won the week idk how to do this. Add to history in whatever way you want.

    return history

def run_cda(agents):
    pass

if __name__ == '__main__':
    mech_type = "AMM"
    player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)
    num_players = 8

    # Agent generation
    agents = []
    if mech_type == "AMM":
        for i in range(num_players):
            vals = valuation_generation(player_df)
            agents.append(ShortTermAgent(vals))
            team = team_selection_amm(vals, player_df)
            agents[i].team = team

        run_amm(agents)
    else:
        for i in range(num_players):
            vals = valuation_generation(player_df)
            agents.append(ShortTermAgent(vals))
        
        teams = team_selection_draft(agents, player_df)

        for i in range(num_players):
            agents[i].team = teams[i]
        
        run_cda(agents)
