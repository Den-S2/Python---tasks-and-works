# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.

# number = int(input("Take first number  - "))
# number2 = int(input("Take second number - "))
# b = 1
# print(number,"^", number2, " = ", number**number2)
#
# for i in range(number2):
#     b *= number
# print("Answer - ", b)

# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.

# number = int(input("Take first number  - "))
# number2 = int(input("Take second number - "))
# count = 0
# for i in range(number, number2):
#     i1 = i // 100
#     i2 = (i // 10) % 10
#     i3 = i % 10
#     if i1 == i2 or i2 == i3 or i3 == i1:
#         count += 1
# print("Able - ", count)
#
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

# number = int(input("Take first number  - "))
# number2 = int(input("Take second number - "))
# count = 0
# for i in range(number, number2):
#     i1 = i // 1000
#     i2 = (i // 100) % 100
#     i3 = i % 100
#     if i1 != i3 or i2 != i3 or i3 != i1:
#         count += 1
# print("Able - ", count)
#
# Пользователь вводит любое целое число. Необхо-
# димо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.
#
# number = input("Take number - ")
# new_number = ""
# for i in number:
#     if i != "6" and i!= "3":
#         new_number = new_number + i
# print(" Delete number 3 and 6 - ",new_number)