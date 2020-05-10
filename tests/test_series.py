from math_series.series import sum_series

def test_sum_fib_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_luc_zero():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum_fib_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_luc_one():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected

def test_sum_fib_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_luc_two():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_fib_three():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_luc_three():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected