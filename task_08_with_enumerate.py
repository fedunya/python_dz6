# Задайте список из n чисел последовательности (1+1/n)**n 
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system("cls")
# list = []
num = input('Введите целое число больше нуля: ')
while not num.isdigit() or num == '0':
    print('Неверный ввод, повторите!')
    num = input('Введите целое число больше нуля: ')
num = int(num)
# for i in range(1, num+1):
#     list.append(round((1 + 1/i)**i, 2))
list = [round((1 + 1/x)**x, 2) for x in range(1, num+1)]
sum = 0
for i in range(len(list)):
    sum += list[i]
my_dict = dict(enumerate(list, 1))
print(my_dict)
print(f'Сумма чисел последовательности: {sum}')

