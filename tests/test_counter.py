from lib.counter import *

def test_counter_with_0() :
    new_counter = Counter() 
    new_counter.add(0)
    result = new_counter.report()
    assert result == "Counted to 0 so far."

def test_counter_with_10() :
    new_counter = Counter() 
    new_counter.add(10)
    result = new_counter.report()
    assert result == "Counted to 10 so far."

def test_counter_with_minus100() :
    new_counter = Counter() 
    new_counter.add(-100)
    result = new_counter.report()
    assert result == "Counted to -100 so far."

def test_counter_with_58372() :
    new_counter = Counter() 
    new_counter.add(58372)
    result = new_counter.report()
    assert result == "Counted to 58372 so far."