from typing import Protocol

class Expression(Protocol):
    def reduce(self,bank: "Bank", to) -> "Money":
        ...

class Bank():
    def __init__(self) -> None:
        self.rates = {}
    def addRate(self,from_currency: str,to : str, rate: int):
        self.rates[f"{from_currency}_{to}"] = rate
        
    def reduce(self,source: Expression, to):
        return source.reduce(self,to)
    def rate(self, fromm, to):
        key = f"{fromm}_{to}"
        if fromm == to:
            return 1
        elif key in self.rates:
            return self.rates[key]
        
        
class Sum(Expression):
    def __init__(self, augend: "Money", addend: "Money") -> None:
        self.augend = augend
        self.addend = addend
    def reduce(self,bank:Bank,to):
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
         
    def reduce(self, bank:Bank, to):
        rate = bank.rate(self.currency(), to)
        return Money(self._amount/rate, to)

class _Pair():
    def __init__(self, from_currency : str, to_currency: str):
        self.from_currency = from_currency
        self.to_currency = to_currency
    def equal(self, other):
        if not isinstance(other, _Pair):
            return False
        return self.from_currency == other.from_currency and self.to_currency == other.to_currency
    def hashCode(self):
        return 0
    
