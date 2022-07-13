"""
8.	Даны упорядоченные по неубыванию числовые массивы А[1..n] и В[1..m].
Разработать программу, которая ищет и выводит на экран индексы всех элементов массива A, входящих также и в массив В.
"""
arrA = []
arrB = []
n = int(input("n = "))
m = int(input("m = "))

for i in range(1, n+1):
    arrA.append(+i)
print("Массив А:", *arrA)

for i in range(1, m+1):
    arrB.append(+i)
print("Массив B:", *arrB)
print("Индексы входящих элементов в два массива: ")
for i in arrA:
    if i in arrB:
        if arrA > arrB:
            print(arrB.index(i), end=' ')
        else:
            print(arrA.index(i), end=' ')




