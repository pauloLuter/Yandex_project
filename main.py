import logging
import pymorphy2
from datetime import datetime
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5324119937:AAE2Oheh3gw7v-Brh64iFuWGkhPg4o6xPiU'

d = {'информатика': '20.06.2022', 'биология': '14.06.2022', 'география': '26.05.2022', 'литература': '26.05.2022',
     'химия': '26.05.2022', 'русский': '30.05.2022', 'математика': '03.06.2022', 'история': '06.06.2022', 'физика': '06.06.2022',
     'обществознание': '09.06.2022'}

photo = ['https://jokesland.net.ru/pc/motivatory_20/1.jpg',
         'https://kaifolog.ru/uploads/posts/2010-06/1275372822_004.jpg',
         'https://i.pinimg.com/564x/bb/20/58/bb2058edd627108b2855c72d655b5130.jpg',
         'https://cs10.pikabu.ru/images/big_size_comm/2020-11_5/1606069357178316867.png',]

morph = pymorphy2.MorphAnalyzer()


def echo(update, context):
    update.message.reply_text(start(update, context))


def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Хочу мотивационную картинку", callback_data='1')],
        [InlineKeyboardButton("Посоветуй сайты для подготовки", callback_data='2')],
        [InlineKeyboardButton("Сколько дней осталось до моего экзамена", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите один из вариантов:', reply_markup=reply_markup)

    write(update, context)


def read(update, context):
    context = context.lower()
    context = morph.parse(context)[0]
    k = 0
    for i in d.keys():
        if i in context.inflect({'nomn'}).word:
            k = 1
            a = datetime.today().date().strftime("%d.%m.%Y")
            a = datetime.strptime(a, "%d.%m.%Y")
            b = datetime.strptime(d[i], "%d.%m.%Y")
            i = morph.parse(i)[0]
            sub = i.inflect({'datv'}).word
            day = morph.parse('день')[0]
            update.message.reply_text(f'до ЕГЭ по {sub} осталось {(b - a).days} {day.make_agree_with_number((b - a).days).word}')
    if k == 0:
        update.message.reply_text('Пока что я не умею понимать все сообщения :(')


def write(update, context):
    context = update.message.text
    read(update, context)


def button(update, context):
    query = update.callback_query
    variant = query.data
    query.answer()
    if variant == '1':
        query.edit_message_text(text=f"{photo[random.randint(0, 3)]}")
    elif variant == '2':
        query.edit_message_text(text=f"На этом сайте много материалов для подготовки: {'https://ege.sdamgia.ru/'}")
    else:
        query.edit_message_text(text="Какой экзамен ты будешь сдавать?")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler('read', read))
    dp.add_handler(CommandHandler('write', write))
    dp.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
