"""
4.	Дан массив A[1..n], состоящий из действительных чисел.
Разработать программу, которая ищет  в этом массиве наименьшее положительное число.
"""
print("Наименьшее положительное число массива =",
      min(int(i) for i in input("Введите элементы массива через пробел : ").split() if int(i) > 0))