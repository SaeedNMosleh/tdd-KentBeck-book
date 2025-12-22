def test_multiplication():
    from src.money import Dollar
    five = Dollar(5)
    five.times(2);
    assert five.amount == 10 
