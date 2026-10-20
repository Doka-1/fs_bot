import os
import telebot
from telebot import types

# Токен берётся из переменной окружения BOT_TOKEN
bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

# Главное меню (кнопки внизу экрана)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_requests = types.KeyboardButton('📋 Заявки')
    btn_tests = types.KeyboardButton('📝 Тесты')
    btn_checklists = types.KeyboardButton('☑️ Чек-листы')
    btn_acts_defect = types.KeyboardButton('📦 Акт и Брак / Услуги')
    markup.add(btn_requests, btn_tests, btn_checklists, btn_acts_defect)

    bot.send_message(
        message.chat.id,
        "Привет! Выберите нужный раздел из меню ниже:",
        reply_markup=markup
    )

# Раздел «Заявки»
@bot.message_handler(func=lambda message: message.text == '📋 Заявки')
def menu_requests(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('💻 IT: Оборудование, Доступы, Сеть', url='https://forms.yandex.ru/cloud/6a68680949af47002dbe1bf1'),
        types.InlineKeyboardButton('🌐 IT: Проблемы с сайтом', url='https://forms.yandex.ru/cloud/6a68672c1f1eb5003095dc86'),
        types.InlineKeyboardButton('💳 IT: Касса, CRM', url='https://forms.yandex.ru/cloud/6a5f67dcf47e73002f3136cf'),
        types.InlineKeyboardButton('👥 Заявка на подбор персонала', url='https://forms.yandex.ru/cloud/6a68952149af470bf0be1bdc'),
        types.InlineKeyboardButton('🔧 Заявка на ремонт', url='https://forms.yandex.ru/cloud/6a6886ca90290208587b1e9c'),
        types.InlineKeyboardButton('🔄 Возврат брака / списание', url='https://forms.yandex.ru/cloud/6a86e29c068ff00be8ae03f2')
    )
    bot.send_message(message.chat.id, "Выберите нужную заявку:", reply_markup=markup)

# Раздел «Тесты»
@bot.message_handler(func=lambda message: message.text == '📝 Тесты')
def menu_tests(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('Стажёр. Тест №1', url='https://forms.yandex.ru/cloud/6a6b41af6d2d73706946ba78'),
        types.InlineKeyboardButton('Стажёр. Тест №2', url='https://forms.yandex.ru/cloud/6a6b56059029025f607b1d64'),
        types.InlineKeyboardButton('Стажёр. Тест №3', url='https://forms.yandex.ru/cloud/6a6b5b644936395de0a47b93'),
        types.InlineKeyboardButton('Стажёр. Тест №4', url='https://forms.yandex.ru/cloud/6a7d9c281f1eb556b10deb6b'),
        types.InlineKeyboardButton('Стажёр. Тест №5', url='https://forms.yandex.ru/cloud/6a7db3ec9029025b3ad5cf6e'),
        types.InlineKeyboardButton('Стажёр. Тест №6', url='https://forms.yandex.ru/cloud/6a7dbbea9029025dc5d5ce5e')
    )
    bot.send_message(message.chat.id, "Выберите тест для прохождения:", reply_markup=markup)

# Раздел «Чек-листы»
@bot.message_handler(func=lambda message: message.text == '☑️ Чек-листы')
def menu_checklists(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('🔍 РЕВИЗОРРО', url='https://forms.yandex.ru/cloud/6a9037114936393d20aa619f'),
        types.InlineKeyboardButton('🚪 Чек-лист увольняющегося сотрудника', url='https://forms.yandex.ru/cloud/6a68a29790fa7b10613e5963')
    )
    bot.send_message(message.chat.id, "Выберите чек-лист:", reply_markup=markup)

# Раздел «Акт и Брак / Услуги»
@bot.message_handler(func=lambda message: message.text == '📦 Акт и Брак / Услуги')
def menu_acts(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('🛠 Брак. Услуги', url='https://forms.yandex.ru/cloud/6a86d3a895add50a21aa8a25'),
        types.InlineKeyboardButton('📋 Акт приемки товара', url='https://forms.yandex.ru/cloud/6a7dc61b90290260b8d5ce73')
    )
    bot.send_message(message.chat.id, "Выберите форму:", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
