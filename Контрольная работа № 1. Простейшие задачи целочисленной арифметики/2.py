'''2.	Составить алгоритм и разработать программу,
которая находит две средние цифры произведения двузначного числа ab на число ba.
Число ab вводится с клавиатуры..'''

n1 = int(input("Введите двузначное число: "))
n2 = n1 // 10 +10 *(n1 % 10)
print('Двузначное число наоборот:',n2)
s = n1 * n2
print('Произведение двузначных чисел =',s)
if s>1000:
    a=(s//100)%10
    b=(s//10)%10
    print('Две средние цифры:',a,b)
else:
    print("Невозможно найти две средние цифры")


