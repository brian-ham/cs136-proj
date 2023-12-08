class History:
    def __init__(self):
        # I feel like this should be a dictionary of player : price. It is bro. It's a list of dataframes.
        # prices[0] represents the prices for all the players in week 0.
        self.prices = []
    
    def round(self):
        return len(self.prices)
    
    def __getitem__(self, key):
        return self.prices[key]
