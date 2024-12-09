from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("50/100") == 50
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
          convert("cat")
          convert("101/100")
          convert("2/1")
          convert("cat/dog")
          convert("600/1")
          convert("-")
          convert("-1/-1")
    with pytest.raises(ZeroDivisionError):
          convert("1/0")
          convert("100/0")
def test_gauge():
     assert gauge(-1) == "E"
     assert gauge(1) == "E"
     assert gauge(0) == "E"
     assert gauge(100) == "F"
     assert gauge(120) == "F"
     assert gauge(60) == "60%"
     assert gauge(99) == "F"
