#Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій

# class Car:
#     def __init__(self, autname, yearbild, engine, color, price):
#         self.autname = autname
#         self.yearbild = yearbild
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     def cheng(self):
#         self.engine = input("Enter engine l: ")
#         return "I cool!"
#     def teng(self):
#         if self.engine.startswith("1") == True:
#             return "To small engine!"
#     def rul_pr(self, number):
#         self.price = number
#         return "okay"
#     def tpri(self):
#         if self.price.endswith("$") == True or self.price.endswith("ua"):
#             return "okay"
#         else:
#             return self.rul_pr(input("number: "))
#     def cyear(self):
#         self.yearbild = input("Enter a year: ")
#         return "You right!"
#     def tyear(self):
#         if self.yearbild.startswith("09") == False and self.yearbild.endswith("99") == True:
#             return "No gooddamn"
#     def __str__(self):
#         return f"{self.autname}, {self.yearbild}, {self.engine}, {self.color}, {self.price}"
# auto = Car("Nissan","2005","1.9","black","2500rub")
# print(auto)
# print(auto.cheng())
# print(auto)
# print(auto.tpri())
# print(auto)
# print(auto.cyear())
# print(auto)

#Реалізуйте клас «Книга». Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

# class Book:
#     def __init__(self, namebook, yearbild, genre, autor, price):
#         self.namebook = namebook
#         self.yearbild = yearbild
#         self.genre = genre
#         self.autor = autor
#         self.price = price
#
#     def cheng(self):
#         self.genre = input("Enter genre: ")
#         return "Oh nice!"
#     def teng(self):
#         if self.genre.startswith("ro") == True:
#             return "Sorry but this genre is end!"
#     def rul_pr(self, number):
#         self.price = number
#         return "okay"
#     def tpri(self):
#         if self.price.endswith("$") == True or self.price.endswith("ua"):
#             return "okay"
#         else:
#             return self.rul_pr(input("number: "))
#     def cyear(self):
#         self.yearbild = input("Enter a year: ")
#         return "You right!"
#     def tyear(self):
#         if self.yearbild.startswith("09") == False and self.yearbild.endswith("99") == True:
#             return "No gooddamn"
#     def __str__(self):
#         return f"{self.namebook}, {self.yearbild}, {self.genre}, {self.autor}, {self.price}"
# list = Book("Back on earth","2001","rommancy","Nolan Black","2500rub")
# print(list)
# print(list.cheng())
# print(list)
# print(list.tpri())
# print(list)
# print(list.cyear())
# print(list)

#Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття,
# країну, місто, місткість. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

# class Stadium:
#     def __init__(self, stadname, yearbild, country, city, count):
#         self.stadname = stadname
#         self.yearbild = yearbild
#         self.country = country
#         self.city = city
#         self.count = count
#
#     def cheng(self, text):
#         self.country = text
#         return "Oh nice!"
#     def teng(self):
#         if self.country.startswith("Rus") == True:
#             return "Sorry but this country is dead!"
#         else:
#             return self.cheng(input("text: "))
#     def rul_pr(self, number):
#         self.count = number
#         return "okay"
#     def tpri(self):
#         if self.count > 1000 or self.count < 5000:
#             return "okay"
#         else:
#             return self.rul_pr(input("number: "))
#     def cyear(self):
#         self.yearbild = input("Enter a year: ")
#         return "You right!"
#     def tyear(self):
#         if self.yearbild.startswith("09") == False and self.yearbild.endswith("99") == True:
#             return "No gooddamn"
#     def __str__(self):
#         return f"{self.stadname}, {self.yearbild}, {self.country}, {self.city}, {self.count}"
# lia = Stadium("Buckernecky","1999","Latvia","Riga", 2500)
# print(lia)
# print(lia.teng())
# print(lia)
# print(lia.tpri())
# print(lia)
# print(lia.cyear())
# print(lia)