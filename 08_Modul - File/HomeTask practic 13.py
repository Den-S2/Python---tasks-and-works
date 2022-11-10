#Напишите информационную систему «Сотрудники».
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

import os.path
import json
file2 = open(os.path.join("../Strike 2", "tenda.json"), "r")
file = open(os.path.join("../Strike 2", "tenda.json"), "a")
fis_list = json.load(file2); print(fis_list)
# fis_list = dict()
select = 0
while select != 6:
   select = int(input(" Select number #1 Add #2 Remove #3 Find #4 Replace #5 Print all #6 Save \n: "))
   if select == 1:
        file2 = open(os.path.join("../Strike 2", "tenda.json"), "r")
        file = open(os.path.join("../Strike 2", "tenda.json"), "w")
        first = input("Name: ")
        sec = input("Surname: ")
        thi = input("Age: ")
        fou = input("Profession: ")
        fis_list[first] = {"Surname": sec, "Age": thi, "Profession": fou}
        json.dump(fis_list,file); file.close()
   elif select == 2:
        file2 = open(os.path.join("../Strike 2", "tenda.json"), "r")
        file = open(os.path.join("../Strike 2", "tenda.json"), "w")
        first = input("Name for remove : ")
        sel = int(input("#1 remove surname #2 remove age #3 remove prof #4 remove person\n - "))
        if sel == 1:
             fis_list[first]["Surname"] = ""
        elif sel == 2:
             fis_list[first]["Age"] = ""
        elif sel == 3:
             fis_list[first]["Profession"] = ""
        elif sel == 4:
             fis_list.pop(first)
        json.dump(fis_list, file); file.close()
   elif select == 3:
        file2 = open(os.path.join("../Strike 2", "tenda.json"), "r")
        first = input("Name for find : ")
        sel = int(input("#1 Find surname #2 Find age #3 Find prof\n - "))
        if sel == 1:
             print("Surname :", fis_list[first]["Surname"])
        elif sel == 2:
             print("Age :", fis_list[first]["Age"])
        elif sel == 3:
             print("Profession :", fis_list[first]["Profession"])
        file2.close()
   elif select == 4:
        file2 = open(os.path.join("../Strike 2", "tenda.json"), "r")
        file = open(os.path.join("../Strike 2", "tenda.json"), "w")
        first = input("Name for find : ")
        sel = int(input("#1 Replace surname #2 Replace age #3 Replace prof\n - "))
        if sel == 1:
             second = input("Surname :")
             fis_list[first]["Surname"] = second
        elif sel == 2:
             third = input("Age : ")
             fis_list[first]["Age"] = third
        elif sel == 3:
             four = input("Profession : ")
             fis_list[first]["Profession"] = four
        elif sel == 4:
             five = input("Name : ")
             fis_list[first]["Name"] = five
        json.dump(fis_list, file); file.close()
   elif select == 5:
        file2 = open(os.path.join("../Strike 2", "tenda.json"), "r")
        print(fis_list)
        file2.close()
   elif select == 6:
       file.close();file2.close()
       print("Saved and exit!")
       break