import pymysql
import os.path
import json
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Cisco123@45@g",
        database="sakila",
        cursorclass=pymysql.cursors.DictCursor     )
    print("Okay")
# finally: connection.close()
except: print("error")
with connection.cursor() as cursor:
  while True:
        sector = int(input("Sec 1 #1 Creation\n \t  #2 Redact/Select\n \t  #3 Exit: "))
        if sector == 1:
                 section = int(input("#1 Creation BD #2 Used BD #3 Creation table: "))
                 try:
                     if section == 1:
                         selec = input("Take name of BD: ")
                         cursor.execute(f"create database {selec}")
                         print("well done")
                     elif section == 2:
                         connection.select_db(input("Db name: "))
                         connection.commit()
                         print("operation done")
                     elif section == 3:
                         data = input("Take name table: ")
                         try:
                             data = "peop"
                             cursor.execute(f"CREATE TABLE `{data}` (id int AUTO_INCREMENT, name varchar(30), age int, city varchar(100), country varchar(100), PRIMARY KEY (id));")
                             print("well done")
                         except: print("Error!")
                 except: print("Error!")
        elif sector == 2:
              sectio = int(input("Sec 2 #1 Select your command\n \t  #2 Ready part select\n \t  #3 Insert\n \t  #4 Update\n \t  #5 Delete: "))
              if sectio == 1:
                  # select_all = "SELECT * FROM `students`;"
                  cursor.execute(input("Take command: "))
                  result = cursor.fetchall()
                  ask = input("Enter name file: ")
                  file = open(os.path.join(ask + ".txt"), "a")
                  print("\n".join([f"Id: {row.get('id')}, Name:> {row.get('name')}, Age:> {row.get('age')}, City:> {row.get('city')},\
 Country:> {row.get('country')} " for row in result]))
                  file.write(str(result) + "\n")
                  file.close()
              elif sectio == 2:
                  query = input("Enter filter age, city or country: ")
                  if query == "age":
                      data = input("Enter name table: ")
                      age = int(input("Enter age: "))
                      cursor.execute(f"SELECT name, age FROM `{data}` where age = '{age}';")
                      result = cursor.fetchall()
                      ask = input("Enter name file: ")
                      file = open(os.path.join(ask + ".txt"), "a")
                      print("\n".join([f"Name:> {row.get('name')}, Age:> {row.get('age')} " for row in result]))
                      file.write(str(result) + "\n"); file.close()
                  elif query == "city":
                      data = input("Enter name table: ")
                      city = input("Enter city: ")
                      cursor.execute(f"SELECT name, city FROM `{data}` where city = '{city}';")
                      result = cursor.fetchall()
                      ask = input("Enter name file: ")
                      file = open(os.path.join(ask + ".txt"), "a")
                      print("\n".join([f"Name:> {row.get('name')}, City:> {row.get('city')} " for row in result]))
                      file.write(str(result) + "\n"); file.close()
                  elif query == "country":
                      data = input("Enter name table: ")
                      country = input("Enter country: ")
                      cursor.execute(f"SELECT name, country FROM `{data}` where country = '{country}';")
                      result = cursor.fetchall()
                      ask = input("Enter name file: ")
                      file = open(os.path.join(ask + ".txt"), "a")
                      print("\n".join([f"Name:> {row.get('name')}, Country:> {row.get('country')} " for row in result]))
                      file.write(str(result) + "\n"); file.close()
              elif sectio == 3:
                  data = input("Enter name table: ")
                  name = input("Enter name person: ")
                  age = int(input("Enter age: "))
                  city = input("Enter name of city: ")
                  country = input("Enter name of country: ")
                  cursor.execute(
                      f"INSERT INTO `{data}` (name, age, city, country) VALUES ('{name}','{age}', '{city}','{country}')")
                  connection.commit()
              elif sectio == 4:
                  print("<:Tag for redact in this sector: name, age, city, country:>")
                  data = input("Enter name table: ")
                  seltype = input("What are you want redact: ")
                  path = input("Enter id of person from BD: ")
                  if seltype == "name" or seltype == "city" or seltype == "country":
                     seltrip = input("Take redact text: ")
                     cursor.execute(f"UPDATE `{data}` SET {seltype} = '{seltrip}' WHERE id = {path}")
                     connection.commit()
                     print("Done!")
                  elif seltype == "age":
                      seltrip = int(input("Take age: "))
                      cursor.execute(f"UPDATE `{data}` SET {seltype} = '{seltrip}' WHERE id = {path}")
                      connection.commit()
                      print("Done!")
              elif sectio == 5:
                  data = input("Enter name table: ")
                  name = input("Enter name person: ")
                  cursor.execute(f"DELETE FROM `{data}` WHERE name = '{name}';")
                  connection.commit()
                  print("Done!")
        elif sector == 3:
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
# while True:
#     sector = int(input("Enter number #1 create BD and table #2 Select"))
#     if sector == 1:
#         with connection.cursor() as cursor:
#              na = input("Enter name of BD: ")
#              create_table = f"CREATE DATABASE `{na}`"
#              try:
#                  cursor.execute(create_table)
#                  print("well done")
#              except: print("Error!")
#     elif sector == 2:
#         with connection.cursor() as cursor:
#             select_all = input("Enter select command: ")
#             cursor.execute(select_all)
#             result = cursor.fetchall()
#             print(result)
#             for row in result:
#                 print(row)

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

# Update data
# with connection.cursor() as cursor:
#     create_table = "UPDATE `students` SET password = 'qwerty' WHERE id = 6"
#     cursor.execute(create_table)
#     connection.commit()

# Select data
# with connection.cursor() as cursor:
#     select_all = "SELECT * FROM `students`;"
#     cursor.execute(select_all)
#     result = cursor.fetchall()
#     print(result)
#     for row in result:
#         print(row)