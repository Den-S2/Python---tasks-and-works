# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# fis_list =  tuple([randint(number1, number2) for i in range(number3)])
# sec_list = tuple([randint(number1, number2) for j in range(number3)])
# third_list = tuple([randint(number1, number2) for k in range(number3)])
# print(fis_list, sec_list, third_list)
# empty_list = set()
# for i in fis_list:
#     if i in sec_list and i in third_list:
#         empty_list.add(i)
# empty_list = tuple(empty_list)
#
# print("List:", empty_list)

# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# fis_list =  tuple([randint(number1, number2) for i in range(number3)])
# sec_list = tuple([randint(number1, number2) for j in range(number3)])
# third_list = tuple([randint(number1, number2) for k in range(number3)])
# print(fis_list, sec_list, third_list)
# empty_list = []
#
# for i in fis_list+sec_list+third_list:
#     if i not in empty_list:
#         empty_list.append(i)
#
# empty_list = tuple(empty_list)
#
# print("List:", empty_list)

# Есть три кортежа целых чисел необходимо найти эле-
# менты, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# fis_list =  tuple([randint(number1, number2) for i in range(number3)])
# sec_list = tuple([randint(number1, number2) for j in range(number3)])
# third_list = tuple([randint(number1, number2) for k in range(number3)])
#
# fis_list = [5,6,7,4]
# sec_list = [5,6,7,4]
# third_list = [5,6,7,4]
# print(fis_list, sec_list, third_list)
# empty_list = set()
# for i in fis_list:
#     if i in sec_list and i in third_list and fis_list.index(i) == sec_list.index(i) and fis_list.index(i) == third_list.index(i):
#         empty_list.add(i)
# empty_list = tuple(empty_list)
#
# print("List:", empty_list)