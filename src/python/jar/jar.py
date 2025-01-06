class Jar:

    def __init__(self, size=0, capacity=12):

        self._capacity = capacity
        self._size = size

    def __str__(self):
        n = self.size
        return "🍪" * n

    @property
    def capacity(self):
        if self._capacity < 0:
            raise ValueError
        return self._capacity

    @property
    def size(self):
        return self._size

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError

    def withdraw(self, n):
        self._size -= n
