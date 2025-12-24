class Moeny:
    def __init__(self,amount) -> None:
        self._amount = amount

class Dollar(Moeny): 
    def __init__(self,amount) -> None:
        super().__init__(amount)        
    def times(self,multiplier):
        #self.amount *= multiplier
        return Dollar(self._amount*multiplier)
    # Sample equal method -> it needs to be replaced with __eq__
    def equal(self, other):
        return self._amount == other._amount if isinstance(other, Dollar) else False

class Franc:
    def __init__(self,amount) -> None:
        self.__amount = amount
    def times(self,multiplier):
        #self.amount *= multiplier
        return Franc(self.__amount*multiplier)
    # Sample equal method -> it needs to be replaced with __eq__
    def equal(self, other):
        return self.__amount == other.__amount if isinstance(other, Franc) else False