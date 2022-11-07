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