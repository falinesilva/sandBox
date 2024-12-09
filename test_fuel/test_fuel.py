from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("50/100") == 50
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
          convert("cat")
    with pytest.raises(ValueError):
          convert("101/100")
    with pytest.raises(ValueError):
          convert("2/1")
    with pytest.raises(ValueError):
          convert("cat/dog")
    with pytest.raises(ValueError):
          convert("600/1")
    with pytest.raises(ValueError):
          convert("-")
    with pytest.raises(ValueError):
          convert("-1/-1")
    with pytest.raises(ValueError):
          convert("2.5/3.5")

def test_convert_zer0():
      with pytest.raises(ZeroDivisionError):
          convert("1/0")

def test_gauge():
     assert gauge(-1) == "E"
     assert gauge(1) == "E"
     assert gauge(0) == "E"
     assert gauge(100) == "F"
     assert gauge(120) == "F"
     assert gauge(60) == "60%"
     assert gauge(99) == "F"
