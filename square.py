# square of triangle

"""
>>> [triangle_exist_check(4, 6, 9), triangle_exist_check(3, 3, math.sqrt(18))]
[True, True]
>>> square(3, 3, math.sqrt(18))
4.5
"""
import math


class Point:
    """Класс, содержащий координаты x и y точки"""

    def __init__(self, x, y):
        """Конструктор класса
        :param x: координата по оси х
        :param y: координата по оси y.
        """

        self.x = x
        self.y = y


def input_coordinates():
    """Ввод данных пользователем: координаты x и y точки

    :return points: массив объектов класса Point.
    """

    points = []
    for i in range(1, 4):
        print("Введите координаты точки {}".format(i))
        ix = input("Координата x:")
        iy = input("Координата y:")
        if ix.isdigit() and iy.isdigit():
            points.append(Point(float(ix), float(iy)))
        else:
            raise ValueError('Неверный тип данных, требуется ввести целые или дробные числа')
    return points


def triangle_exist_check(abLength, bcLength, acLength):
    """Функция проверяет существование треугольника по правилу a+b>c, a+c>b, b+c>a, a > 0, b > 0, c > 0

    :param abLength: длина стороны ab
    :param bcLength: длина стороны bc
    :param acLength: длина стороны ac
    :return: bool (True, если выполныются все условия, и треугольник существует; False в  обратном случае).
    """

    acCondition = abLength + bcLength > acLength
    abCondition = bcLength + acLength > abLength
    bcCondition = abLength + acLength > bcLength

    zeroCheck = abLength > 0 and bcLength > 0 and acLength > 0

    return acCondition and abCondition and bcCondition and zeroCheck


def side_length(points):
    """Считает длины сторон треугольника

    :param points: массив экземпляров класса Point
    :return abLength, bcLength, acLength: длины сторон.
    """

    abLength = math.sqrt((points[1].x - points[0].x) ** 2 + (points[1].y - points[0].y) ** 2)
    bcLength = math.sqrt((points[2].x - points[1].x) ** 2 + (points[2].y - points[1].y) ** 2)
    acLength = math.sqrt((points[2].x - points[0].x) ** 2 + (points[2].y - points[0].y) ** 2)
    return abLength, bcLength, acLength


def square(abLength, bcLength, acLength):
    """Считает площадь по формуле Герона

    :param abLength: длина стороны ab
    :param bcLength: длина стороны bc
    :param acLength: длина стороны ac
    :return s0: площадь треугольника, float.
    """

    polu_per = (abLength + bcLength + acLength) * 0.5
    s = math.sqrt(polu_per * (polu_per - abLength) * (polu_per - bcLength) * (polu_per - acLength))
    s0 = float('%.4f' % s)
    return s0


def triangle_square_finding():
    """Функция, выполняющая всю работу по проверке и подсчету площади треугольника"""

    points = input_coordinates()
    abLength, bcLength, acLength = side_length(points)

    if triangle_exist_check(abLength, bcLength, acLength):
        s = square(abLength, bcLength, acLength)
        return s
    else:
        return "You did something wrong, please, be more careful"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(triangle_square_finding())


