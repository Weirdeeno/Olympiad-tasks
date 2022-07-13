"""
9.	Разработать программу, которая по номеру месяца и номеру дня 2001 года ищет день недели, который припадает на эту дату.
"""
import datetime

m = int(input("Введите номер месяца: "))
d = int(input("Введите день: "))
date = datetime.datetime(
    year = 2001,
    month = m,
    day = d)
print('День недели -', date.weekday()+1)