from abc import ABC, abstractmethod
from typing import Self

class Money(ABC):
    def __init__(self,amount,currency) -> None:
        self._amount = amount
        self._currency = currency        
    # Sample equal method -> it needs to be replaced with __eq__
    def equal(self, other):
        return self._amount == other._amount if type(self) is type(other) else False
    
    @classmethod
    def dollar(cls,amount):
        return Dollar(amount,currency="USD")
    
    @classmethod
    def franc(cls,amount):
        return Franc(amount,currency="CHF")

    @abstractmethod
    def times(self, multiplier) -> Self:
        pass

    def currency(self) -> str:
        return self._currency


class Dollar(Money): 
    def __init__(self,amount,currency) -> None:
        super().__init__(amount,currency)        
                
    def times(self,multiplier):
        #self.amount *= multiplier
        return Money.dollar(self._amount*multiplier)



class Franc(Money):
    def __init__(self,amount,currency) -> None:
        super().__init__(amount,currency)
       
        
    def times(self,multiplier):
        #self.amount *= multiplier
        return Money.franc(self._amount*multiplier)

