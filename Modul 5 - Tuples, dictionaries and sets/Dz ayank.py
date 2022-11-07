#1 Створіть програму, що містить інформацію про відомих
# баскетболістів. Збережіть ПІБ та зріст кожного баскетболіс-
# та. Реалізуйте можливість додавати, видаляти, знаходити та
# змінювати дані. Використовуйте словник для збереження
# інформації.

# fis_list = {
#     "Koby Bright": "2.65",
#     "Jerry Uest": "2.15",
#     "Oscar Shmidt": "2.32",
#     "Sergey Belov": "2.5"
# }
# print(fis_list)
# select = 0
# while select != 6:
#     select = int(input(" Select number #1 Add people #2 Remove people #3 Find people #4 Replace #5 Print all\n: "))
#     if select == 1:
#         first = input("Name with last name : ")
#         second = input("Growth :")
#         fis_list[first] = second
#         print(fis_list)
#     elif select == 2:
#         first = input("Remove - take full name : ")
#         first.replace(" ", "")
#         fis_list.pop(first)
#         print(fis_list)
#     elif select == 3:
#         first = input("Find people : ")
#         first.replace(" ", "")
#         fis_list.get(first)
#         print("Found - ", first)
#     elif select == 4:
#         first = input("Find name for replace : ")
#         second = input("Info for replace : ")
#         fis_list[first] = second
#     elif select == 5:
#         print(fis_list)
#     elif select == 6:
#         print("Exit!")
#         break

#2 Створіть програму «Англо-французький словник». Збе-
# режіть слово англійською та його переклад на французьку.
# Реалізуйте можливість додавати, видаляти, знаходити та
# змінювати дані. Використовуйте словник для збереження
# інформації.

# fis_list = {
#     "Growth": "croissance",
#     "Rose": "rosée",
#     "Album": "l'album",
#     "Worker": "ouvrier",
#     "Assassin": "l'assassin"
# }
# print(fis_list)
# select = 0
# while select != 6:
#     select = int(input(" Select number #1 Add word #2 Remove word #3 Find word #4 Replace word #5 Print all\n: "))
#     if select == 1:
#         first = input("Take word : ")
#         second = input("Translate :")
#         fis_list[first] = second
#         print(fis_list)
#     elif select == 2:
#         first = input("Remove - word : ")
#         first.replace(" ", "")
#         fis_list.pop(first)
#         print(fis_list)
#     elif select == 3:
#         first = input("Find - word : ")
#         first.replace(" ", "")
#         fis_list.get(first)
#         print("found - ", first)
#     elif select == 4:
#         first = input("Find word for replace : ")
#         second = input("Info for replace : ")
#         fis_list[first] = second
#     elif select == 5:
#         print(fis_list)
#     elif select == 6:
#         print("Exit!")
#         break

#3 Створіть програму «Фірма», яка зберігає інформацію про
# працівників: ПІБ, телефон, корпоративний email, назва посади,
# номер кабінету, Skype. Реалізуйте можливість додавати, вида-
# ляти, знаходити та змінювати дані. Використовуйте словник
# для збереження інформації

# fis_list = dict()
# select = 0
# while select != 5:
#    select = int(input(" Select number #1 Add #2 Remove #3 Find #4 Replace \n: "))
#    if select == 1:
#         first = input("Name : ")
#         second = input("Number : ")
#         third = input("Email : ")
#         four = input("Position on work : ")
#         five = input("Skype : ")
#         fis_list[first] = {"Number": second, "Email": third, "Position on work": four, "Skype": five}
#         print(fis_list)
#    elif select == 2:
#         first = input("Name for remove : ")
#         sel = int(input("#1 Remove phone #2 Remove mail #3 Remove position #4 Remove Skype\n -"))
#         if sel == 1:
#             fis_list[first]["Number"] = ""
#         elif sel == 2:
#             fis_list[first]["Email"] = ""
#         elif sel == 3:
#             fis_list[first]["Position on work"] = ""
#         elif sel == 4:
#             fis_list[first]["Skype"] = ""
#         elif sel == 5:
#             fis_list.pop(first)
#         print(fis_list)
#    elif select == 3:
#        first = input("Name for find : ")
#        sel = int(input("#1 Find for phone #2 Find for mail #3 Find for position #4 Find for Skype\n -"))
#        if sel == 1:
#            print("Number : ", fis_list[first]["Number"])
#        elif sel == 2:
#            print("Email : ", fis_list[first]["Email"])
#        elif sel == 3:
#            print("Position on work : ", fis_list[first]["Position on work"])
#        elif sel == 4:
#            print("Skype : ", fis_list[first]["Skype"])
#    elif select == 4:
#        first = input("Name for replace : ")
#        sel = int(input("#1 Replace phone #2 Replace mail #3 Replace position #4 Replace Skype\n -"))
#        if sel == 1:
#            second = input("Number : ")
#            fis_list[first]["Number"] = second
#        elif sel == 2:
#            third = input("Email : ")
#            fis_list[first]["Email"] = third
#        elif sel == 3:
#            four = input("Position on work : ")
#            fis_list[first]["Position on work"] = four
#        elif sel == 4:
#            five = input("Skype : ")
#            fis_list[first]["Skype"] = five
#    elif select == 5:
#        print(fis_list)

#4 Створіть програму «Книжкова колекція», яка зберігає
# інформацію про книги: автор, назва книги, жанр, рік випуску,
# кількість сторінок, видавництво. Реалізуйте можливість дода-
# вати, видаляти, знаходити та змінювати дані. Використовуйте
# словник для збереження інформації.

fis_list = dict()
select = 0
while select != 5:
   select = int(input(" Select number #1 Add #2 Remove #3 Find #4 Replace \n: "))
   if select == 1:
        first = input("Name of book : ")
        second = input("Number of list : ")
        third = input("Auteur : ")
        four = input("Genre : ")
        five = input("Editor : ")
        fis_list[first] = {"Number of list": second, "Auteur": third, "Genre": four, "Editor": five}
        print(fis_list)
   elif select == 2:
        first = input("Name for remove : ")
        sel = int(input("#1 Remove book #2 Remove auteur #3 Remove genre #4 Remove editor\n -"))
        if sel == 1:
            fis_list[first]["Number of list"] = ""
        elif sel == 2:
            fis_list[first]["Auteur"] = ""
        elif sel == 3:
            fis_list[first]["Genre"] = ""
        elif sel == 4:
            fis_list[first]["Editor"] = ""
        elif sel == 5:
            fis_list.pop(first)
        print(fis_list)
   elif select == 3:
       first = input("Book for find : ")
       sel = int(input("#1 Find for lists #2 Find for Auteur #3 Find for genre #4 Find for editor\n -"))
       if sel == 1:
           print("Number of list : ", fis_list[first]["Number of list"])
       elif sel == 2:
           print("Auteur : ", fis_list[first]["Auteur"])
       elif sel == 3:
           print("Genre : ", fis_list[first]["Genre"])
       elif sel == 4:
           print("Editor : ", fis_list[first]["Editor"])
   elif select == 4:
       first = input("Book for replace : ")
       sel = int(input("#1 Replace lists #2 Replace auteur #3 Replace genre #4 Replace editor\n -"))
       if sel == 1:
           second = input("Number of list : ")
           fis_list[first]["Number of list"] = second
       elif sel == 2:
           third = input("Auteur : ")
           fis_list[first]["Auteur"] = third
       elif sel == 3:
           four = input("Genre : ")
           fis_list[first]["Genre"] = four
       elif sel == 4:
           five = input("Editor : ")
           fis_list[first]["Editor"] = five
   elif select == 5:
       print(fis_list)