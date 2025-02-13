import plates
from plates import is_valid

def test_middle():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("AAAAAA") == True

def test_initial():
    assert is_valid("50CS") == False
    assert is_valid("123") == False
    assert is_valid("ABC") == True

def test_alphanum():
    assert is_valid("HI.BYE") == False
    assert is_valid("PI3.14") == False
