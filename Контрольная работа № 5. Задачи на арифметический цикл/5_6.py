"""
6.	Разработать программу поиска наибольшего и наименьшего значения функции y = (1/Pi)*Sin(x2/Pi) на интервале [a, b]
методом последовательного вычисления значений этой функции на заданном интервале с шагом h изменения переменной x.
"""

import math

h = int(input("Введите шаг: "))
a, b = map(int, input("Введите интервал [a, b]: ").split())
x = a
maxx = 0
minn = 0
for x in range(a, b+1, h):
    y = (1/math.pi)*math.sin(x**2/math.pi)
    maxx = max(maxx, y)
    minn = min(minn, y)

print("max -", maxx)
print("min -", minn)
