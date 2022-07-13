"""
5.	Последовательность из n точек плоскости задана массивами Х[1..n] и Y[1..n] координат этих точек.
Разработать программу, которая ищет в этой последоватедльности точку, наиболее удаленную от начала координат.
"""
from math import sqrt

maxx = 0
coords = ()
for i in range(int(input("N: "))):
    x, y = map(float, input(f'{i + 1}-я пара: ').split())
    length = sqrt(x * x + y * y)
    if length > maxx:
        maxx = length
        coords = x, y

print(f'Наиболее отдаленная точка {coords}, на расстоянии {maxx}')
