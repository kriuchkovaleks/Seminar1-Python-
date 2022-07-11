'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет'''

print("Input number from 1 to 7")
number = int(input())
if number < 1 or number > 7:
    print("Input number from 1 to 7")
else:
    if number == 6 or number == 7:
        print("HOLIDAY")
    else:
        print("Weekday:-((((")
