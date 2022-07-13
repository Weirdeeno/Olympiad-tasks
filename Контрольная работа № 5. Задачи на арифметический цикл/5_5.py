"""
5.	Разработать программу табулирования функции  y = (1/Pi)*Sin(x2/Pi) на интервале [a, b] с шагом h изменения переменной x.
"""

import math

h = int(input("Введите шаг: "))
a, b = map(int, input("Введите интервал [a, b]: ").split())
x = a
while x < b+1:
    print(x, "\t", (1/math.pi)*math.sin(x**2/math.pi))
    x += h




