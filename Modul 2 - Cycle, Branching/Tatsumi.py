# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если число кратно 7, его надо выводить на экран.

# firnum = int(input("Take first number - "))
# secnum = int(input("Take second number - "))
#
# for i in range(firnum, secnum + 1):
#     if i % 7 == 0:
#         print("Elven number seven - ", i)

# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

# firnum = int(input("Take first number - "))
# secnum = int(input("Take second number - "))
# selnum = int(input("Select type for find\n #1 Find numbers\n #2 Find numbers falling order\n #3 Find elven number seven\n #4 Find elven number five\n #5 Exit - "))
# i = 1
# while selnum != 5:
#  if selnum == 1:
#    for i in range(firnum, secnum + 1):
#      print("Find number - ", i)
#    break
#  if selnum == 2:
#    for i in range(secnum, firnum -1, -1):
#         print("Find number in falling order - ", i)
#    break
#  if selnum == 3:
#    for i in range(firnum, secnum, + 1):
#       if i % 7 == 0:
#              print("Elven number seven - ", i)
#    break
#  if selnum == 4:
#    for i in range(firnum, secnum + 1):
#          if i % 5 == 0:
#              print("Elven number five - ", i)
#    break
#  if selnum == 5:
#      print("Exit")

# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число

# firnum = int(input("Take first number - "))
# secnum = int(input("Take second number - "))
#
# for i in range(firnum, secnum + 1):
#      if i % 3 == 0 and i % 5 == 0:
#       print(" Fizz Buzz")
#      elif i % 3 == 0:
#        print(" Fizz ")
#      elif i % 5 == 0:
#        print(" Buzz ")
#      else:
#          print("Number - ", i)

# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеариф-
# метическое каждой группы

# firnum = int(input("Take first number - "))
# secnum = int(input("Take second number - "))
# i=0
# sum = sum2= sum3 = sum4 = sum5 = sum6 = 0
#
# for i in range(firnum, secnum + 1):
#     if i % 2 == 0:
#       sum += i
#       sum2 = sum / i
#     elif i % 9 == 0:
#       sum3 += i
#       sum4 = sum3 / i
#     else:
#       sum5 += i
#       sum6 = sum5 / i
#
# print("Suma Even and avar = ", sum, sum2)
# print("Suma Even nine and avar = ", sum3, sum4)
# print("Suma Odd and avar = ", sum5, sum6)

# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %

# number = int(input("Take size number - "))
# sym = str(input("Take symbol - "))
# count = 0
# while count < number:
#     count = count + 1
#     if count == number:
#      for i in range(number):
#       print(sym)

# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive», если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

# while True:
#  number = int(input(" Take number - "))
#
#  if number > 0:
#    print("Number :", number, "is positive")
#  elif number == 0:
#    print("Number :", number, "is equal to zero")
#  elif number == -7:
#    print("Number :", number, "is exit, Good bye!!")
#    break
#  else:
#    print("Number :", number, "is negative")

# Пользователь вводит с клавиатуры числа. Програм-
# ма должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»

# while True:
#
#  select = int(input("Take number #1 max 2# min 3# average sum - "))
#  number = int(input("Take first - "))
#  number2 = int(input("Take second - "))
#  number3 = int(input("Take third - "))
#
#
#  if select == 1:
#     result = max(number,number2,number3)
#     print("Max number -",result)
#  elif select == 2:
#     result = min(number,number2,number3)
#     print("Min number -", result)
#  elif select == 3:
#     print("Average -", (number + number2 + number3) / 3)
#  else:
#     print("Number :", number, "is exit, Good bye!!")
#     break

