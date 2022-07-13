"""
4.	На числовой прямой заданы отрезки [a, b] и [c, d].
Напишите программу, которая вычисляет общую длину части числовой оси, занятой этими отрезками.
"""
a, b = map(int, input("Введите две координаты отрезка [a, b] через пробел: ").split())
c, d = map(int, input('Введите две координаты отрезка [c, d] через пробел: ').split())

if a < b and a < c and a < d:
    if b < c and b < d:
        if c < d:
            print("a + d =", a + d)
        else:
            print("a + c =", a + c)
    elif c > b > d:
        print("a + c =", a + c)
    elif c < b < d:
        print("a + d =", a + d)
    else:
        print("a + b =", a + b)

elif b < a and b < c and b < d:
    if a < c and a < d:
        if c < d:
            print("b + d =", b + d)
        else:
            print("b + c =", b + c)
    elif c > a > d:
        print("b + c =", b + c)
    elif c < a < d:
        print("b + d =", b + d)
    else:
        print("b + a =", b + a)

elif c < a and c < b and c < d:
    if a < b and a < d:
        if b < d:
            print("c + d =", c + d)
        else:
            print("c + b =", c + b)
    elif b > a > d:
        print("c + b =", c + b)
    elif b < a < d:
        print("c + d =", c + d)
    else:
        print("c + a =", c + a)

elif d < a and d < b and d < c:
    if a < b and a < c:
        if b < c:
            print("d + c =", d + c)
        else:
            print("d + b =", d + b)
    elif b > a > c:
        print("d + b =", d + b)
    elif b < a < c:
        print("d + c =", d + c)
    else:
        print("d + a =", d + a)