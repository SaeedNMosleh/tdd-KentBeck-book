from src.money import Dollar, Franc
def testMultiplication():
    five = Dollar(5)
    assert five.times(2).equal(Dollar(10))
    assert five.times(3).equal(Dollar(15))

def testEquality():
    assert Dollar(5).equal(Dollar(5))
    assert not Dollar(5).equal(Dollar(6))

def testFrancMultiplication():
    five = Franc(5)
    assert five.times(2).equal(Franc(10))
    assert five.times(3).equal(Franc(15))