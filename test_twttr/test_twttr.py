import twttr
from twttr import shorten

def test_shorten():
    assert shorten("HELLO") == "HLL"
    assert shorten("hello") == "hll"
    assert shorten("Hi 123") == "H"
