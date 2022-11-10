# Пользователь вводит с клавиатуры три числа. В за-
# висимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел

# number = int(input("Take first - "))
# number2 = int(input("Take second - "))
# number3 = int(input("Take third - "))
#
# print("Result sum", number + number2 + number3)
# print("Result mult", number * number2 * number3)

# Пользователь вводит с клавиатуры три числа. В за-
# висимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или сред-
# неарифметическое трёх чисел

# number = int(input("Take first - "))
# number2 = int(input("Take second - "))
# number3 = int(input("Take third - "))
# select = int(input("Take number #1 max 2# min 3# average sum - "))
#
# if select == 1:
#     result = max(number,number2,number3)
#     print("Max number -",result)
# elif select == 2:
#     result = min(number,number2,number3)
#     print("Min number -", result)
# else:
#     print("Average -", (number+number2+number3)/3)

# Пользователь вводит с клавиатуры количество ме-
# тров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

# number = int(input(" Take number  - "))
# number2 = int(input(" Select type #1 Cm #2 Dm #3 Mn #4 Mi  - "))
#
# if number2 == 1:
#    print("Cm = ",number * 100)
# elif number2 == 2:
#    print("Dm = ",number * 10)
# elif number2 == 3:
#    print("Мm = ",number * 1000)
# elif number2 == 4:
#    print("Mi = ",number / 1609)
# else:
#     print("Error")

# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня неде-
# ли. Например, если 1, то на экране надпись понедельник,2 — вторник и т.д.

# number = int(input(" Take date - "))
#
# if number == 1:
#    print("January")
# elif number == 2:
#    print("February")
# elif number == 3:
#    print("March")
# elif number == 4:
#    print("April")
# elif number == 5:
#    print("May")
# elif number == 6:
#    print("June")
# elif number == 7:
#    print("July")
# elif number == 8:
#    print("August")
# elif number == 9:
#    print("September")
# elif number == 10:
#    print("October")
# elif number == 11:
#    print("November")
# elif number == 12:
#    print("December")
# else:
#     print("Error")

# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»

# number = int(input(" Take number - "))
#
# if number > 0:
#    print("Number -", number, "is positive")
# elif number == 0:
#    print("Number -", number, "is equal to zero")
# else:
#    print("Number -", number, "is negative")

# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке возрастания.

number = int(input(" Take number #1  - "))
number2 = int(input(" Take number #2  - "))

if number > number2:
   print("First number bigger - ", number2, number)
elif number == number2:
   print("First equal Second!")
else:
    print("Second number bigger - ", number, number2)
