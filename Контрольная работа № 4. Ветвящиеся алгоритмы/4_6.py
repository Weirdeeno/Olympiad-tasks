"""
6.	Напишите программу, которая вычисляет наибольшее и наименьшее значения функции
	       Y=ax2 +bx+c на отрезке [p ; q].
"""
import math

def f(x):
    return a * x ** 2 + b * x + c

a, b, c = map(int, input("Введите коэффициенты a, b, c: ").split())
p, q = map(int, input("Введите значения отрезка [p ; q]: ").split())

f_min = math.inf
f_max = -math.inf

for x in range(int(p), int(q) + 1):
    f_min = min(f_min, f(x))
    f_max = max(f_max, f(x))

print("Наименьшее -", f_min,
      "\nНаибольшее -", f_max)
