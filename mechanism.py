class AMM:
    def __init__(self, players):
        self.players = players

    def buy_player(self, player, bid):
        if bid >= self.players.loc[player]:
            return True

        return False
    
    def sell_player(self, player, ask):
        if ask <= self.players.loc[player]:
            return True
        
        return False
    
class CDA:
    def __init__(self):
        self.player_bids = {}
        self.player_asks = {}

    def buy_player(self, agent, player, bid):
        if player not in self.player_bids:
            self.player_bids[player] = []
        self.player_bids[player].append((agent, bid))

    def sell_player(self, agent, player, ask):
        if player not in self.player_asks:
            self.player_asks[player] = []
        self.player_asks[player].append((agent, ask))

    def resolve_trades(self):
        '''
        Returns list of tuples of the form (agent1, player1, ask, agent2, player2, bid),
        where agent1 trades 
        '''
        