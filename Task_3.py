## Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

from email import message


def check_if_quarter_exist(message):
    while True: 
        print(message)
        quarter = int(input())
        if quarter in range(1,5):
            return quarter
        else:
            print("Input proper quarter from 1 to 4")

user_message = "Imput quarter"
quarter = check_if_quarter_exist(user_message)

if quarter == 1: print("Possible X-range is (0, +limitless) Y-range is (0, +limitless)")
if quarter == 2: print("Possible X-range is (0, -limitless) Y-range is (0, +limitless)")
if quarter == 3: print("Possible X-range is (0, -limitless) Y-range is (0, -limitless)")
if quarter == 4: print("Possible X-range is (0, +limitless) Y-range is (0, -limitless)")
