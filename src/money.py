from typing import Protocol

class Expression(Protocol):
    def reduce(self,to):
        pass

class Bank(Expression):
    def __init__(self) -> None:
        pass
    def reduce(self,source: Expression, to):
        return source.reduce(to)
class Sum(Expression):
    def __init__(self, augend: "Money", addend: "Money") -> None:
        self.augend = augend
        self.addend = addend
    def reduce(self,to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)

class Money(Expression):
    def __init__(self,amount,currency) -> None:
        self._amount = amount
        self._currency = currency        
    # Sample equal method -> it needs to be replaced with __eq__
    def equal(self, other):
        return self._amount == other._amount if self._currency == other._currency else False
    
    @classmethod
    def dollar(cls,amount):
        return Money(amount,currency="USD")
    
    @classmethod
    def franc(cls,amount):
        return Money(amount,currency="CHF")

    
    def times(self, multiplier):
        return Money(self._amount* multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self,addend):
        return Sum(self, addend)       
    def reduce(self, to):
        return self
