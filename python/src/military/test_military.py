from hours import military_time
import pytest
import sys

def test_convert_a():
    assert military_time('9 AM to 5 PM') == '09:00 to 17:00'
    assert military_time('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert military_time('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert military_time('10:30 PM to 8:00 AM') == '22:30 to 08:00'
    assert military_time('12:00 AM to 5:59 PM') == '00:00 to 17:59'


def test_convert_b():
    with pytest.raises(SystemExit):
        military_time('9:30 to 5:30')
    with pytest.raises(SystemExit):
        military_time('9 AM - 5 PM')
    with pytest.raises(SystemExit):
        military_time('09:00 AM - 17:00')
    with pytest.raises(SystemExit):
        military_time('9:60 AM to 5:59 PM')
    with pytest.raises(SystemExit):
        military_time('13:00 PM to 13:00 AM')