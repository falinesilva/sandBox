import pytest
from um import count


def test_count_a():
    assert count("um") == 1


def test_count_b():
    assert count("Hi um, world!") == 1


def test_count_c():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks for the um...") == 2
