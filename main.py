from typing import Self
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, handler: 'Handler' = None):
        self.next_handler = handler

    def set_next_handler(self, handler: 'Handler'):
        self.next_handler = handler

    @abstractmethod
    def handle(self, data): ...


class IntegerHandler(Handler):
    def handle(self, data):
        if not isinstance(data, int):
            raise TypeError('Input must be int')
        return self.next_handler.handle(data)


class FizzBuzzHandler(Handler):
    def handle(self, data):
        if data % 15 == 0:
            return 'FizzBuzz'
        return self.next_handler.handle(data)


class BuzzHandler(Handler):
    def handle(self, data):
        if data % 5 == 0:
            return 'Buzz'
        return self.next_handler.handle(data)


class FizzHandler(Handler):
    def handle(self, data):
        if data % 3 == 0:
            return 'Fizz'
        return self.next_handler.handle(data)


class DefaultHandler(Handler):
    def handle(self, data):
        return data


class SolveHandler(Handler):
    def handle(self, data):
        return self.next_handler.handle(data)


def main():
    default = DefaultHandler()
    fizz = FizzHandler(default)
    buzz = BuzzHandler(fizz)
    fizz_buzz = FizzBuzzHandler(buzz)
    is_integer = IntegerHandler(fizz_buzz)
    solve = SolveHandler(is_integer)

    for i in range(100):
        print(solve.handle(i))


if __name__ == '__main__':
    main()
