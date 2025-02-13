from gastank import fuel

def test_fuel_1():
    assert fuel("50/100") == "50%"
    assert fuel("99/100") == "F"

def test_fuel_2():
     assert fuel("0/1") == "E"
     assert fuel("1/100") == "E"
     assert fuel("100/100") == "F"
     assert fuel("60/100") == "60%"
     assert fuel("99/100") == "F"
