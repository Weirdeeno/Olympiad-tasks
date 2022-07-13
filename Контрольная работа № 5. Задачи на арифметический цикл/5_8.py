"""
8.	Разработать программу приближенного вычисления интеграла ∫ f(x)dx на отрезке [a, b] по формуле средних прямоугольников
 при фиксированном числе N разбиения отрезка интегрирования [a, b] на N равных частей
"""


def trianmethod(f, a, b, n):

    """Вычисляет приближенное значение интеграла с помощью формулы прямоугольников
    f - подынтегральная функция
    a, b - пределы интегрирования
    n - количество частичных отрезков"""

    h = float(b - a) / n
    result = f(a + 0.5 * h)
    for i in range(1, n):
        result += f(a + 0.5 * h + i * h)
        result *= h
        return result