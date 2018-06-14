"""
Word Counter Kata

A function that, given a delimited string, returns a collection of all of the unique words in it
and the count of how many times they occurred.

Example::

    >>> word_count('boom bang boom')
    {'boom': 2, 'bang': 1}
"""
import sys

import pytest


def word_count(string):
    return {}


def test_one_word():
    assert word_count('boom') == {'boom': 1}


if __name__ == '__main__':
    pytest.main(sys.argv)
