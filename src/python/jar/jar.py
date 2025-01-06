import sys

class Jar:

    def __init__(self, size =0, capacity=12):

        self._capacity = capacity
        self._size = size

        if not capacity > 0:
            raise ValueError
        

    def __str__(self):
        n = self.size
        print(n)

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
    def deposit(self, n):
        self._size += n

    def withdraw(self, n):
        self._size -= n


def main():
    try:
        jar = Jar(3)
        print (jar.size)
        jar.deposit(1)
        print(jar.size)
        jar.withdraw(1)
        print(jar.size)

    except ValueError:
        sys.exit('ValueError')

if __name__ == "__main__":
    main()