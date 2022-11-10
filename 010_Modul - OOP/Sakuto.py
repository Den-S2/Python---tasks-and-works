# import os.path
# import json
# class Car:
#     def __init__(self, autname, yearbild, engine, color, type):
#         self.autname = autname
#         self.yearbild = yearbild
#         self.engine = engine
#         self.color = color
#         self.type = type
#     def __str__(self):
#         return f"{self.autname},{self.yearbild},{self.engine},{self.color},{self.type}"
#
# car = Car("Toyota MK4", "1999", "2.5", "red", "cupe")
# car2 = Car("Toyota MK5", "2019", "2.5", "blue-metal", "cupe")
# car3 = Car("Toyota Selica", "1994", "1.9", "red", "cupe")
# class Autosalon:
#     def __init__(self, fname):
#         self.fname = fname + ".json"
#         self.path = os.path.join("Strike 2", self.fname)
#     def addcar(self, cars):
#         file = open(self.path, "r")
#         sdict = json.load(file)
#         sdict[cars.autname] = {"Year": cars.yearbild, "Engine l": cars.engine, "Color": cars.color, "Type": cars.type}
#         file.close()
#         file = open(self.path, "w")
#         json.dump(sdict, file); file.close()
#         return f"Adding auto {cars.autname}!"
#     def update(self, cars):
#         file = open(self.path, "r")
#         sdict = json.load(file)
#         sdict[cars.autname] = {"Year": cars.yearbild, "Engine l": cars.engine, "Color": cars.color, "Type": cars.type}
#         file.close()
#         file = open(self.path, "w")
#         json.dump(sdict, file); file.close()
#         return f"Updating auto!"
#     def compas(self, cars, cars1):
#         file = open(self.path, "r")
#         sdict = json.load(file)
#         sd, sd1 = {}, {}
#         for i in sdict[cars.autname]:
#             if (i in sdict[cars.autname] and (sdict[cars.autname][i] != sdict[cars1.autname][i])):
#                 sd[i] = sdict[cars1.autname][i]
#             elif (i in sdict[cars.autname] and (sdict[cars.autname][i] == sdict[cars1.autname][i])):
#                 sd1[i] = sdict[cars1.autname][i]
#         return f"Compas not common {sd} Common is in {sd1}"
#     def sellcar(self, autoname):
#         file = open(self.path, "r")
#         sdict = json.load(file); file.close()
#         sdict.pop(autoname)
#         file = open(self.path, "w")
#         json.dump(sdict, file); file.close()
#         return f"Auto {autoname} sold!"
#     def __str__(self):
#         file = open(self.path, "r")
#         sdict = json.load(file); file.close()
#         return "\n".join([f"{item}, {sdict.get(item).get('Year')}, \
# {sdict.get(item).get('Engine l')}, {sdict.get(item).get('Color')}, {sdict.get(item).get('Type')}" for item in sdict])
# auto = Autosalon("new2")
# print(auto.addcar(car))
# print(auto.addcar(car2))
# print(auto.addcar(car3)); print(auto)
# print(auto.compas(car,car2))
# print(auto.sellcar(input("Enter name car: "))); print(auto)