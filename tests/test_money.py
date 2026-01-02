from src.money import Money, Bank, Expression, Sum
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
    
def testCurrency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()

def testSimpleAddition():
    five = Money.dollar(5)
    sum = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10).equal(reduced)

def testPlusReturnSum():
    five = Money.dollar(5)
    result: Expression = five.plus(five)
    sum : Sum = result
    assert five.equal(sum.augend)
    assert five.equal(sum.addend)

def testReduceSum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert Money.dollar(7).equal(result)

def testReduceMoney():
    bank = Bank()
    result : Money = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1).equal(result)