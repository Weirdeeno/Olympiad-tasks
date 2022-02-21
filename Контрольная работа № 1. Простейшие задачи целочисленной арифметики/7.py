'''7.Многоэтажный дом имеет N этажей и M подъездов.
На каждой лестничной площадке  расположено K квартир.
Составить алгоритм и разработать программу, которая по номеру F квартиры
определяет подъезд и этаж расположения этой квартиры.  '''

N = int(input('Введите кол-во этажей: '))
M = int(input('Введите кол-во подъездов: '))
K = int(input('Введите кол-во квартир на лестничной площадке: '))

aih = K * N
aib = aih * M
print('\nКол-во квартир в подъезде =', aih)
print('Кол-во квартир в доме =',aib)

F = int(input('\nВведите номер квартиры: '))

F = F - 1 # чтоб расчет квартир шёл с 1
X = F//aih
Y = (X + 1)# узнаём в каком подъезде квартира
Z = F % aih
D = Z // K
S = (D + 1) # узнаём на каком этаже
print(str(Y), 'подъезд')
print(str(S), 'этаж')

