#Маємо два текстові файли. З’ясуйте, чи співпадають їхні
# рядки. Якщо ні, то виведіть із кожного файлу рядок, який не
# співпадає.

# import os.path
# import string
#
# path = os.path.join("Strike 2", "strike.txt")
# file = open(path, "r")
# path = os.path.join("Strike 2", "strike2.txt")
# file2 = open(path, "r")
# line = file.read().split()
# line2 = file2.read().split()
# abod = []
# c = str
# print(file.read())
# for i in line:
#   if i not in line2:
#         abod.append(i)
#         c = " ".join(abod)
# print(c)
# file.close(); file2.close();

# Маємо текстовий файл. Створіть новий файл і запишіть
# до нього наступну статистику за вихідним файлом:
# ■ кількість символів;
# ■ кількість рядків;
# ■ кількість голосних літер;
# ■ кількість приголосних літер;
# ■ кількість цифр.

# import os.path
# import string
#
# path = os.path.join("Strike 2", "strike.txt")
# path2 = os.path.join("Strike 2", "strike2.txt")
# file = open(path, "w")
# file2 = open(path2, "r")
# # base_list = [i[:len(i)-1] for i in file2]
# c = []
# line = file2.read()
# count, count2,count3,count4 = 0,0,0,0
# a = ["a","e","i","o","q","u","y"]
# b = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","w","x","z"]
# print("All symbols in file: ", len(line))
# for i in line:
#    if i in a:
#        count += 1
#    elif i in b:
#        count2 += 1
#    elif i.isdigit():
#        count3 += 1
# print("Light symbols: ", count)
# print("Hard symbols: ", count2)
# print("Numbers: ", count3)
# file2.close()
# file2 = open(path2, "r")
# base_list = [i[:len(i)-1] for i in file2]
# print("String in file: ",len(base_list))
# file.write(str(count)); file.write("\n")
# file.close();file2.close()

# Маємо текстовий файл. Видаліть з нього останній рядок.
# Результат запишіть до іншого файлу.
# import os.path
# path = os.path.join("Strike 2", "strike.txt")
# path2 = os.path.join("Strike 2", "strike2.txt")
# file = open(path, "w")
# file2 = open(path2, "r")
# base_list = [element[:len(element)-1] for element in file2]
# # print(len(base_list))
# base_list.reverse()
# base_list.pop(1)
# base_list.reverse()
# for i in base_list:
#    if i in base_list:
#       print(i)
#    file.write(i); file.write("\n")
# file.close(); file2.close()

# Маємо текстовий файл. Знайдіть довжину найдовшого
# рядка.

# import os.path
#
# path = os.path.join("Strike 2", "strike.txt")
# path2 = os.path.join("Strike 2", "strike2.txt")
# file = open(path, "w")
# file2 = open(path2, "r")
# base_list = [element[:len(element)-1] for element in file2]
# for i in base_list:
#        print(i)
# sort = (sorted(base_list, key=len))
# print("\nMaxsimum size: ",sort[-1])
# print("Minimum size: ",sort[1])
# file.close(); file2.close()

# Маємо текстовий файл. Підрахуйте кількість заданого
# користувачем слова у ньому

# import os.path
# path = os.path.join("Strike 2", "strike.txt")
# file = open(path, "r")
# file2 = open(os.path.join("Strike 2", "strike2.txt"), "a")
# strin = str(input("Take symbol for find! - "))
# a = 0
# line = file.read().split()
# for i in line:
#   if i.startswith(strin):
#      a += 1
#      p = i
#      print("Word - ", i)
#      print("Count - ", a)
#   file2.write(i); file2.write("\n")
# file.close(); file2.close()

# Маємо текстовий файл. Знайдіть і замініть у ньому задане
# слово. Яке слово шукати і на яке замінювати — встановлю-
# ється користувачем.

# import os.path
# path = os.path.join("Strike 2", "strike2.txt")
# file2 = open(path, "r")
# file = open(os.path.join("Strike 2", "strike.txt"), "a")
# line = file2.read()
# print(line)
# xs = []
# a = (input("Take word fo find: "))
# d = (input("Take word for replace: "))
# replace = line.replace(a, d)
# # replace = line.replace('when', 'aasdas')
# print(replace)
# file.write(replace); file.write("\n")
# file.close(); file2.close()