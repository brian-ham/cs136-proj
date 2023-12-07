from abc import ABC, abstractmethod

class Mechanism(ABC):
    _instance = None
    
    def __init__(self) -> None:
        raise RuntimeError("Call instance()")
        
    @classmethod
    def instance(cls):
        pass

    @abstractmethod
    def buy_player(self, player, bid):
        pass

    @abstractmethod
    def sell_player(self, player, ask):
        pass

class AMM(Mechanism):
    def __init__(self) -> None:
        super().__init__()
        self.liquidity = 0.2
    pass

class CDA(Mechanism):
    pass