from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar(3, 10)
    assert str(jar) == '🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

def test_withdraw():
    jar = Jar(2)
    jar.withdraw(1)
    assert jar.size == 1