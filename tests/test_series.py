import pytest
from series import fibonacci, lucas, sum_series
# # 0, 1, 1, 2, 3, 5, 8, 13, ... fibonacci
# # 2, 1, 3, 4, 7, 11, 18, 29, ...lucas
def test_fibonacci_0():
    """test fibonacci value of 0 index"""
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fibonacci_1():
    """test fibonacci value of 1 index"""
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fibonacci_2():
    """test fibonacci value of 2 index"""
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_fibonacci_3():
    """test fibonacci value of 3 index"""
    expected = 2
    actual = fibonacci(3)
    assert actual == expected
    
def test_fibonacci_4():
    """test fibonacci value of 4 index"""
    expected = 3
    actual = fibonacci(4)
    assert actual == expected

def test_fibonacci_5():
    """test fibonacci value of 5 index"""
    expected = 5
    actual = fibonacci(5)
    assert actual == expected

def test_fibonacci_8():
    """test fibonacci value of 8 index"""
    expected = 21
    actual = fibonacci(8)
    assert actual == expected


def test_lucas_0():
    """test Lucas series value of index 0"""
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_lucas_1():
    """test Lucas series value of index 1"""
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_lucas_2():
    """test Lucas series value of index 2"""
    expected = 3
    actual = lucas(2)
    assert actual == expected

def test_lucas_3():
    """test Lucas series value of index 3"""
    expected = 4
    actual = lucas(3)
    assert actual == expected

def test_lucas_4():
    """test Lucas series value of index 4"""
    expected = 7
    actual = lucas(4)
    assert actual == expected

def test_lucas_7():
    """test Lucas series value of index 7"""
    expected = 29
    actual = lucas(7)
    assert actual == expected


def test_sum_series_default_values():
    '''test sum_series default values (0,1)'''
    expected = 21
    actual = sum_series(8)
    assert actual == expected

def test_sum_series_fib():
    '''test sum_series with passing Fibonacci's values (0,1) '''
    expected = 2
    actual = sum_series(3,0,1)
    assert actual == expected

def test_sum_series_lucas():
    '''test sum_series with passing Lucas's values (2,1)'''
    expected = 4
    actual = sum_series(3,2,1)
    assert actual == expected

def test_sum_series_different_series():
    '''test sum_series with passing different series values(5,5) '''
    expected = 10
    actual = sum_series(2,5,5)
    assert actual == expected


