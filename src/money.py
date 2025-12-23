class Dollar:
    def __init__(self,amount) -> None:
        self.amount = amount
    def times(self,multiplier):
        #self.amount *= multiplier
        return Dollar(self.amount*multiplier)
    # Sample equal method -> it needs to be replaced with __eq__
    def equal(self, other):
        return self.amount == other.amount if isinstance(other, Dollar) else False
