"""
6.	Функция f с натуральными  аргументами и  значениями определена так:
f(0) = 0,   f(1) = 1,   f (2n) = f(n),   f (2n+1) = f (n) + f (n+1).
Составить программу вычисления f(n) по заданному  n, которая требуюет порядка log2n арифметических  операций.
"""
import math

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return n // 2
    else:
        return f(n // 2) + f(n // 2+1)

n = float(input("Enter n: "))
print(f(math.log2(n)))