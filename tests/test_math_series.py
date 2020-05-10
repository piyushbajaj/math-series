from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fib_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fib_100():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

##################################################

def test_luc_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_luc_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_luc_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_luc_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_luc_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_luc_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

##################################################

def test_sum_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

