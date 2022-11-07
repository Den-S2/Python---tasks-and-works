# Створіть базовий клас «Фігура» з методом для підрахунку
# площі. Створіть похідні класи: прямокутник, коло, прямокутний трикутник, трапеція, зі своїми методами для підрахунку
# площі.

# import os.path
# import string
# class Figure:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
# class Squade(Figure):
#     def __str__(self):
#         return f"Num1 = {self.num1}, Num2 = {self.num2} Rectangle S = {self.num1 * self.num2}"
# class Trian(Figure):
#     def __str__(self):
#         return f"Num1 = {self.num1}, Num2 = {self.num2} Right triangle S = {(self.num1 * self.num2) / 2}"
# class Circ(Figure):
#     def __str__(self):
#         return f"Num1 = {self.num1} Circle S = {3.14 * pow(self.num1,2)}"
# class Trap(Figure):
#     def __init__(self, num1, num2, num3):
#         self.num3 = num3
#         super().__init__(num1, num2)
#
#     def __str__(self):
#         return f"Num1 = {self.num1}, Num2 = {self.num2}, Num3 = {self.num3} Trapecia S = {((self.num1 + self.num2) / 2) * self.num3}"
# while True:
#  sec = int(input("Take mode #1 - Check file or #2 - Print answer formula in file! "))
#  if sec == 1:
#     file = open(os.path.join("Strike 2", "strt.txt"), "r")
#     br = file.read()
#     print(br)
#  elif sec == 2:
#     secr = int(input("Take formula #1 - S Squade #2 - S Triangle #3 - S Circle #4 - S Trap! "))
#     if secr == 1:
#        file = open(os.path.join("Strike 2", "strt.txt"), "a")
#        squ = Squade(5,3); print(squ)
#        file.write(str(squ) + "\n"); file.close()
#     elif secr == 2:
#         file = open(os.path.join("Strike 2", "strt.txt"), "a")
#         tri = Trian(5,3); print(tri)
#         file.write(str(tri) + "\n"); file.close()
#     elif secr == 3:
#         file = open(os.path.join("Strike 2", "strt.txt"), "a")
#         ci = Circ(10,1); print(ci)
#         file.write(str(ci) + "\n"); file.close()
#     elif secr == 4:
#         file = open(os.path.join("Strike 2", "strt.txt"), "a")
#         tra = Trap(5,3,5); print(tra)
#         file.write(str(tra) + "\n"); file.close()