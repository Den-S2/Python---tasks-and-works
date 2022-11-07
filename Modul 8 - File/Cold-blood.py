# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редакти-
# рование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.


# import os.path
# path = os.path.join("Strike 2", "strt.txt")
# file2 = open(path, "r")
# file = open(os.path.join("Strike 2", "strt.txt"), "a")
# fis_list = file2.read()
# print(fis_list)
# select = 0
# while select != 6:
#    select = int(input(" Select number #1 Add #2 Remove #3 Find #4 Replace #5 Print all #6 Save #7 Save and exit! \n: "))
#    if select == 1:
#         file2 = open(path, "r")
#         file = open(os.path.join("Strike 2", "strt.txt"), "a")
#         first = input("Take name surname age and profession: ")
#         print(first)
#         file.write("\n" + first)
#         file.close(); file2.close()
#    elif select == 2:
#         file2 = open(path, "r")
#         file = open(os.path.join("Strike 2", "strt.txt"), "w")
#         first = input("Name for remove : ")
#         remove = fis_list.replace(first, "")
#         print(remove)
#         file.write(remove)
#         file.close(); file2.close()
#    elif select == 3:
#         file2 = open(path, "r")
#         sec = int(input("#1 Find all for symbol #2 Find info for name : "))
#         if sec == 1:
#           first = input("Name for find: ")
#           for i in file2:
#              if first in i:
#                 print(i)
#         if sec == 2:
#           first = input("Name for find: ")
#           sector = int(input("#1 For surname #2 For age #3 For prof: "))
#           for i in file2:
#              if first in i:
#                 print(i.split()[sector]); break
#    elif select == 4:
#         file = open(os.path.join("Strike 2", "strt.txt"), "w")
#         first = (input("Take word fo find: "))
#         sec = (input("Take word for replace: "))
#         replace = fis_list.replace(first, sec)
#         print(replace)
#         file.write(replace)
#         file.close(); file2.close()
#    elif select == 5:
#         file2 = open(path, "r")
#         print(file2.read())
#         file.close(); file2.close()
#    elif select == 6:
#        file.close();file2.close()
#        print("Saved and exit!")
#    elif select == 7:
#        file.close();file2.close()
#        print("Saved and exit!")
#        break