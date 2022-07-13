"""
7.	Разработать программу, которая для данного натурального числа N ищет представление
этого числа в виде суммы двух квадратов натуральных чисел: N = x2 + y2 .
"""
from math import sqrt


def main():
    number = int(input('Введите число: '))
    for k in range(1, 5):
        decompose = to_sum_of_squares(number, k)
        if decompose:
            print(decompose)
            break


def to_sum_of_squares(n: int, k: 'squares count:int') -> list:
    if (n < 0) or (k <= 0):
        return []
    maximum = round(sqrt(n))
    if n == maximum * maximum:
        return [n]
    for c in range(1, maximum + 1):
        decomposition = to_sum_of_squares((n - c * c), k - 1)
        if decomposition:
            return [c * c] + decomposition


if __name__ == '__main__':
    main()