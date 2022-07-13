"""
3.	Среди 4-х одинаковых по виду монет одна фальшивая, причем не известно, легче она остальных или тяжелее.
Для взвешивания монет используются чашечные весы, с помощью которых можно определять,
что один предмет легче, тяжелее или равен по весу другому.
Разработайте алгоритм и напишите программу, которая находит фальшивую монету.
"""
import random

coin_1 = random.randint(1, 10)
coins = set(range(10))
coins.discard(coin_1)
coin_2 = random.choice(list(coins))

coins = [coin_1] * 3
coins.append(coin_2)
random.shuffle(coins)

if coins[0] == coins[1]:
    if coins[1] == coins[2]:
        print("Фальшивой монетой является 4.")
        print(coins)
    else:
        print("Фальшивой монетой является 3.")
        print(coins)
else:
    if coins[0] == coins[2]:
        print("Фальшивой монетой является 2.")
        print(coins)
    else:
        print("Фальшивой монетой является 1.")
        print(coins)