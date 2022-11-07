# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве па-
# раметра. Полученный результат возвращается из функции.

# def first(a):
#     print(a)
#     mult = 1
#     for i in a:
#         mult *= i
#     return mult
# print(first([int(input("Take number : ")) for i in range(5)]))

# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

# def first(a):
#     print(a)
#     return min(a)
# print(first([int(input("Take number : ")) for i in range(5)]))

# Напишите функцию, определяющую количество про-
# стых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.
from random import randint
# def first(a):
#      print(a)
#      count2 = 0
#      for i in a:
#         count = 0
#         for j in range(1, i):
#            if i % j == 0 and j != i:
#              count += 1
#         if count == 1:
#            count2 += 1
#      return count2
# print(first([int(input("Take number : ")) for i in range(5)]))
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

# def first(a):
#     print(a)
#     # a = set(a)
#     c = (int(input("Take number for remove: ")))
#     a.remove(c)
#     print("Number delete - ")
#     return a
#
# print(first([int(input("Take number : ")) for i in range(5)]))

# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.

# def first(a, b):
#     print(a)
#     print(b)
#     c = []
#     for i in a + b:
#        c.append(i)
#     return c
# print(first([int(input("Take list1 : ")) for i in range(5)],[int(input("Take list2 : ")) for j in range(5)]))

# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержа-
# щий полученные результаты

# def first(a, b):
#     print(a)
#     c = []
#     for i in a:
#      mult = i ** b
#      c.append(mult)
#     return c
#         # c.append(mult)
#
# print(first([int(input("Take list1 : ")) for i in range(5)],int(input("Take number: "))))