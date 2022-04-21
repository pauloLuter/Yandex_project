import logging
from datetime import datetime
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5324119937:AAE2Oheh3gw7v-Brh64iFuWGkhPg4o6xPiU'


def echo(update, context):
    update.message.reply_text(write(update, context))


def read(update, context):
    if 'биология' in context:
        a = datetime.today().date().strftime("%d/%m/%Y")
        update.message.reply_text(f'до ЕГЭ по биологии осталось {a} дней')
    # if 'химия' in context:
    #     update.message.reply_text('до ЕГЭ по химии осталось 40 дней')
    # if 'математика' in context:
    #     update.message.reply_text('до ЕГЭ по осталось 40 дней')
    # if 'русский' in context:
    #     update.message.reply_text('до ЕГЭ по биологии осталось 40 дней')
    # if 'литература' in context:
    #     update.message.reply_text('до ЕГЭ по биологии осталось 40 дней')
    # if 'физика' in context:
    #     update.message.reply_text('до ЕГЭ по биологии осталось 40 дней')
    # if 'информатика' in context:
    #     update.message.reply_text('до ЕГЭ по биологии осталось 40 дней')


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
