"""PyTest automatically runs any file with a name that starts with test_ .
So running command pytest will run all tests in this file.

Any function with a name that starts with test_ will be run as a test.

This file has two tests:
    1. test_add_one_plus_one: a test based on a specific example
    2. test_add_zero: a test based on a general property of the function
"""

from hypothesis import given, strategies as st

# Module to test
import lib

# Test based on specific example
def test_add_one_plus_one():
    assert lib.plus(1, 1) == 2

# Test based on general property of function
@given(st.integers())
def test_add_zero(x):
    """Given any random integer x, test if x + 0 == x and 0 + x == x"""
    assert lib.plus(x, 0) == x
    assert lib.plus(0, x) == x