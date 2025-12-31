from abc import ABC, abstractmethod
from typing import Self

class Money():
    def __init__(self,amount,currency) -> None:
        self._amount = amount
        self._currency = currency        
    # Sample equal method -> it needs to be replaced with __eq__
    def equal(self, other):
        return self._amount == other._amount if self._currency == other._currency else False
    
    @classmethod
    def dollar(cls,amount):
        return Dollar(amount,currency="USD")
    
    @classmethod
    def franc(cls,amount):
        return Franc(amount,currency="CHF")

    
    def times(self, multiplier):
        return Money(self._amount* multiplier, self._currency)

    def currency(self) -> str:
        return self._currency


class Dollar(Money): 
    def __init__(self,amount,currency) -> None:
        super().__init__(amount,currency)
        self._currency = currency        
                

class Franc(Money):
    def __init__(self,amount,currency) -> None:
        super().__init__(amount,currency)
        self._currency = currency
        
