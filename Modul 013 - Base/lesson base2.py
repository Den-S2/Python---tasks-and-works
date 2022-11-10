import pymysql
import os.path
import json
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Cisco123@45@g",
        database="sales",
        cursorclass=pymysql.cursors.DictCursor     )
    print("Okay")
# finally: connection.close()
except: print("error")
# class File():
#     def __init__(self, fle):
#         self.fle = fle + ".json"
#         self.path = os.path.join(input("Enter path: "), self.fle)
#     def show(self, file):
#         file = open(self.path, "r")
#     def write(self, file):
#         file = open(self.path, "a")
# f2 = File(input("Name of file: "))
while True:
    sector = int(input("Choose menu #1 Data info #2 Redact data #3 Work with file #4 Exit: "))
    if sector == 1:
        sector1 = int(input("""\t\t  1 - Відображення усіх угод,
          2 - Відображення угод конкретного продавця,
          3 - Відображення максимальної за сумою угоди,
          4 - Відображення мінімальної за сумою угоди,
          5 - Відображення максимальної суми угоди для конкретного продавця,
          6 - Відображення мінімальної за сумою угоди для конкрет-ного продавця,
          7 - Відображення максимальної за сумою угоди для конкрет-ного покупця,
          8 - Відображення мінімальної за сумою угоди для конкрет-ного покупця,
          9 - Відображення продавця з максимальною сумою продажів за всіма угодами,
          10 - Відображення продавця з мінімальною сумою продажів за всіма угодами,
          11 - Відображення покупця з максимальною сумою покупок за всіма угодами,
          12 - Відображення середньої суми покупки для конкретного покупця,
          13 - Відображення середньої суми покупки для конкретного продавця: """))

        if sector1 == 1:
                with connection.cursor() as cursor:
                    select_all = "SELECT * FROM `Sales`;"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 2:
                with connection.cursor() as cursor:
                    namesale = input("Take namesale: ")
                    select_all = f"SELECT Informan FROM Salesman where Namman = '{namesale}';"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 3:
                with connection.cursor() as cursor:
                    select_all = "SELECT max(Summas) FROM Sales where Summas;"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 4:
                with connection.cursor() as cursor:
                    select_all = "SELECT min(Summas) FROM Sales where Summas;"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 5:
                with connection.cursor() as cursor:
                    namesale = input("Take namesale: ")
                    select_all = f"SELECT max(Summas) FROM Sales where Namsale = '{namesale}';"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 6:
                with connection.cursor() as cursor:
                    namesale = input("Take namesale: ")
                    select_all = f"SELECT min(Summas) FROM Sales where Namsale = '{namesale}';"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 7:
                with connection.cursor() as cursor:
                    namecu = input("Take namesale: ")
                    select_all = f"SELECT min(Summas1) FROM Customer where Namcus = '{namecu}';"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 8:
                with connection.cursor() as cursor:
                    namecu = input("Take namesale: ")
                    select_all = f"SELECT max(Summas1) FROM Customer where Namcus = '{namecu}';"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 9:
                with connection.cursor() as cursor:
                    select_all = f"SELECT Namsale, max(Summas) from Sales where Summas = (select max(Summas) from Sales);"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 10:
                with connection.cursor() as cursor:
                    select_all = f"SELECT Namsale, min(Summas) from Sales where Summas = (select min(Summas) from Sales);"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 11:
                with connection.cursor() as cursor:
                    select_all = f"SELECT Namcus, max(Summas1) from Customer where Summas1 = (select max(Summas1) from Customer);"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 12:
                with connection.cursor() as cursor:
                    namecu = input("Take namecust: ")
                    select_all = f"SELECT avg(Summas1) FROM Customer where Namcus = '{namecu}';"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
        elif sector1 == 13:
                with connection.cursor() as cursor:
                    namesale = input("Take namesale: ")
                    select_all = f"SELECT avg(Summas) FROM Sales where Namsale = '{namesale}';"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    ask = input("Enter name file: ")
                    file = open(os.path.join(ask + ".txt"), "a")
                    for row in result:
                        print(row)
                        file.write(str(row) + "\n")
                    file.close()
    elif sector == 2:
        sector1 = int(input("Enter #1 - insert, #2 - update or #3 - delete: "))
        if sector1 == 1:
            with connection.cursor() as cursor:
                sel = input("Print name table: ")
                if sel == "Sales":
                    date1 = input("Take namesale: ")
                    date2 = float(input("Take summa: "))
                    insert = f"INSERT INTO `Sales` (Namsale, Summas) VALUES ('{date1}', '{date2}')"
                    cursor.execute(insert)
                    connection.commit()
                elif sel == "Salesman":
                    date1 = input("Take saller name: ")
                    date2 = input("Take infor: ")
                    insert = f"INSERT INTO `Salesman` (Namman, Informan) VALUES ('{date1}', '{date2}')"
                    cursor.execute(insert)
                    connection.commit()
                elif sel == "Customer":
                    date1 = input("Take namesale: ")
                    date2 = input("Take information: ")
                    date3 = float(input("Take summa: "))
                    insert = f"INSERT INTO `Customer` (Namcus, Inforcus, Summas1) VALUES ('{date1}', '{date2}, '{date3}')"
                    cursor.execute(insert)
                    connection.commit()
                else:
                    print("You write wrong name Table or this isn't exist!")
        elif sector1 == 2:
            with connection.cursor() as cursor:
                sel = input("Print name table: ")
                if sel == "Sales":
                    print("<:Info for redact in this sector: Namsale, Summas:>")
                    seltype = input("What are you want redact: ")
                    redactdat = input("Infor to replace: ")
                    path = input("Enter id of person from BD: ")
                    create_table = f"UPDATE `Sales` SET {seltype} = '{redactdat}' WHERE id = {path}"
                    cursor.execute(create_table)
                    connection.commit()
                elif sel == "Salesman":
                    print("<:Info for redact in this sector: Namman, Informan:>")
                    seltype = input("What are you want redact: ")
                    redactdat = input("Infor to replace: ")
                    path = input("Enter id of person from BD: ")
                    create_table = f"UPDATE `Salesman` SET {seltype} = '{redactdat}' WHERE id = {path}"
                    cursor.execute(create_table)
                    connection.commit()
                elif sel == "Customer":
                    print("<:Info for redact in this sector: Namcus, Inforcus, Summas1:>")
                    seltype = input("What are you want redact: ")
                    redactdat = input("Infor to replace: ")
                    path = input("Enter id of person from BD: ")
                    create_table = f"UPDATE `Customer` SET {seltype} = '{redactdat}' WHERE id = {path}"
                    cursor.execute(create_table)
                    connection.commit()
                else:
                    print("You write wrong name Table or this isn't exist!")
        elif sector1 == 3:
            with connection.cursor() as cursor:
                sel = input("Print name table: ")
                create_table = f"DROP TABLE `{sel}`"
                cursor.execute(create_table)
    elif sector == 3:
        ask = input("Enter name file: ")
        file = open(os.path.join(ask + ".txt"), "r")
        line = file.read()
        print(line)
    elif sector == 4:
        print("Exit!")
        break
