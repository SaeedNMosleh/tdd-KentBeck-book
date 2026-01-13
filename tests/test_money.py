from src.money import Money, Bank, Expression, Sum, Bank
from typing import cast
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
    sum :Sum = cast(Sum,result)
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

def testReduceMoneyDifferentCurrency():
    bank = Bank()
    bank.addRate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1).equal(result)

def testArrayEquals():
    assert ["abc"] == ["abc"]

def testIdentityRate():
    bank = Bank()
    assert 1 == bank.rate("USD", "USD")

def testMixedAddition():
    fiveBucks : Expression = Money.dollar(5)
    tenFranc:Expression = Money.franc(10)
    bank = Bank()
    bank.addRate("CHF", "USD", 2)
    result : Money = bank.reduce(fiveBucks.plus(tenFranc), "USD")
    assert Money.dollar(10).equal(result)

def testSumPlusMoney():
    fiveBucks: Expression = Money.dollar(5)
    tenFrancs: Expression = Money.franc(10)
    bank = Bank()
    bank.addRate("CHF", "USD", 2)
    sum: Expression = Sum(fiveBucks, tenFrancs)
    result: Money = bank.reduce(sum.plus(fiveBucks), "USD")
    assert Money.dollar(15).equal(result)

def testSumTimes():
    fiveBucks : Expression = Money.dollar(5)
    tenfrancs : Expression = Money.franc(10)
    bank = Bank()
    bank.addRate("CHF", "USD", 2)
    sum : Expression = Sum(fiveBucks, tenfrancs).times(2)
    result : Money = bank.reduce(sum, "USD")
    assert Money.dollar(20).equal(result)

""" def testPlusSameCurrencyReturns():
    sum : Expression = Money.dollar(1).plus(Money.dollar(1))
    assert isinstance(sum, Money) """
