class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            self._size = self._size + n

        if self.size + n > self.capacity:
            raise ValueError("Exceeded. No more capacity.")

        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("No more cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    print(str(jar))


if __name__ == "__main__":
    main()
