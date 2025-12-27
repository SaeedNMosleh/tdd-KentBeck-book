from src.money import Dollar, Franc, Money
def testMultiplication():
    five = Money.dollar(5)
    assert five.times(2).equal(Money.dollar(10))
    assert five.times(3).equal(Money.dollar(15))

def testEquality():
    assert Money.dollar(5).equal(Money.dollar(5))
    assert not Money.dollar(5).equal(Money.dollar(6))
    assert Money.franc(5).equal(Money.franc(5))
    assert not Money.franc(5).equal(Money.franc(6))
    assert not Money.franc(5).equal(Money.dollar(5))
    

def testFrancMultiplication():
    five = Money.franc(5)
    assert five.times(2).equal(Money.franc(10))
    assert five.times(3).equal(Money.franc(15))
