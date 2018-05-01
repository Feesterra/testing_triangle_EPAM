import unittest
import square
import math


class TestSquare(unittest.TestCase):
    """Класс тестирует модуль square.py"""

    def test_positive_triangle_exist_check(self):
        """Тестирует работу функции triangle_exist_check модуля square.py"""

        self.assertTrue(square.triangle_exist_check(4, 6, 9))

    def test_negative_triangle_exist_check(self):
        """Тестирует работу функции triangle_exist_check модуля square.py"""

        self.assertFalse(square.triangle_exist_check(0, 0, 0))

    def test_square(self):
        """Тестирует работу функции square модуля square.py"""

        self.assertEqual(4.5, square.square(3, 3, math.sqrt(18)), "Wrong answer")

    def test_input_coordinates(self):
        """Тестирует выброс ошибки (в любом случае) в функции input_coordinates (ввод данных) модуля square.py"""

        with self.assertRaises(ValueError) as raised_exception:
            square.input_coordinates()
        self.assertEqual('Type wrong', raised_exception.exception.args[0])

    def test_side_length(self):
        """Тестирует функцию side_length модуля square.py"""

        points = []
        a = square.Point(5, 6)
        b = square.Point(5, 5)
        c = square.Point(4, 5)
        points.extend([a, b, c])
        self.assertEqual((1, 1, math.sqrt(2)), square.side_length(points))


if __name__ == '__main__':
    unittest.main()
