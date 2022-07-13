"""
7.	Разработать программу табулирования функции  двух переменных z = (1/Pi)*Sin((x2+y2)/Pi)
на прямоугольнике [a, b] * [c, d] с шагом h изменения переменных x и y.
"""
import math


h = int(input("Введите шаг: "))
a, b = map(int, input("Введите интервал [a, b]: ").split())
c, d = map(int, input("Введите интервал [c, d]: ").split())

x = a
y = c
while x < b + 1 and y < d + 1:
    print(x, "\t", (1 / math.pi) * math.sin(x ** 2 / math.pi), "\t", y, "\t", (1 / math.pi) * math.sin(y ** 2 / math.pi))
    x += h
    y += h
