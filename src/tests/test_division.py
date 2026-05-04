import pytest
from spacemed.division import divide


def test_division():
    ratio = divide(1, 2)
    assert ratio == 0.5


def test_divisionByZero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
