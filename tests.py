from unittest import TestCase
from main import DefaultHandler, FizzHandler, BuzzHandler, FizzBuzzHandler, IntegerHandler, SolveHandler


class FizzBuzzTest(TestCase):
    def setUp(self) -> None:
        self.default = DefaultHandler()
        self.fizz = FizzHandler(self.default)
        self.buzz = BuzzHandler(self.fizz)
        self.fizz_buzz = FizzBuzzHandler(self.buzz)
        self.is_integer = IntegerHandler(self.fizz_buzz)
        self.solve = SolveHandler(self.is_integer)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.solve.handle('invalid data')

    def test_valid_data(self):
        self.assertEqual(self.solve.handle(15), 'FizzBuzz')
        self.assertEqual(self.solve.handle(5), 'Buzz')
        self.assertEqual(self.solve.handle(3), 'Fizz')
        self.assertEqual(self.solve.handle(37), 37)


if __name__ == '__main__':
    FizzBuzzTest()
