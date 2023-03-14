"""
Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года,
которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
"""
while True:
    year = int(input('Enter year: '))
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            print('Year: ', year, 'is leap')
    else:
            print('Year: ', year, 'is not leap')