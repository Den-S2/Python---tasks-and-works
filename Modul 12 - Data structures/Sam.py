#Користувач вводить з клавіатури набір рядків. Збере-жіть отримані
# рядки до двозв’язного списку. Після чого покажіть меню, в якому
# запропонуєте користувачеві набір пунктів:
#
# text = input("Enter words: ")
# text1 = text.split()
# print(text1)
# while True:
#   sec = int(input("#1 add #2 remove #3 show #4 find #5 replace: "))
#   if sec == 1:
#       texts = input("Enter num for add: ")
#       if texts in text1:
#         print("This word in case!")
#       else:
#        text1.append(texts)
#   elif sec == 2:
#       texts = input("Enter word for remove: ")
#       text1.remove(texts)
#   elif sec == 3:
#       print(text1)
#   elif sec == 4:
#       texts = input("Enter word for find: ")
#       for i in text1:
#           if texts in i:
#               print("This word is: ", i)
#           else:
#               print("Not word in list!")
#   elif sec == 5:
#       texts = int(input("Enter index: "))
#       text2 = input("Enter word for replace: ")
#       text1[texts - 1] = text2
#       print(text1)
#   elif sec == 6:
#       print("Exit!")
#       break

# Реалізуйте клас стека роботи з цілими значеннями (стек цілих).
#
# class Stek:
#     def __init__(self, num1):
#             self.num1 = num1
#
#     def add(self, num):
#         self.num1.append(num)
#         return "Num adds to list!"
#     def remove(self, num):
#         if num in self.num1:
#           self.num1.remove(num)
#           return "Num remove from list!"
#     def show(self):
#         return f"{self.num1}"
#     def countl(self):
#         return f"{len(self.num1)}"
#     def empty(self):
#         if self.num1 == []:
#             return True
#         else:
#             return False
#     def clear(self):
#         self.num1 = []
#         return "List clear!"
#     def find(self, num):
#         if num in self.num1:
#            return True
#         else:
#            return False
#     def repla(self, fnum, num):
#         self.num1[self.num1.index(fnum)] = num
#         return "Num is replace!"
# stel = int(input("Choose mode #1 Work with num #2 Work with word: "))
# if stel == 1:
#   numus = Stek(list(map(int, input("Enter first num: ").split())))
# elif stel == 2:
#   numus = Stek(list(map(str, input("Enter first word: ").split())))
#
# while True:
#  sec = int(input("#1 add #2 remove #3 show #4 find #5 replace: "))
#  if sec == 1:
#    print(numus.add(input("Enter param for add: ")))
#  elif sec == 2:
#    print(numus.remove(input("Enter param for remove: ")))
#  elif sec == 3:
#    print(numus.show())
#  elif sec == 4:
#    print(numus.find(input("Enter param for find: ")))
#  elif sec == 5:
#      print(numus.repla(input("Enter param for : "), input("Enter param for replace: ")))