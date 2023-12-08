class AMM:
    def __init__(self):
        self.player_pool = [] # Map from players to ask price

    def buy_player(self, player, bid):
        if player not in self.player_pool:
            # Error
            pass
        
        if bid >= self.player_pool[player]:
            # Give
            pass
    
    def sell_player(self, player, ask):
        pass

class CDA:
    def __init__(self):
        pass

    def buy_player(self, player, bid):
        pass

    def sell_player(self, player, ask):
        pass
