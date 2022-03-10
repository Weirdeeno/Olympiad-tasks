"""
10. В карточной игре “Подкидной дурак” необходимо определять, бьет ли одна карта другую, или нет.
Составьте программу, которая дает ответ на этот вопрос. Масти карт задаются буквами П, Б, Т, Ч.
Названия карт - 6, 7, 8, 9, 10, В, Д, К, Т.
Исходные данные программы: масти и названия двух карт и масть козыря.   
"""
import random

D = 'Бубна'
H = 'Червь'
S = 'Пика'
C = 'Треф'

suit = [D, H, S, C]

cards = ['6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']

Ac = random.choice(cards)
As = random.choice(suit)
Bc = random.choice(cards)
Bs = random.choice(suit)

TrumpSuit = random.choice(suit)

# Исходные данные
print('Масти: ', D + ',', H + ',', S + ',', C)
print('Первая карта -', Ac, As)
print('Вторая карта -', Bc, Bs)
print('Масть козыря -', TrumpSuit)

if cards.index(Ac) > cards.index(Bc) and suit.index(As) == suit.index(Bs) or cards.index(Ac) > cards.index(Bc) and suit.index(As) == suit.index(TrumpSuit) or cards.index(Ac) > cards.index(Bc) and suit.index(TrumpSuit) == suit.index(Bs):
    print('Первая карта бъет вторую')
elif cards.index(Ac) < cards.index(Bc) and suit.index(As) == suit.index(Bs) or cards.index(Ac) < cards.index(Bc) and suit.index(As) == suit.index(TrumpSuit) or cards.index(Ac) < cards.index(Bc) and suit.index(TrumpSuit) == suit.index(Bs):
    print('Вторая карта бъет первую')
else:
    print('Ничья')
