import pymysql
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Cisco123@45@g",
        database="Museum",
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
        sectora = int(input("""Choose \t #1 Add expo
         #2 Delete expo 
         #3 Update expo's infor 
         #4 Print All exponate
         #5 Print all exponate info
         #6 Print peo of exponate
         #7 Exit: """))
        if sectora == 1:
            add1 = input("Enter name exponate: ")
            add2 = input("Enter infor of expo: ")
            cursor.execute(f"INSERT INTO `Exponate` (Namexpo, Infoexpo) VALUES ('{add1}','{add2}')")
            connection.commit()
            print("Done!")
        elif sectora == 2:
            add2 = input("Enter id from table: ")
            cursor.execute(f"DELETE FROM `Exponate` WHERE id = {add2};")
            connection.commit()
            print("Done!")
        elif sectora == 3:
            print("<:Tag for redact in this sector: Namexpo, Infoexpo:>")
            seltype = input("What are you want redact: ")
            redactdat = input("Infor to replace: ")
            if seltype == "Namexpo":
                name = input("Enter name of exponate from BD: ")
                cursor.execute(f"UPDATE `Exponate` SET {seltype} = '{redactdat}' WHERE Namexpo = '{name}'")
                connection.commit()
                cursor.execute(f"UPDATE `People` SET Linkad = '{redactdat}' WHERE Linkad = '{name}'")
                connection.commit()
                print("Done!")
            else:
                path = input("Enter id of exponate from BD: ")
                cursor.execute(f"UPDATE `Exponate` SET {seltype} = '{redactdat}' WHERE id = {path}")
                connection.commit()
                print("Done!")
        elif sectora == 4:
                cursor.execute(
                    f"SELECT * from `Exponate`")
                result = cursor.fetchall()
                print("\n".join(
                        [f"Id: {row.get('id')}, Name exponate:> {row.get('Namexpo')}, Info of exponate:> {row.get('Infoexpo')} " for row in result]))
        elif sectora == 5:
            name = input("Take name exponate: ")
            cursor.execute(
                f"SELECT * from `Exponate` where Namexpo = '{name}'")
            result = cursor.fetchall()
            print("\n".join(
                [f"Id: {row.get('id')}, Name exponate:> {row.get('Namexpo')}, Info of exponate:> {row.get('Infoexpo')} "
                 for row in result]))
        elif sectora == 6:
            name = input("Take name exponate: ")
            cursor.execute(
                f"SELECT Namepeop, Surnapeop, Linkad from `People` where Linkad = '{name}'")
            result = cursor.fetchall()
            print("\n".join(
                [f"Name peo:> {row.get('Namepeop')}, Surname peo:> {row.get('Surnapeop')}, Exponate peo:> {row.get('Linkad')} "
                 for row in result]))
        elif sectora == 7:
            print("Exit!")
            break