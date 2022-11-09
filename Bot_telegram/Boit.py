import telebot

config = {
    'name': 'Jackyficj_bot',
    'token': '5629735612:AAGM5LsvmjVBhKPfedmYBJtUW5SN0fIm-jg'
}

sanktum = telebot.TeleBot(config['token'])

@sanktum.message_handler(content_types= ['text'])
def get_text(message):
    if message.text == "Hello":
        sanktum.send_message(message.chat.id, "hello user!")
    if message.text == "Where my money?":
        sanktum.send_message(message.chat.id, "Your money? It's our!")
    if message.text == "Calcult":
        s = sanktum.send_message(message.chat.id,"Enter action! ")
        sanktum.register_next_step_handler(s, cal)
    if message.text == "Cast":
        s = sanktum.send_message(message.chat.id,"Enter words! ")
        sanktum.register_next_step_handler(s, show)
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
sanktum.polling(none_stop=True, interval=0)