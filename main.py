import logging
import pymorphy2
from datetime import datetime
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5324119937:AAE2Oheh3gw7v-Brh64iFuWGkhPg4o6xPiU'

d = {'информатика': '20.06.2022', 'биология': '14.06.2022', 'география': '26.05.2022', 'литература': '26.05.2022',
     'химия': '26.05.2022', 'русский': '30.05.2022', 'математика': '03.06.2022', 'история': '06.06.2022', 'физика': '06.06.2022',
     'обществознание': '09.06.2022'}
morph = pymorphy2.MorphAnalyzer()


def echo(update, context):
    update.message.reply_text(write(update, context))


def read(update, context):
    context = context.lower()
    context = morph.parse(context)[0]
    for i in d.keys():
        if i in context.inflect({'nomn'}).word:
            a = datetime.today().date().strftime("%d.%m.%Y")
            a = datetime.strptime(a, "%d.%m.%Y")
            b = datetime.strptime(d[i], "%d.%m.%Y")
            i = morph.parse(i)[0]
            sub = i.inflect({'datv'}).word
            day = morph.parse('день')[0]
            update.message.reply_text(f'до ЕГЭ по {sub} осталось {(b - a).days} {day.make_agree_with_number((b - a).days).word}')


def write(update, context):
    context = update.message.text
    read(update, context)

#
#
# def wrong(update, context):
#     update.message.reply_text('нет, не так')
#     update.message.reply_text(a[k + 1])
#     write(update, context, k)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler('read', read))
    # dp.add_handler(CommandHandler('write', write))
    # dp.add_handler(CommandHandler('wrong', wrong))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
