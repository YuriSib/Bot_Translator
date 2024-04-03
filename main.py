import telebot
from googletrans import Translator

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)
group_chat_id = -1002105457435


def text_translator(text, src='ru', dest='tr'):
    try:
        ru_translator = Translator()
        translation = ru_translator.translate(text=text, src=src, dest=dest)

        return translation.text
    except Exception as ex:
        bot.send_message(-1002075374727, f'{ex}')
        return ex


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    print(message.chat.type)
    print(message.chat.id)
    if message.chat.id == -1002075374727:
        text_ru = message.text
        text_en = text_translator(text_ru)
        bot.send_message(-1002075374727, text_en)
        print(text_en)
        print(f"Message from {message.chat.title}: {message.text}")
    elif message.chat.id == group_chat_id:
        text_ru = message.text
        text_en = text_translator(text_ru)
        bot.send_message(group_chat_id, text_en)
        print(f"Message from {message.chat.title}: {message.text}")


bot.polling()


# def send_message():
#     bot.send_message(-1002075374727, f'Проверка')
#
#
# send_message()