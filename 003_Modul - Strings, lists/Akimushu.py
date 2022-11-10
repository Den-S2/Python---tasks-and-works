# Користувач вводить з клавіатури арифметичний вираз.
# Наприклад, 23+12.
# Виведіть результат виразу на екран. У нашому прикладі 35.
# Арифметичний вираз може складатися тільки з трьох частин:
# число, операція, число. Можливі операції: +, -, *, /

# string = input("Take Ar sen - ")
# li = ['+', '-', '*', '/']
# if '+' in string:
#     number1, number2 = string.split('+')
#     print("Result : ", number1, "+", number2, "=", int(number1) + int(number2))
# elif '-' in string:
#     number1, number2 = string.split('-')
#     print("Result : ", number1, "-", number2, "=", int(number1) - int(number2))
# elif '*' in string:
#      number1, number2 = string.split('*')
#      print("Result : ", number1, "*", number2, "=", int(number1) * int(number2))
# elif '/' in string:
#      number1, number2 = string.split('/')
#      print("Result : ", number1, "/", number2, "=", int(number1) / int(number2))

# У списку цілих, заповненому випадковими числами, ви-
# значте мінімальний та максимальний елементи, підрахуйте
# кількість від’ємних елементів, додатних елементів та кількість
# нулів. Результати виведіть на екран.

# from random import randint
# number = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# list = [randint(number,number2) for i in range(number3)]
# # list7 = list[list.index(1,list):list.index(number3,list)+1]
# sum1, sum2, sum3 = 0,0,0
# print("Numbers : ", list)
# print("Count pos num : ", sum(i > 0 for i in list))
# print("Count neg num : ", sum(i < 0 for i in list))
# print("Count zero : ", sum(i == 0 for i in list))
# print("Min number : ", min(list))
# print("Max number : ", max(list))
# # print("Mult range min - max : ", sum(list7))

#second type
from random import randint
number = int(input("Take first diap - "))
number2 = int(input("Take second diap - "))
number3 = int(input("Take cost numbers - "))
list = [randint(number, number2) for i in range(number3)]
list2 = [randint(number, number2) for j in range(number3)]
emptylist, mx, dup = [], [], []
sum1, sum2, sum3 = [], [], []
for i in list+list2:
       if i not in emptylist:
           emptylist.append(i)
       else:
           dup.append(i)

mx.append(min(list))
mx.append(min(list2))
mx.append(max(list))
mx.append(max(list2))

# dup = [x for i, x in enumerate(list) if i != list.index(x)]
print("List #1 : ", list)
print("List #2 : ", list2)
print("List #3 : ", list+list2)
print("Elements of both list : ", dup)
print("Elements without repe : ", emptylist)
print("El common to two list : ", emptylist)
print("Min, max number : ", mx)
# print("Mult range min - max : ", sum(list7))