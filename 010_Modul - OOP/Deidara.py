#Створіть клас Device, який містить інформацію про при-
# стрій.За допомогою механізму успадкування реалізуйте клас
# CoffeeMachine (містить інформацію про кавомашину), клас
# Blender (містить інформацію про блендер), клас MeatGrinder
# (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

# class Device:
#     def __init__(self, name):
#         self.name = name
# class CoffeMachine(Device):
#     def __str__(self):
#         return f"Can make coffe on morning - {self.name}"
# class Blender(Device):
#     def __str__(self):
#         return f"Can blend anything - {self.name}"
# class MeatGrinder(Device):
#     def __str__(self):
#         return f"Can small grind meat - {self.name}"
# coffe = CoffeMachine("Watawa");print(coffe)
# blend = Blender("Mantis");print(blend)
# meat = MeatGrinder("Atona");print(meat)

#Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас
# Frigate (містить інформацію про фрегат), клас Destroyer (містить
# інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

# class Ship:
#     def __init__(self, name):
#         self.name = name
# class Frigate(Ship):
#     def __str__(self):
#         return f"Frigate: {self.name} is of air warfare frigates was developed in Germany."
# class Destroyer(Ship):
#     def __str__(self):
#         return f"Destroyer: {self.name} technological advances have improved the capability of modern destroyers culminating"
# class Cruiser(Ship):
#     def __str__(self):
#         return f"Cruiser: {self.name} cruisers are new multi-role ships of the US Navy."
# coffe = Frigate("Sachsen");print(coffe)
# blend = Destroyer("Arleigh Burke");print(blend)
# meat = Cruiser("Zumwalt");print(meat)

#Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для збері-
# гання копійок (центи, євроценти, копійки тощо). Реалізуйте методи виведення суми на екран, задання
# значень частин.
# Створіть клас Product для роботи з продуктом або то-
# варом беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.

# class Money:
#     def __init__(self, fullmo, centmo, sfullmo, scentmo, conm):
#         self.fullmo = int(fullmo)
#         self.centmo = int(centmo)
#         self.sfullmo = int(sfullmo)
#         self.scentmo = int(scentmo)
#         self.conm = conm
#
#     def __str__(self):
#         return f"Money {self.fullmo}.{self.centmo}, Product {self.sfullmo}.{self.scentmo}"
#
# class Product(Money):
#
#     def convert(self, conm):
#         if conm == "USD" and self.conm == "UA":
#             self.fullmo /= 37.16
#             return "Okay!"
#         elif conm == "USD" and self.conm == "EU":
#             self.fullmo *= 1.83
#         elif conm == "UA" and self.conm == "USD":
#             self.fullmo *= 37.16
#         elif conm == "UA" and self.conm == "EU":
#             self.fullmo *= 36.16
#
#     def chamo(self):
#         self.fullmo = int(input("Full-money: "))
#         self.centmo = int(input("Cent-money: "))
#         return self.testmo()
#     def testmo(self):
#         if self.fullmo < self.sfullmo:
#             print(f"Product cost: {self.sfullmo}.{self.scentmo}")
#             print("Too small money:")
#             return self.chamo()
#         else:
#             print(f"Product cost: {self.sfullmo}.{self.scentmo}")
#             return f"Balance: {self.fullmo - self.sfullmo}.{self.centmo - self.scentmo}"
# bank = Product(input("Enter full-money: "),input("Enter cent-money: "), 35,13, input("Enter value: "))
# print(bank.convert("USD"));print(bank)
# print(bank.testmo());print(bank)