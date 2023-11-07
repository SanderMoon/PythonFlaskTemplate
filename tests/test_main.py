"""Tests some sample method."""

from src.math_example import add_numbers


def test_add_numbers():
    """Tests some sample method from math_example.py."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-5, -7) == -12
