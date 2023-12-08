class AMM:
    def __init__(self, players):
        self.players = players

    def buy_player(self, player, bid):
        if bid >= self.players.loc[player]["Price"]:
            return True

        return False
    
    def sell_player(self, player, ask):
        if ask <= self.players.loc[player]["Price"]:
            return True
        
        return False
    
class CDA:
    def __init__(self):
        pass

    def buy_player(self, player, bid):
        pass

    def sell_player(self, player, ask):
        pass
