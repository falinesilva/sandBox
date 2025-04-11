
import vowels
from vowels import shorten

def test_vowels():
    assert shorten("HELLO") == "HLL"
    assert shorten("hello") == "hll"
    assert shorten("Hi 123") == "H 123"
    assert shorten("hello, world") == "hll, wrld"
