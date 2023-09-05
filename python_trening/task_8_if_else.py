# Программа проверяет является ли число положительным
# или отрицательным и выводит соответствущее сообщение.

num = 3

# Также попробуйте следующие значения num.
# num = -5
# num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

str_1 = 'test'
str_2 = 'test1'
if str_1 in str_2:
    print('Да')
else:
    print('Нет')


num_float = 3.4
# Также попробуйте варианты
# num_float = 0
# nun_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True
num = -1
if num > 0 and permit_print:
    print('nam - Положительное число')
elif not permit_print:
    print('Печать запрещена')


x = 1

if  x>= 1 and x <= 4:
    print('Баколавр')
elif x < 7:
    print('Магистр')
elif x < 10:
    print('Аспирант')
else:
    print('Введите корректный год обучения')


x = 150
if x > 100 or x < -100:
    print('-')
else:
    print('+')