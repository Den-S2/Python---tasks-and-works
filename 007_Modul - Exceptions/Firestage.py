#Опишите класс сотрудника, который включает в себя такие поля, как имя,
#фамилия, отдел и год поступления на работу. Конструктор должен генерировать
#исключение, если заданы неправильные данные. Введите список работников с клавиатуры.
#Выведите всех сотрудников, которые были приняты после заданного года.

# class Employer:
#     def __init__(self, name, surname, depart, year):
#         self.name = name
#         self.surname = surname
#         self.depart = int(depart)
#         self.year = int(year)
#         if int(year) <= 1982 or int(year) >= 2022:
#            raise ("Wrong year!")
#         else:
#             self.year = int(year)
#         self.emlist = []
#     def __str__(self):
#         return f"Name: {self.name}, Surname: {self.surname}, Depart: {self.depart}, Year: {self.year}:>"
#
# class Emp:
#     def __init__(self, fname):
#          self.fname = fname + ".txt"
#          self.path = os.path.join("Strike 2", self.fname)
#     def addemp(self, empys):
#             file = open(self.path, "a")
#             file.write(str(empys) + "\n"); file.close()
#             return f"Adding employ!"
#     def findper(self, empys):
#         file = open(self.path, "r")
#         list = [i for i in file if empys in i]; file.close()
#         return list
#     def showper(self):
#         file = open(self.path, "r")
#         line = [i for i in file]
#         return f"All personal: {line}"
#     def __str__(self):
#         file = open(self.path, "r")
#         line = [i for i in file]
#         return "".join(line)
# empp = Emp("employer")
# while True:
#     sec = int(input("Choose mode #1 print employer #2 add employer #3 Find for year #4 Exit: "))
#     if sec == 1:
#         print(empp.showper())
#     elif sec == 2:
#         try:
#          empy = Employer(input("Take name: "), input("Take surname: "), input("Take depart: "), input("Take year: "))
#         except ValueError:
#             print("Diff value! ")
#         else:
#             print(empp.addemp(empy))
#     elif sec == 3:
#         print(empp.findper(input("Take year: ")))
#     elif sec == 4:
#         print("Exit!")
#         break