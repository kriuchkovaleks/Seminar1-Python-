'''
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''


def check_if_zero(message):
    while True:
        print(message)
        coordinate = float(input())
        if coordinate != 0:
            return coordinate
        else:
            print("Input number not equal 0")


def calc_coordinates(x_corr, y_corr):
    if x_corr > 0 and y_corr > 0:
        print("1st quarter")
    if x_corr > 0 and y_corr < 0:
        print("4th quarter")
    if x_corr < 0 and y_corr > 0:
        print("2nd quarter")
    if x_corr < 0 and y_corr < 0:
        print("3rd quarter")


user_message = "Input coordinate X"
x = check_if_zero(user_message)

user_message = "Input coordinate Y"
y = check_if_zero(user_message)

calc_coordinates(x, y)
