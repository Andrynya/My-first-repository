import telebot
import threading
import random
from telebot import types

bot = telebot.TeleBot("введите токен")

reminder_times = []

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    item_start = types.KeyboardButton('/start')
    item_fact = types.KeyboardButton('/fact')
    markup.row(item_start, item_fact)
    bot.reply_to(message, "Привет, я чат бот, который будет напоминать тебе выпить витаминки.", reply_markup=markup)
    reminder_threads = threading.Thread(target=set_reminder_time, args=(message,))
    reminder_threads.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    facts = ["Агата Кристи работала в аптеке. Во время Первой мировой войны знаменитая писательница была медсестрой, а "
             "затем трудилась в аптеке.",
             "В 1240 году император Священной Римской империи Фридрих II издал указ, который "
             "разделил обязанности врачей и фармацевтов.",
             "Один из символов фармации — чаша со змеёй, которую называют "
             "сосудом Гигеи. Использовать его начали по меньшей мере с 1796 года."]
    random_fact = random.choice(facts)
    bot.reply_to(message, f"Факт о фармацевтике: {random_fact}")

@bot.message_handler(commands=['help'])
def help_message(message):
    commands = [
        '/start - Начать взаимодействие с ботом.',
        '/fact - Получить интересный факт о фармацевтике.',
        '/help - Показать доступные команды бота.',
        '/napominanya - Установить время для напоминаний.',
        '/sport - Будь в курсе спортивных новостей'
    ]
    bot.reply_to(message, "Доступные команды:\n" + "\n".join(commands))

@bot.message_handler(commands=['napominanya'])
def set_reminder_time(message):
    bot.reply_to(message, "Введите время в формате HH:MM для установки напоминаний. Для завершения ввода времен используйте команду /done.")

    @bot.message_handler(func=lambda msg: msg.text and len(msg.text) == 5 and msg.text.count(':') == 1 and all(i.isdigit() for i in msg.text.replace(':', '')) or msg.text == '/done')
    def process_reminder_time(message):
        if message.text == '/done':
            bot.reply_to(message, f"Установлены следующие времена для напоминаний: {reminder_times}")
            # Добавьте код здесь для использования списка reminder_times в функции send_reminders()
            return

        reminder_time = message.text
        reminder_times.append(reminder_time)
        bot.reply_to(message, f"Добавлено время для напоминаний: {reminder_time}")

@bot.message_handler(commands=['sport'])
def sport_message(message):
    bot.reply_to(message, "Хочешь быть в курсе спортивных новостей? Переходи по ссылке: https://rsport.ria.ru/")

bot.polling(non_stop=True)