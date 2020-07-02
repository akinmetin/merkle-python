import pytest
from Problem1 import Time
from Problem2 import findTheLongest
from Problem3 import secondLowest
from Problem4 import balance


def test_timeString():
    myclass = Time(1, 30, 20)
    assert myclass.timeString() == "01:30:20"


def test_scale():
    myclass = Time(1, 30, 20)
    myclass.scale(400)
    assert myclass.timeString() == "01:37:00"


def test_normalise():
    mynewclass = Time(1, 100, 0)
    assert mynewclass.timeString() == "02:40:00"


@pytest.mark.parametrize("test_input, expected", [
    ("dghhhmhmx", ("h", 3)),
    ("dhkkhhKKKt", ("k", 3)),
    ("aBbBadddadd", ("b", 3)),
])
def test_findTheLongest(test_input, expected):
    assert findTheLongest(test_input) == expected


@pytest.mark.parametrize("test_input2, expected2", [
    ([4, 3, 1, 1, 2], 1),
    ([4, 3, 1, 1, 2, 2], 2),
    ([4, 3, 1, 2], 2),
])
def test_secondLowest(test_input2, expected2):
    assert secondLowest(test_input2) == expected2


@pytest.mark.parametrize("openingSum, interestRate, taxFreeLimit, taxRate, numMonths, expected3", [
    (10000, 1, 20000, 1, 2, 10201),
    (25000, 2, 20000, 1, 2, 25904.5),
    (19800, 2, 20000, 1, 2, 20597.96),
])
def test_balance(openingSum, interestRate, taxFreeLimit, taxRate, numMonths, expected3):
    assert balance(openingSum, interestRate, taxFreeLimit, taxRate, numMonths) == expected3
