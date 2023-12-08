import pandas as pd

from agents import *
from mechanism import AMM, CDA
from history import History
from utils import *

def run_amm(agents, player_df):
    history = History()
    history.add(player_df["Price"])
    prev_teams = []
    for i in range(1, 15):
        print("round", len(history.prices))
        mech = AMM(history[-1])
        for agent in agents:
            agent.calculate_points(history)
            prev_teams.append(agent.team)
            asks = agent.player_prices(history)
            for (player, ask) in asks.items():
                if mech.sell_player(player, ask):
                    agent.team.remove(player)
                    agent.remaining_budget += history[-1][player]
            bids = agent.player_bids(history)
            for (player, bid) in bids.items():
                if mech.buy_player(player, bid):
                    agent.team.append(player)
                    agent.remaining_budget -= history[-1][player]
            
        new_prices = price_fluc(agents, prev_teams, history[-1])
        prev_teams = []
        history.add(new_prices)

    for agent in agents:
        print(type(agent), "%.2f" % agent.total_score)

    return history

def run_cda(agents):
    history = History()
    history.add(player_df["Price"])
    prev_teams = []
    for i in range(1, 15):
        print("round", len(history.prices))
        mech = CDA(agents)
        for agent in agents:
            agent.calculate_points(history)
            prev_teams.append(agent.team)
            asks = agent.player_prices(history)
            for (player, ask) in asks.items():
                if mech.sell_player(agent, player, ask):
                    agent.team.remove(player)
                    agent.remaining_budget += history[-1][player]
            bids = agent.player_bids(history)
            for (player, bid) in bids.items():
                if mech.buy_player(agent, player, bid):
                    agent.team.append(player)
                    agent.remaining_budget -= history[-1][player]
            
        new_prices = price_fluc(agents, prev_teams, history[-1])
        prev_teams = []
        history.add(new_prices)

    for agent in agents:
        print(type(agent), "%.2f" % agent.total_score)

if __name__ == '__main__':
    mech_type = "CDA"
    player_df = pd.read_csv("data/2021/player_list.csv", index_col=0)
    num_players = 10

    # Agent generation
    agents = []
    if mech_type == "AMM":
        for i in range(num_players):
            vals = valuation_generation(player_df)
            if i < 2:
                agents.append(ShortTermAgent(vals))
            elif i < 4:
                agents.append(LongTermAgent(vals))
            elif i < 6:
                agents.append(AFKAgent(vals))
            elif i < 8:
                agents.append(RandomAgent(vals))
            elif i < 10:
                agents.append(SmartAgent(vals))
            team = team_selection_amm(vals, player_df)
            agents[i].team = team
            agents[i].remaining_budget = agents[i].remaining_budget - sum([player_df.loc[player]["Price"] for player in team])

        run_amm(agents, player_df)
    else:
        for i in range(num_players):
            vals = valuation_generation(player_df)
            if i < 2:
                agents.append(ShortTermAgent(vals))
            elif i < 4:
                agents.append(LongTermAgent(vals))
            elif i < 6:
                agents.append(AFKAgent(vals))
            elif i < 8:
                agents.append(RandomAgent(vals))
            elif i < 10:
                agents.append(SmartAgent(vals))
        
        teams = team_selection_draft(agents, player_df)

        for i in range(num_players):
            agents[i].team = teams[i]
        
        run_cda(agents)
