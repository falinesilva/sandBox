from numb3rs import validate

def test_validate_true():
    assert validate('1.2.3.4') == 'True'
    assert validate('255.255.255.255') == 'True'

def test_validate_false():
    assert validate('cat') == 'False'
    assert validate('256.255.255.255') == 'False'
