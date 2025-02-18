from ipcheck import validate


def test_validate_true():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True


def test_validate_false():
    assert validate("cat") == False
    assert validate("256.255.255.255") == False
    assert validate("111.111.111.111111111") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.256.1.1") == False
    assert validate("256.1.1.1") == False
