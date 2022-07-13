"""
4.	Реализовать алгоритм приближенного решения уравнения f(x) = 0 на отрезке [a, b] методом хорд.
Вычисление значения функции f в точке x реализовать в виде функции.
"""
import math


def F(x):
    return 0.1 * math.pow(x, 2) - x * math.log(x)


def F1(x):
    res = 0.2 * x - math.log(x) - 1
    print(res)
    return res


def Method(a, b):
    try:
        x0 = (a + b) / 2
        xn = F(x0)
        xn1 = xn - F(xn) / F1(xn)
        while abs(xn1 - xn) > math.pow(10, -5):
            xn = xn1
            xn1 = xn - F(xn) / F1(xn)
        print(xn1)
        return xn1
    except ValueError:
        print("Value not invalidate")


if __name__ == '__main__':
    x=float(input("x = "))
    a=float(input("a = "))
    b=float(input("b = "))
    F(x)
    F1(x)
    Method(a, b)