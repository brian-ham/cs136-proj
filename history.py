import numpy

class History:
    def __init__(self):
        self.prices = []
    
    def add(self, new_prices):
        to_add = {}
        for player, price in new_prices.items():
            if type(price) == numpy.float64 or type(price) == float:
                to_add[player] = price
            else:
                to_add[player] = price[0]
        
        self.prices.append(to_add)

    def round(self):
        return len(self.prices)
    
    def __getitem__(self, key):
        return self.prices[key]
