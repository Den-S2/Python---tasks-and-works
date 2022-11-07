# Напишіть функцію, яка виводить на екран форматований
# текст, наведений нижче:

# def first(a):
#     return a
# print(first("\"Don’t compare yourself with anyone in this world...\n  if you do so, you are insulting yourself.\"\n \t\t\t\t\t\t\t\t\t\t  Bill Gates" ))

# Напишіть функцію, яка приймає два числа як параметр
# і відображає усі парні числа між ними.

# def first(a,b):
#     c = []
#     for i in range(a+1, b):
#       if i % 2 == 0:
#          c.append(i)
#     return c
# print(first(int(input("Number 1: ")),int(input("Number 2: "))))

# Напишіть функцію, яка відображає порожній або запо-
# внений квадрат із певним символом. Функція приймає в яко-
# сті параметрів довжину сторони квадрата, символ та змінну
# логічного типу:
# ■ якщо вона дорівнює True, квадрат заповнений;
# ■ якщо False, квадрат порожній.

# def first(a,b,c):
#    count = 0
#    if c == True:
#        while count < b:
#          count += 1
#          print("*" * a)
#    else:
#        while count < b:
#          count += 1
#          print("*" + " " * (a - 2) + "*")
#          print("*" * a)
#        return b
# first(int(input("Size: ")),int(input("Take size 2: ")),(int(input("True or false: "))))

# def first(a,b,c):
#    if c == True:
#        for i in range(a):
#          print((b + " ") * a)
#    else:
#        print((b + " ") * a)
#        for i in range(a-2):
#          d = a - 2
#          print(b + " " + d * "  " + " " + b)
#          print((b + " ") * a)
#        return b
# first(int(input("Size: ")),(input("Take sumbol 2: ")),(int(input("True or false: "))))

# Напишіть функцію, яка повертає мінімальне з п’яти чисел.
# Числа передаються як параметри.

# def first(a):
#    result = min(a)
#    print(result)
#    return a
# first([int(input("Take number : ")) for i in range(5)])

# Напишіть функцію, яка повертає добуток чисел у зазна-
# ченому діапазоні. Межі діапазону передаються як параметри.
# Якщо межі діапазону переплутані (наприклад, 5 — верхня
# межа, 25 — нижня межа), їх треба поміняти місцями.

# def first(a,b):
#     if a > b:
#         a, b = b, a
#     suma = 1
#     for i in range(a, b+1):
#          suma *= i
#     print(suma)
#     return
# first(int(input("Number 1: ")),int(input("Number 2: ")))

# Напишіть функцію, яка підраховує кількість цифр у числі.
# Число передається як параметр. Поверніть з функції отриману
# кількість цифр. Наприклад, якщо передали 3456, кількість
# цифр буде 4.

# def first(a):
#     count = 0
#     for i in a:
#         count += 1
#     return count
# print(first(input("Take number : ")))

# Напишіть функцію, яка перевіряє число на паліндром.
# Число передається як параметр. Якщо число є паліндромом,
# поверніть з функції true, якщо ні — false.
# «Паліндром» — це число, в якому перша частина цифр
# дорівнює другій перевернутій частини цифр. Наприклад,
# 123321 — паліндром (перша частина 123, друга 321, яка після
# перевороту стає 123), 546645 — паліндром, а 421987 — не
# паліндром.

# def first(a):
#     if a == a[::-1]:
#         print("True - ")
#     else:
#         print("False!")
#     return a
# print(first(input("take number : ")))