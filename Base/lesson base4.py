import pymysql
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Cisco123@45@g",
        database="Messanger",
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
        sectora = int(input("""Choose \t #1 Add user
         #2 Delete user 
         #3 Update user's infor 
         #4 Find full NSEl
         #5 Print user's infor
         #6 Print user's friends
         #7 Print user's publishers
         #8 Exit: """))
        if sectora == 1:
            add1 = input("Enter name user: ")
            add2 = input("Enter surname user: ")
            add3 = input("Enter elname user: ")
            add4 = input("Enter short user's infor: ")
            cursor.execute(f"INSERT INTO `User` (Nameuser, Surnauser, Elnauser, Infouser) VALUES ('{add1}','{add2}', '{add3}', '{add4}')")
            connection.commit()
            print("Done!")
        elif sectora == 2:
            add2 = input("Enter id from table: ")
            cursor.execute(f"DELETE FROM `User` WHERE id = {add2};")
            connection.commit()
            print("Done!")
        elif sectora == 3:
            print("<:Tag for redact in this sector: Nameuser, Surnauser, Elnauser, Infouser:>")
            seltype = input("What are you want redact: ")
            redactdat = input("Infor to replace: ")
            if seltype == "Nameuser":
                name = input("Enter name of person from BD: ")
                cursor.execute(f"UPDATE `User` SET {seltype} = '{redactdat}' WHERE Nameuser = '{name}'")
                connection.commit()
                cursor.execute(f"UPDATE `Friend` SET Linkad = '{redactdat}' WHERE Linkad = '{name}'")
                connection.commit()
                cursor.execute(f"UPDATE `Publish` SET Linkpub = '{redactdat}' WHERE Linkpub = '{name}'")
                connection.commit()
                print("Done!")
            else:
                path = input("Enter id of person from BD: ")
                cursor.execute(f"UPDATE `User` SET {seltype} = '{redactdat}' WHERE id = {path}")
                connection.commit()
                print("Done!")
        elif sectora == 4:
                name = input("Take name user: ")
                surname = input("Take surname user: ")
                elna = input("Take elname user: ")
                cursor.execute(
                    f"SELECT * from `User` where Nameuser = '{name}' and Surnauser = '{surname}' and Elnauser = '{elna}'")
                try:
                    result = cursor.fetchall()
                    print("\n".join(
                        [f"Id: {row.get('id')}, Name:> {row.get('Nameuser')}, Surname:> {row.get('Surnauser')}, Elname:> {row.get('Elnauser')},\
 Information:> {row.get('Infouser')} " for row in result]))
                except:
                   print("Wrong user!")
        elif sectora == 5:
            name = input("Take name user: ")
            cursor.execute(f"SELECT Infouser from `User` where Nameuser = '{name}';")
            result = cursor.fetchall()
            print("\n".join([f"Information:> {row.get('Infouser')} " for row in result]))
        elif sectora == 6:
            name = input("Take name user: ")
            cursor.execute(f"SELECT count(Namefrie) from `Friend` where Linkad = '{name}';")
            result = cursor.fetchall()
            print("\n".join([f"Friends:> {row.get('count(Namefrie)')} " for row in result]))
            seld = input("Do you want see all friend:> yes or no: ")
            if seld == "yes":
                cursor.execute(f"SELECT Namefrie from `Friend` where Linkad = '{name}';")
                result = cursor.fetchall()
                print("\n".join([f"Friends:> {row.get('Namefrie')} " for row in result]))
            elif seld == "no":
                print("Run away!")
        elif sectora == 7:
            name = input("Take name user: ")
            cursor.execute(f"SELECT count(Infopub) from `Publish` where Linkpub = '{name}';")
            result = cursor.fetchall()
            print("\n".join([f"Publish:> {row.get('count(Infopub)')} " for row in result]))
            seld = input("Do you want see all friend:> yes or no: ")
            if seld == "yes":
                cursor.execute(f"SELECT Infopub from `Publish` where Linkpub = '{name}';")
                result = cursor.fetchall()
                print("\n".join([f"Publish:> {row.get('Infopub')} " for row in result]))
            elif seld == "no":
                print("Run away!")
        elif sectora == 8:
            print("Exit!")
            break