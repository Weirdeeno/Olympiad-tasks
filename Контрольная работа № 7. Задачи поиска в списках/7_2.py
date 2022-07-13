"""
2.	Дан массив A[1..n], элементами которого являются действительные числа.
Разработать программу, которая находит в этом массиве наибольшую по количеству элементов
возрастающую подпоследовательность подряд идущих элементов.
"""
import random

n = int(input("Введите n: "))
data = list(range(30))
random.shuffle(data)
print("Массив: ", data[:n])


arr = [[data[0]]]
for i in range(1, len(data)):
    if data[i - 1] > data[i]:
        arr.append([])
    arr[-1].append(data[i])

print("Возрастающая последовательность массива: ", max(arr, key = len))