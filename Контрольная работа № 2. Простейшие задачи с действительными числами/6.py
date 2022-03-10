"""
6. Составить программу, которая вычисляет внутренние углы треугольника, заданного длинами сторон.
"""
import math
a, b, c = map(int, input('Введите три стороны треугольника через пробел: ').split())

if a<b+c or b<a+c or c<a+b:
    A = round(math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c))))
    B = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c))))
    C = round(180 - (A+B))

    print('A =',A, '\nB =',B, '\nC =',C )
else:
    print('Error')



