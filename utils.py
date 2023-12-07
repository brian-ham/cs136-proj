def valuation_generation():
    '''
    list -> list: Creates initial valuations for agents
    
    uses performance from past year as a mean + adds some variance to each player
    '''
    #TODO

def price_init():
    '''
    list -> list: Creates initial prices for players
    
    uses performance from past year, takes into account Value for a certain position:
    i.e. if a player is a lot better than the average player at his position, he will be more expensive
    use # of standard deviations above mean for a certain position as a multiplier for price

    total budget is $100 for 8 players (1QB, 2RB, 2WR, 1TE, 1DST, 1K)
    '''

    #TODO

def price_fluc():
    '''
    list -> list: Creates price fluctuations for players based on week's performance
    '''