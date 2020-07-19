from ls16 import *


def test_base_converter():
    assert base_converter([7], 10, 2) == [1, 1, 1]
    assert base_converter([2, 4], 10, 3) == [2, 2, 0]


def test_calculate_digit_and_remainder():
    assert calculate_remainder_and_digit([6, 0], 10, 10, 1) == ([0, 0], 6)
    assert calculate_remainder_and_digit([1, 7], 10, 3, 4) == ([1, 7], 0)
    assert calculate_remainder_and_digit([1, 2, 1], 3, 10, 1) == ([0, 2, 0], 1)


def test_pow_base():
    assert pow_base(10, 2, 2) == [4]
    assert pow_base(2, 10, 0) == [1]
    assert pow_base(3, 3, 3) == [1, 0, 0, 0]


def test_convert_to_list():
    assert convert_to_list(1, 10) == [1]
    assert convert_to_list(4, 2) == [1, 0, 0]


def test_compare():
    assert compare([1, 0], [0, 5]) == 1
    assert compare([2, 0, 5], [2, 0, 5]) == 0
    assert compare([8, 0, 4], [9, 9, 9]) == -1
