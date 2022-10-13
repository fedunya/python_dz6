# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fill_list_random(list_len):
    return [round(random.uniform(1, 10), 2) for i in range(list_len)]
def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0':
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

import os, random
os.system("cls")
my_list = fill_list_random(user_input('Введите размер списка: '))
print(f'\nЗаданный список -> {my_list}\n')
# fractional_part = [round(my_list[i] % 1, 2) for i in range(len(my_list))]
fractional_part = list(map(lambda x: round(x % 1, 2), my_list))
print(f'Ответ -> {round(max(fractional_part) - min(fractional_part), 2)}\n')
