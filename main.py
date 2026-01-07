from decouple import config
import telebot
from telebot import types

bot_token = config("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)

names = {
    "Jibek": "01.01.1999",
    "Atai": "02.02.2001",
    "Erbol": "03.03.2003"
}
@bot.message_handler(commands=["start","привет"])
def start(message):
    send_text = f"Привет {message.chat.first_name}\n" \
                f"Я бот который помогает найти дату " \
                f"рождения твоих коллег\n" \
                f"Выбери пожалуйста имя сотрудника!"
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    murkup.add(types.KeyboardButton("Jibek"))
    murkup.add(types.KeyboardButton("Atai"))
    murkup.add(types.KeyboardButton("Erbol"))
    bot.reply_to(message, send_text, reply_markup=murkup)

@bot.message_handler(func=lambda message : True)
def get_text(message):
    name = message.text
    birth_date = names.get(name)
    response_text = "Нечего не найдено!"
    if birth_date:
        response_text = f"Коллега по имени {name}\n" \
                        f"родилась {birth_date}"
    keyboard = types.InlineKeyboardMarkup()
    button_save = types.InlineKeyboardButton(text="Фамилия",
                                                     callback_data='last_name')
    button_change = types.InlineKeyboardButton(text="Департамент",
                                                       callback_data='department')
    keyboard.add(button_save, button_change)
    bot.reply_to(message, response_text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'last_name')
def get_last_name(call):
    print(call)
    message = call.message
    # print(message)
    bot.send_message(call.message.chat.id, "Фамилия")

@bot.callback_query_handler(func=lambda call: call.data == 'department',
                            url='https://youtu.be/Udn3hq5lsow?si=ZKLqubqn_mg4Jjts')
def get_last_name(call):
    print(call)
    message = call.message
    # print(message)
    bot.send_message(call.message.chat.id, "Департамент")

bot.polling()
names = {
    "Jibek": {
        "date": "01.01.1999",
        "last_name": "Джолдошбекова",
        "department": "IT"
    } ,
    "Atai": {
        "date": "02.02.2001",
        "last_name": "Самудинов",
        "department": "DevOps"
    } ,
    "Erbol": {
        "date": "03.03.2003",
        "last_name": "Эгембердиев",
        "department": "Project Management"
    }
}