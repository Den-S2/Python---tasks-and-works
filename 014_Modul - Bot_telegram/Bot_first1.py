import telebot
import pymysql
from telebot import types

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Cisco123@45@g",
        database="Veg",
        cursorclass=pymysql.cursors.DictCursor     )
    print("Okay")
# finally: connection.close()
except: print("error")

config = {
    'name': 'Jackyficj_bot',
    'token': '5629735612:AAGM5LsvmjVBhKPfedmYBJtUW5SN0fIm-jg'
}
with connection.cursor() as cursor:
    auth_verfy = False
    sanktum = telebot.TeleBot(config['token'])
    # @sanktum.message_handler(content_types= ['text'])
    @sanktum.message_handler(commands= ['start'])
    def start(message):
        keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if not auth_verfy:
            button1 = types.KeyboardButton('log')
            keybord.add(button1)
            sanktum.send_message(message.chat.id, '_', reply_markup=keybord)
        else:
            button2 = types.KeyboardButton('add')
            button3 = types.KeyboardButton('show')
            button4 = types.KeyboardButton('showid')
            button5 = types.KeyboardButton('tfilter')
            button6 = types.KeyboardButton('delete')
            keybord.add(button2, button3, button4, button5, button6)
            sanktum.send_message(message.chat.id, 'Menu: ', reply_markup=keybord)
    @sanktum.message_handler(content_types=['text'])
    def get_text(message):
        if message.text == "log":
            if not auth_verfy:
                s = sanktum.send_message(message.chat.id, "Enter login and password ! ")
                sanktum.register_next_step_handler(s, autherithation)
            else:
                sanktum.send_message(message.chat.id, "You in! ")
        elif auth_verfy:
            if message.text == "add":
                s = sanktum.send_message(message.chat.id,"Enter Name, Type, Color, Caloric, Sklist, Money! ")
                sanktum.register_next_step_handler(s, add)
            elif message.text == "show":
                s = sanktum.send_message(message.chat.id, "Enter anything! ")
                sanktum.register_next_step_handler(s, show)
            elif message.text == "tfilter":
                s = sanktum.send_message(message.chat.id,"Enter param and product! ")
                sanktum.register_next_step_handler(s, tfilter)
            elif message.text == "showid":
                s = sanktum.send_message(message.chat.id,"Enter anything! ")
                sanktum.register_next_step_handler(s, showid)
            elif message.text == "delete":
                s = sanktum.send_message(message.chat.id, "Enter id! ")
                sanktum.register_next_step_handler(s, delete)
            elif message.text == "exit":
                return start(message)
        elif message.text == "/regist":
            if not auth_verfy:
                s = sanktum.send_message(message.chat.id,"Enter login and password for registration with wipe! ")
                sanktum.register_next_step_handler(s, auther_create)
            else:
                sanktum.send_message(message.chat.id, "You in! ")
        else:
            sanktum.send_message(message.chat.id, "You don't do autherithation or registration ! ")
            start(message)
    def auther_create(message):
        t1 = message.text.split()
        message.log = t1[0]
        message.passwd = t1[1]
        cursor.execute(f"INSERT INTO `Auth` (Login,Passwd) VALUES ('{message.log}','{message.passwd}')")
        connection.commit()
        sanktum.send_message(message.chat.id, "Done!")
    def auther_try(message):
        s = sanktum.send_message(message.chat.id, "Enter login and password! ")
        sanktum.register_next_step_handler(s, autherithation)
    def autherithation(message):
            try:
                t = message.text.split()
            except: sanktum.send_message(message.chat.id, "Wrong type! ")
            else:
                message.log = t[0]
                message.passwd = t[1]
                message.select_all = f"SELECT Login,Passwd FROM `Auth` where Login = '{message.log}';"
                cursor.execute(message.select_all)
                message.result = cursor.fetchall()
                print(message.result)
                try:
                    if message.result[0].get('Login') == message.log and message.result[0].get('Passwd') == message.passwd:
                        global auth_verfy
                        auth_verfy = True
                        sanktum.send_message(message.chat.id, "You logged in!")
                        return start(message)
                    else:
                        sanktum.send_message(message.chat.id, "Bad password try again!")
                        return auther_try(message)
                except:
                    sanktum.send_message(message.chat.id, "This account not exist in Base!")
                    return sanktum.send_message(message.chat.id, "/regist")

    def add(message):
        t = message.text.split()
        cursor.execute(f"INSERT INTO `Veg_fruit` (Name, Type, Color, Caloric, Sklist, Money) VALUES ('{t[0]}','{t[1]}','{t[2]}','{t[3]}','{t[4]}','{t[5]}')")
        connection.commit()
        sanktum.send_message(message.chat.id,"Done!")
    def show(message):
        cursor.execute(
            f"SELECT * from `Veg_fruit`")
        result = cursor.fetchall()
        sanktum.send_message(message.chat.id, "\n".join(
            [
                f"Name - {row.get('Name')}, Type - {row.get('Type')}, Color - {row.get('Color')}, Caloric - {row.get('Caloric')}, Sklist - {row.get('Sklist')}, Money - {row.get('Money')} "
                for row in result]))
    def showid(message):
        cursor.execute(
            f"SELECT * from `Veg_fruit`")
        result = cursor.fetchall()
        sanktum.send_message(message.chat.id, "\n".join(
            [
                f"Id: {row.get('id')}, Name - {row.get('Name')} "
                for row in result]))
    def delete(message):
        cursor.execute(f"DELETE FROM `Veg_fruit` WHERE id = {int(message.text)};")
        connection.commit()
        sanktum.send_message(message.chat.id, "Done!")
    def tfilter(message):
        t = message.text.split()
        add1 = t[0]
        add2 = t[1]
        if add1 == 'Name' or add1 == 'Type' or add1 == 'Color':
            cursor.execute(
                f"SELECT * FROM `Veg_fruit` where {add1} = '{add2}'")
            result = cursor.fetchall()
            sanktum.send_message(message.chat.id, "\n".join(
                [
                    f"Name - {row.get('Name')}, Type - {row.get('Type')}, Color - {row.get('Color')} "
                for row in result]))
        elif add1 == 'Caloric' or add1 == 'Money':
            cursor.execute(
                f"SELECT * FROM `Veg_fruit` where {add1} <= '{add2}'")
            result = cursor.fetchall()
            sanktum.send_message(message.chat.id, "\n".join(
                [
                    f"Name - {row.get('Name')}, Caloric - {row.get('Caloric')}, Money - {row.get('Money')} "
                    for row in result]))
        elif add1 == 'Sklist':
            cursor.execute(
                f"select * from Veg_fruit where (select locate('{add2}', Sklist))")
            result = cursor.fetchall()
            sanktum.send_message(message.chat.id, "\n".join(
                [
                    f"Name - {row.get('Name')}, Sklist - {row.get('Sklist')}, Money - {row.get('Money')} "
                    for row in result]))
    sanktum.polling(none_stop=True, interval=0)