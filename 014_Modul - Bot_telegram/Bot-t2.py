import telebot
import os.path
import pymysql
from telebot import types

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
            button2 = types.KeyboardButton('calc')
            button3 = types.KeyboardButton('cast')
            button4 = types.KeyboardButton('stat')
            button5 = types.KeyboardButton('happ')
            button6 = types.KeyboardButton('exit')
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
            if message.text == "Hello":
                 sanktum.send_message(message.chat.id, "hello user!")
            elif message.text == "Where my money?":
                sanktum.send_message(message.chat.id, "Your money? It's our!")
            elif message.text == "calc":
                s = sanktum.send_message(message.chat.id,"Enter action! ")
                sanktum.register_next_step_handler(s, cal)
            elif message.text == "cast":
                s = sanktum.send_message(message.chat.id,"Enter words! ")
                sanktum.register_next_step_handler(s, show)
            elif message.text == "happ":
                s = sanktum.send_message(message.chat.id,"Enter num! ")
                sanktum.register_next_step_handler(s, happy_tick)
            elif message.text == "stat":
                s = sanktum.send_message(message.chat.id,"Enter text! ")
                sanktum.register_next_step_handler(s, statistic)
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

    def cal(message):
        sym = message.text[2:3]

        if '+' in message.text:
            try:
                number1, number2 = message.text.split('+')
            except: sanktum.send_message(message.chat.id, "Wrong example!")
            else:
                sanktum.send_message(message.chat.id, f"{number1} + {number2} = {int(number1) + int(number2)}")
        elif '-' in message.text:
            try:
                number1, number2 = message.text.split('-')
            except: sanktum.send_message(message.chat.id, "Wrong example!")
            else:
                sanktum.send_message(message.chat.id, f"{number1} - {number2} = {int(number1) - int(number2)}")
        elif '*' in message.text:
            try:
                number1, number2 = message.text.split('*')
            except: sanktum.send_message(message.chat.id, "Wrong example!")
            else:
                sanktum.send_message(message.chat.id, f"{number1} * {number2} = {int(number1) * int(number2)}")
        elif '/' in message.text:
            try:
                number1, number2 = message.text.split('/')
            except: sanktum.send_message(message.chat.id, "Wrong example!")
            else:
                sanktum.send_message(message.chat.id, f"{number1} / {number2} = {int(number1) / int(number2)}")
    def show(message):
        count1 = 0
        for i in message.text.split():
            count1 += 1
        sanktum.send_message(message.chat.id, f"Count of symbols {len(message.text)} and words {count1}")
    def happy_tick(message):
        try:
            a = [int(i) for i in message.text]
            b = len(message.text)/2
        except: sanktum.send_message(message.chat.id, "Wrong example!")
        else:
            if sum(a[:int(b)]) == sum(a[int(b):]):
                sanktum.send_message(message.chat.id, f"Numb of {message.text} is lucky")
            else:
                sanktum.send_message(message.chat.id, f"Numb of {message.text} is unlucky")
    def statistic(message):
        count, count1, count2,count3,count4, count5, count6, count7 = 0,0,0,0,0,0,0,0
        a = ["a","e","i","o","q","u","y"]
        b = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","w","x","z"]
        c = [",", ":", ";", "@", "-", "(", ")", "%"]
        d = [".", "?", "!"]
        for i in message.text:
           if i in a:
               count += 1
           elif i in b:
               count2 += 1
           elif i.isdigit():
               count3 += 1
               if int(i) % 2 == 0:
                  count5 += 1
               else:
                   count6 += 1
           elif i in c:
               count4 += 1
           elif i in d:
               count7 += 1
        file = open(os.path.join("strt.txt"), "w")
        file.write(str(f"All symbols in file: {len(message.text)}")); file.write("\n")
        file.write(str(f"Light symbols: {count}"));file.write("\n")
        file.write(str(f"Hard symbols: {count2}")); file.write("\n")
        file.write(str(f"Numbers: {count3}")); file.write("\n")
        file.write(str(f"Extra symbols: {count4}")); file.write("\n")
        file.write(str(f"Odd numbers: {count5}")); file.write("\n")
        file.write(str(f"Elven numbers: {count6}")); file.write("\n")
        for i in message.text.split():
            count1 += 1
        file.write(str(f"Words in text: {count1}")); file.write("\n")
        file.write(str(f"Sentences: {count7}")); file.write("\n")
        file.close()
        file = open(os.path.join("strt.txt"), "r")
        sanktum.send_document(message.chat.id, file); file.close()
        file = open(os.path.join("strt.txt"), "r")
        br = file.read()
        print(br); file.close()

    sanktum.polling(none_stop=True, interval=0)