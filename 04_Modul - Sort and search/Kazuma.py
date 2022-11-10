# Написать программу, выполняющую сортировку
# списка целых чисел методом пузырьковой сортировки

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# list_numb = [randint(number1, number2) for i in range(number3)]
# print(list_numb)
# for i in range(len(list_numb)-1):
#     for j in range(len(list_numb)-i-1):
#         if list_numb[j] > list_numb[j+1]:
#             number = list_numb[j]
#             list_numb[j] = list_numb[j+1]
#             list_numb[j+1] = number
# print(list_numb)

# Написать программу, выполняющую сортировку
# списка целых чисел методом вставок.

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# list_numb = [randint(number1, number2) for i in range(number3)]
# print(list_numb)
# for i in range(1, len(list_numb)):
#     number = list_numb[i]
#     j = i - 1
#     while j >= 0 and list_numb[j] > number:
#         list_numb[j+1] = list_numb[j]
#         j = j - 1
#     list_numb[j+1] = number
# print(list_numb)

# Есть список целых. Необходимо первую половину
# списка отсортировать по убыванию, вторую половину
# по возрастанию.

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# list_numb = [randint(number1, number2) for i in range(number3)]
# print(list_numb)
# for i in range(len(list_numb)-1):
#     for j in range(len(list_numb)-i-1):
#         if list_numb[j] > list_numb[j+1]:
#             number = list_numb[j]
#             list_numb[j] = list_numb[j+1]
#             list_numb[j+1] = number
# print(list_numb)
# for i in range(1, len(list_numb)):
#     number = list_numb[i]
#     j = i - 1
#     while j >= 0 and list_numb[j] < number:
#         list_numb[j+1] = list_numb[j]
#         j = j - 1
#     list_numb[j+1] = number
# print(list_numb)

# Написать программу, выполняющую сортировку
# списка целых чисел методом слияния

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# list_numb = [randint(number1, number2) for i in range(number3)]
# print("Start : ", list_numb)
# size = len(list_numb)//2
# left_list = list_numb[:size]
# right_list = list_numb[size:]
# i, j, k = 0, 0, 0
# while i < len(left_list) and j < len(right_list):
#      if left_list[i] < right_list[j]:
#             list_numb[k] = left_list[i]
#             i += 1
#      else:
#         list_numb[k] = right_list[j]
#         j += 1
#         k+=1
# left_list = list_numb[:size]
# right_list = list_numb[size:]
# i, j, k = 0, 0, 0
# while i < len(left_list) and j < len(right_list):
#      if left_list[i] > right_list[j]:
#             list_numb[k] = left_list[i]
#             i += 1
#      else:
#         list_numb[k] = right_list[j]
#         j += 1
#         k+=1
# print("Result : ", list_numb)
