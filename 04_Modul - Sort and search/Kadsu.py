# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# list_numb = [randint(number1, number2) for i in range(number3)]
# print("Start result : ", list_numb)
#
# size = len(list_numb) // 3
# left_list = list_numb[:size]
# cen_list = list_numb[size: size + size]
# right_list = list_numb[size + size:]
# if sum(left_list + cen_list) / len(left_list+cen_list) > 0:
#     for i in range(len(left_list) - 1):
#       for j in range(len(left_list)-i-1):
#         if left_list[j] > left_list[j+1]:
#             number = left_list[j]
#             left_list[j] = left_list[j+1]
#             left_list[j+1] = number
#     for i in range(len(cen_list) - 1):
#       for j in range(len(cen_list)-i-1):
#         if cen_list[j] < cen_list[j+1]:
#             number = cen_list[j]
#             cen_list[j] = cen_list[j+1]
#             cen_list[j+1] = number
#     for i in range(len(right_list) - 1):
#       for j in range(len(right_list)-i-1):
#         if right_list[j] > right_list[j+1]:
#             number = right_list[j]
#             right_list[j] = right_list[j+1]
#             right_list[j+1] = number
# else:
#     for i in range(len(left_list) - 1):
#         for j in range(len(left_list) - i - 1):
#             if left_list[j] > left_list[j + 1]:
#                 number = left_list[j]
#                 left_list[j] = left_list[j + 1]
#                 left_list[j + 1] = number
#     for i in range(len(cen_list) - 1):
#         for j in range(len(cen_list) - i - 1):
#             if cen_list[j] > cen_list[j + 1]:
#                 number = cen_list[j]
#                 cen_list[j] = cen_list[j + 1]
#                 cen_list[j + 1] = number
#     for i in range(len(right_list) - 1):
#         for j in range(len(right_list) - i - 1):
#             if right_list[j] < right_list[j + 1]:
#                 number = right_list[j]
#                 right_list[j] = right_list[j + 1]
#                 right_list[j + 1] = number
# print("Finish result : ", left_list + right_list + cen_list)

# Написать программу «успеваемость». Пользователь
# вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя

# mark = [int(input("Take marks : ")) for i in range(10)]
# select, suma = 0, 0
# while select != 5:
#     select = int(input(" #1 Print all marks\n #2 Retake mark\n #3 Student pay?\n #4 Print list on higher\n :"))
#     if select == 1:
#       print("Your marks :", mark)
#     elif select == 2:
#         first = int(input("Find mark : "))
#         second = int(input("Mark for retake : "))
#         mark[first - 1] = second
#         print("Retake list! : ", mark)
#     elif select == 3:
#             if sum(mark)/len(mark) >= 10.7:
#                 print("Student you have your student pay!")
#             else:
#                 print("Forgive for your student pay!")
#     elif select == 4:
#         for i in range(len(mark) - 1):
#             for j in range(len(mark) - i - 1):
#                 if mark[j] > mark[j + 1]:
#                     number = mark[j]
#                     mark[j] = mark[j + 1]
#                     mark[j + 1] = number
#         print("Sorted marks : ", mark)
#     elif select == 5:
#         print("Exit!")
#         break
# Написать программу, реализующую сортировку списка
# методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы ана-
# лизировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку
# нет смысла — список отсортирован.

# from random import randint
# number1 = int(input("Take first diap - "))
# number2 = int(input("Take second diap - "))
# number3 = int(input("Take cost numbers - "))
# list_numb = [randint(number1, number2) for i in range(number3)]
#
# for i in range(len(list_numb)-1):
#     sorted_check = 1
#     for j in range(len(list_numb)-i-1):
#         if list_numb[j] > list_numb[j+1]:
#             number = list_numb[j]
#             list_numb[j] = list_numb[j+1]
#             list_numb[j+1] = number
#             sorted_check = 0
#     if sorted_check == 1:
#         break
# print(list_numb)