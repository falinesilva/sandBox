import sys
import pytest
from working import convert

def test_convert_a(): # Hour and minute conversion tests
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    #assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    #assert convert('10:30 PM to 8:00 AM') == '22:30 to 08:00'
    #assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    #assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    #assert convert('12:00 AM to 5:59 PM') == '00:00 to 17:59'


def test_convert_b(): # AM/PM format tests
    #with pytest.raises(ValueError): convert('9:30 to 5:30')
    #with pytest.raises(ValueError): convert('9 AM - 5 PM')
    #with pytest.raises(ValueError): convert('09:00 AM - 17:00')
    with pytest.raises(ValueError): convert('9 AM 5 PM')
    #with pytest.raises(ValueError): convert('9:00 AM 5 PM')
    #with pytest.raises(ValueError): convert("9 AM to 5:00 PM")



#def test_convert_c(): # Hour and minute range tests
    #with pytest.raises(ValueError): convert('9:60 AM to 5:59 PM')
    #with pytest.raises(ValueError): convert('13:00 PM to 13:00 AM')
