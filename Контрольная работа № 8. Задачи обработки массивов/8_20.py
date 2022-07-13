"""
20.	Дан двумерный числовой массив А[1..n, 1..m].
Разработать программу поиска столбца, сумма квадратов элементов которого минимальна.
"""

a = [
    [1, 3, 5],
    [4, 2, 1],
    [5, 3, 1],
]

min_index = 0
min_sum = sum([x[0]**2 for x in a])

for i in range(len(a[0])):
    col = [x[i] for x in a]
    suma = sum([x**2 for x in col])
    print(col, suma)

    if suma < min_sum:
        min_sum = suma
        min_index = i

print(min_index, min_sum)