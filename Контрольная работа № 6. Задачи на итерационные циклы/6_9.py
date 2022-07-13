"""
9.	Через GCD(A, B) обозначим наибольший общий делитель натуральных чисел A и B.
Известно, что если D = GCD(A, B), то существуют такие целые числа X и Y, что D = X*A + Y*B.
Разработать программу, которая по числам A и B вычисляет X и Y.
"""


def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

a, b = map(int, input("Введите числа А и В: ").split())
n = gcd_extended(a, b)
print(f'Делитель равен {n[0]}, X = {n[1]}, Y = {n[2]}')