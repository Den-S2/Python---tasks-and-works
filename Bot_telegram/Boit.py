import telebot
import os.path
config = {
    'name': 'Jackyficj_bot',
    'token': '5629735612:AAGM5LsvmjVBhKPfedmYBJtUW5SN0fIm-jg'
}

sanktum = telebot.TeleBot(config['token'])

# @sanktum.message_handler(content_types= ['text'])
@sanktum.message_handler(commands= ['calc', 'cast', 'happ', 'stat'])
def get_text(message):
    if message.text == "Hello":
        sanktum.send_message(message.chat.id, "hello user!")
    elif message.text == "Where my money?":
        sanktum.send_message(message.chat.id, "Your money? It's our!")
    elif message.text == "/calc":
        s = sanktum.send_message(message.chat.id,"Enter action! ")
        sanktum.register_next_step_handler(s, cal)
    elif message.text == "/cast":
        s = sanktum.send_message(message.chat.id,"Enter words! ")
        sanktum.register_next_step_handler(s, show)
    elif message.text == "/happ":
        s = sanktum.send_message(message.chat.id,"Enter num! ")
        sanktum.register_next_step_handler(s, happy_tick)
    elif message.text == "/stat":
        s = sanktum.send_message(message.chat.id,"Enter text! ")
        sanktum.register_next_step_handler(s, statistic)
def cal(message):
    sym = message.text[2:3]
    if '+' in message.text:
        number1, number2 = message.text.split('+')
        sanktum.send_message(message.chat.id, f"{number1} + {number2} = {int(number1) + int(number2)}")
    elif '-' in message.text:
        number1, number2 = message.text.split('-')
        sanktum.send_message(message.chat.id, f"{number1} - {number2} = {int(number1) - int(number2)}")
    elif '*' in message.text:
        number1, number2 = message.text.split('*')
        sanktum.send_message(message.chat.id, f"{number1} * {number2} = {int(number1) * int(number2)}")
    elif '/' in message.text:
        number1, number2 = message.text.split('/')
        sanktum.send_message(message.chat.id, f"{number1} / {number2} = {int(number1) / int(number2)}")
def show(message):
    count1 = 0
    for i in message.text.split():
        count1 += 1
    sanktum.send_message(message.chat.id, f"Count of symbols {len(message.text)} and words {count1}")
def happy_tick(message):
    a = [int(i) for i in message.text]
    b = len(message.text)/2
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