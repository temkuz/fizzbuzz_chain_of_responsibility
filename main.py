from typing import Self
from abc import ABC, abstractmethod


class Handler(ABC):
    """Base class for handlers"""

    def __init__(self, handler: 'Handler' = None):
        self.next_handler = handler

    def set_next_handler(self, handler: 'Handler'):
        self.next_handler = handler

    @abstractmethod
    def handle(self, data): ...


class IntegerHandler(Handler):
    """Handler to check if the input is integer"""

    def handle(self, data):
        if not isinstance(data, int):
            raise TypeError('Input must be int')
        return self.next_handler.handle(data)


class FizzBuzzHandler(Handler):
    """Handler to check if the input is divisible by 15"""

    def handle(self, data):
        if data % 15 == 0:
            return 'FizzBuzz'
        return self.next_handler.handle(data)


class BuzzHandler(Handler):
    """Handler to check if the input is divisible by 5"""

    def handle(self, data):
        if data % 5 == 0:
            return 'Buzz'
        return self.next_handler.handle(data)


class FizzHandler(Handler):
    """Handler to check if the input is divisible by 3"""

    def handle(self, data):
        if data % 3 == 0:
            return 'Fizz'
        return self.next_handler.handle(data)


class DefaultHandler(Handler):
    """andler that will fire if all other handlers are passed"""

    def handle(self, data):
        return data


class SolveHandler(Handler):
    """Handler that is the entry point"""

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
