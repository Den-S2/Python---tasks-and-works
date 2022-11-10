import pymysql
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
