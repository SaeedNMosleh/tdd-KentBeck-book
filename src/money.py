from abc import ABC, abstractmethod

class Money:
    def __init__(self,amount) -> None:
        self._amount = amount
    # Sample equal method -> it needs to be replaced with __eq__
    def equal(self, other):
        return self._amount == other._amount if type(self) is type(other) else False
    
    @classmethod
    def dollar(cls,amount):
        return Dollar(amount)
    
    @classmethod
    def franc(cls,amount):
        return Franc(amount)

    @abstractmethod
    def times(self, multiplier):
        pass


class Dollar(Money): 
    def __init__(self,amount) -> None:
        super().__init__(amount)        
    def times(self,multiplier):
        #self.amount *= multiplier
        return Dollar(self._amount*multiplier)


class Franc(Money):
    def __init__(self,amount) -> None:
        super().__init__(amount)
    def times(self,multiplier):
        #self.amount *= multiplier
        return Franc(self._amount*multiplier)
    