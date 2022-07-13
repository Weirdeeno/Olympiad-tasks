"""
3.	Дан числовой массив A[1..n], состоящий из нечетного (n = 2k+1) числа попарно неравных элементов.
Разработать программу, которая ищет средний по величине элемент в этом массиве.
"""
from random import randint
import statistics

n = int(input("Введите n : "))
mas = [int(randint(1, 99)) for i in range(n)]
nch = [int(i) for i in mas if i % 2 != 0]
res_mean = statistics.mean(nch)

print("Массив: ", mas)
print("Массив с нечетными элементами: ", nch)
print("Средний по величине элемент = ", res_mean)