# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палин-
# дром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.

# string = str(input(" Take string - "))
# string3 = string.replace(" ", "")
# string2 = string3[::-1]
#
# if string3.lower() == string2.lower():
#      print("Result -",string)
# else:
#     print(" Error! ")

# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

# string = str(input(" Take string - "))
# string2 = str(input(" Take find words - "))
# string3 = string2.title()
#
# print(string.replace(string2, string3))

# Есть некоторый текст. Посчитайте в этом тексте ко-
# личество предложений и выведите на экран полученный
# результат.

string = str("     He had three simple rules by which he lived! The first was to never eat blue food.\n  \t There was nothing in nature that was edible that was blue. People often asked about blueberries,\n \t but everyone knows those are actually purple. He understood it was one of the stranger rules to live by,\n \t but it had served him well thus far in the 50+ years of his life.It was a weird concept. Why would I really\n \t need to generate a random paragraph? Could I actually learn something from doing so? All these questions\n \t were running through her head as she pressed the generate button. To her surprise, she found what\n \t she least expected to see 10 fishes.")
print(string)
counta,countc = 0,0
for i in string:
    if i == "." or i == "?" or i == "!":
      counta += 1
    elif i.isdigit():
        countc += 1

print(" Sentences - ", counta)
print(" Numbers in - ", countc)