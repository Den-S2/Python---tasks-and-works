import pymysql
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Cisco123@45@g",
        database="Note",
        cursorclass=pymysql.cursors.DictCursor     )
    print("Okay")
# finally: connection.close()
except: print("error")
count = 0
while True:
  with connection.cursor() as cursor:
    log = input("Enter your login: ")
    passwd = input("Enter your password: ")
    select_all = f"SELECT Login,Passwd FROM `Auth` where Login = '{log}';"
    cursor.execute(select_all)
    result = cursor.fetchall()
    print(result)
    try:
        if result[0].get('Login') == log and result[0].get('Passwd') == passwd:
            print("You logged in!")
        else:
            count = +1
            print("Bad password!")
            continue
    except:
         print("Incorrect password!")
         break
    while True:
        sectora = int(input("""Choose \t #1 Add note
         #2 Delete note 
         #3 Update note 
         #4 Print all note
         #5 Print note from date
         #6 Print note with some word
         #7 Exit: """))
        if sectora == 1:
            add1 = input("Enter name note: ")
            add2 = input("Enter infor of note: ")
            add3 = input("Enter date of note: ")
            cursor.execute(f"INSERT INTO `Notepad` (Namenot, Infonot, Datenot) VALUES ('{add1}','{add2}','{add3}')")
            connection.commit()
            print("Done!")
        elif sectora == 2:
            add2 = input("Enter id from table: ")
            cursor.execute(f"DELETE FROM `Notepad` WHERE id = {add2};")
            connection.commit()
            print("Done!")
        elif sectora == 3:
            print("<:Tag for redact in this sector: Namenot, Infonot, Datenot:>")
            seltype = input("What are you want redact: ")
            redactdat = input("Infor to replace: ")
            path = input("Enter id of note from BD: ")
            cursor.execute(f"UPDATE `Notepad` SET {seltype} = '{redactdat}' WHERE id = {path}")
            connection.commit()
            print("Done!")
        elif sectora == 4:
            cursor.execute(
                f"SELECT * from `Notepad`")
            result = cursor.fetchall()
            print("\n".join(
                [f"Id: {row.get('id')}, Name note:> {row.get('Namenot')}, Info of note:> {row.get('Infonot')}, Date of note:> {row.get('Datenot')} "
                 for row in result]))
        elif sectora == 5:
            date = input("Take date of note: ")
            cursor.execute(
                f"SELECT * FROM `Notepad` where Datenot >= '{date}'")
            result = cursor.fetchall()
            print("\n".join(
                [f"Name note:> {row.get('Namenot')}, Info of note:> {row.get('Infonot')}, Date of note:> {row.get('Datenot')} "
                 for row in result]))
        elif sectora == 6:
            some = input("Take some words: ")
            cursor.execute(
                f"select Namenot, Infonot from `Notepad` where (select locate('{some}', Infonot))")
            result = cursor.fetchall()
            print("\n".join([f"Name note:> {row.get('Namenot')}, Info of note:> {row.get('Infonot')} " for row in result]))
        elif sectora == 7:
            print("Exit!")
            break