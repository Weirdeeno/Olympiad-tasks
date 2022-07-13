"""
5.	Реализовать алгоритм приближенного решения уравнения f(x) = 0 на отрезке [a, b] методом деления отрезка пополам.
Вычисление значения функции f в точке x реализовать в виде функции.
"""

from math import fabs


def f(x):
    return x * (x - 3.0234) * (x - 10)


def sgn(x):
    if (x > 0):
        return 1
    elif (x < 0):
        return -1
    else:
        return 0


def root(a, b, fa, fb, epsX, epsF):
    if sgn(fa) * sgn(fb) > 0:
        return None
    c = 0.5 * (a + b)
    fc = f(c)
    if (fabs(fc) < epsF) or (fabs(b - a) < epsX):
        return c
    elif sgn(fa) * sgn(fc) < 0:
        return root(a, c, fa, fc, epsX, epsF)
    else:
        return root(c, b, fc, fb, epsX, epsF)


a = int(input("a = "))
b = int(input("b = "))
r = root(a, b, f(a), f(b), 1e-8, 1e-14)
print(r)