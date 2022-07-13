"""
2.	Даны натуральные числа а, b. Вычислить произведение а*b, используя в программе лишь операции +, -, =, >.
"""

x, y = [int(i) for i in (input('Введите два числа через пробел: ').split())]

result = 0
z = 0

while z != (abs(y)):
    result = result + (abs(x))
    z = z + 1

if (y or x) < 0:
    result = -result

print(result)