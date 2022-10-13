# Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# ->[-5,-4, -3, -2, -1,0,1,2,3,4,5]
# ->15

def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0':
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num
import os
os.system("cls")
num_of_elements = user_input('Введите целое число больше 0 для создания списка: ')
# list = []
# for i in range(-num_of_elements, num_of_elements + 1):
#     list.append(i)
list = [i for i in range(-num_of_elements, num_of_elements + 1)]
print(f'Созданный список  - {list}')
print('Введите позиции элементов для перемножения.')
position_one = user_input('Позиция 1-го числа: ')
while not position_one < 2 * num_of_elements + 2: # Ввод цифр  меньше 1 
                                                  # и не цифры отследит функция user_input
    print('Такой позиции нет в списке, повторите!')
    position_one = user_input('Позиция 1-го числа: ')
position_two = user_input('Позиция 2-го числа: ')
while not position_two < 2 * num_of_elements + 2:
    print('Такой позиции нет в списке, повторите!')
    position_two = user_input('Позиция 2-го числа: ')
print(f'Произведение чисел равно: {list[position_one - 1] * list[position_two - 1]}')