#Create BD
# class Creation():
#     def creat(self):
#         with connection.cursor() as cursor:
#              self.s = "create database People"
#              try:
#                  cursor.execute(self.s)
#                  print("well done")
#              except: print("Error!")
# class Useb():
#     def use(self):
#          with connection.cursor() as cursor:
#              try:
#                  connection.select_db(input("Db name: "))
#                  connection.commit
#                  print("operation done")
#              except Exception as error:
#                  print(error)
# cr = Creation()
# us = Useb()
# while True:
#     sector = int(input("Take 1 to create or 2 to use it: "))
#     if sector == 1:
#        print(cr.creat())
#     if sector == 2:
#        print(us.use())
#     if sector == 3:
#         break

# Create BD
# with connection.cursor() as cursor:
#      create_table = "CREATE DATABASE `students`"
#      try:
#          cursor.execute(create_table)
#          print("well done")
#      except: print("Error!")

# Create table
# with connection.cursor() as cursor:
#     create_table = "CREATE TABLE `students` (id int AUTO_INCREMENT, name varchar(30), password varchar(30), PRIMARY KEY (id));"
#     cursor.execute(create_table)
#     print("well done")

# Insert data
# with connection.cursor() as cursor:
#     insert = "INSERT INTO `students` (name, password) VALUES ('Sasha', '12345'), ('Sasha', '123456')"
#     cursor.execute(insert)
#     connection.commit()

# Drope table
# with connection.cursor() as cursor:
#     create_table = "DROP TABLE `students`"
#     cursor.execute(create_table)
# with connection.cursor() as cursor:
#     create_table = "CREATE DATABASE `students`"
#     cursor.execute(create_table)

# Delete data
# with connection.cursor() as cursor:
#     create_table = "DELETE FROM `students` WHERE name='Sasha';"
#     cursor.execute(create_table)
#     connection.commit()

