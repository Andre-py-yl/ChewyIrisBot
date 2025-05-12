import random
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "7586593962:AAHEFAbAmuTQ-KD2RAzRPHAX2MpaN3GDPmE"

FACTS = [
    "В космосе есть облако спирта размером с 1000 солнечных систем.",
    "Муравьи могут поднимать вес, превышающий их собственный в 50 раз!",
    "Тело человека состоит из 37 триллионов клеток.",
]

HOROSCOPE = [
    "Сегодня твой день! Время действовать!",
    "Будь внимателен – важные перемены уже близко.",
    "Отдохни и наслаждайся моментом.",
]

JOKES = [
    "Программист пошёл в бар, заказал '127.0.0.1'.",
    "Баги? Нет, это скрытые функции!",
    "Почему разработчики любят кофе? Потому что он компилируется в энергию!",
]

QUOTES = [
    "Будь изменением, которое ты хочешь видеть в мире. – Ганди",
    "Не бойся идти медленно, бойся стоять на месте. – Китайская мудрость",
    "Начни делать – и силы появятся. – Гёте",
]

NAMES = ["Артур", "Михаил", "София", "Екатерина", "Александр", "Дарья"]

REMINDERS = {}


async def start(update: Update, context):
    """Приветственное сообщение."""
    await update.message.reply_text("Привет! Я твой многофункциональный бот!")


async def fact(update: Update, context):
    """Отправляет случайный интересный факт."""
    await update.message.reply_text(random.choice(FACTS))


async def horoscope(update: Update, context):
    """Отправляет случайный шуточный гороскоп."""
    await update.message.reply_text(random.choice(HOROSCOPE))


async def joke(update: Update, context):
    """Отправляет случайный анекдот."""
    await update.message.reply_text(random.choice(JOKES))


async def quote(update: Update, context):
    """Отправляет мотивирующую цитату."""
    await update.message.reply_text(random.choice(QUOTES))


async def random_name(update: Update, context):
    """Генерирует случайное имя."""
    await update.message.reply_text(f"Твоё случайное имя: {random.choice(NAMES)}")


async def word_count(update: Update, context):
    """Подсчитывает количество слов в переданном тексте."""
    text = " ".join(context.args)
    count = len(text.split())
    await update.message.reply_text(f"Количество слов в тексте: {count}")


async def math_problem(update: Update, context):
    """Решает простое математическое выражение."""
    try:
        expression = " ".join(context.args)
        result = eval(expression)
        await update.message.reply_text(f"Решение: {result}")
    except Exception:
        await update.message.reply_text("Ошибка в вычислении!")


async def generate_password(update: Update, context):
    """Генерирует случайный пароль."""
    password = ''.join(random.choices(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=12))
    await update.message.reply_text(f"Случайный пароль: {password}")


async def convert_units(update: Update, context):
    """Конвертирует единицы измерения (см ⇄ м)."""
    try:
        value = float(context.args[0])
        unit = context.args[1].lower()
        if unit == "см":
            result = value / 100
            await update.message.reply_text(f"{value} см = {result} м")
        elif unit == "м":
            result = value * 100
            await update.message.reply_text(f"{value} м = {result} см")
        else:
            await update.message.reply_text("Используйте 'см' или 'м'.")
    except ValueError:
        await update.message.reply_text("Ошибка в конвертации!")


async def set_reminder(update: Update, context):
    """Устанавливает напоминание через указанное количество секунд."""
    try:
        time_sec = int(context.args[0])
        text = " ".join(context.args[1:])
        await update.message.reply_text(f"Напоминание установлено на {time_sec} секунд.")
        time.sleep(time_sec)
        await update.message.reply_text(f"Напоминание: {text}")
    except ValueError:
        await update.message.reply_text("Ошибка в установке напоминания!")


async def ascii_art(update: Update, context):
    """Отправляет случайный ASCII-арт."""
    art = [
        "(\\_/)\n(='.'=)\n(\")_(\")  - Кролик приветствует тебя!",
        "░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░\n░░░░░░░░░░░░█░░░█░░░█░░░░░░░░\n🐱 Котик смотрит на тебя!"
    ]
    await update.message.reply_text(random.choice(art))


def main():
    """Запуск бота."""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fact", fact))
    app.add_handler(CommandHandler("horoscope", horoscope))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("name", random_name))
    app.add_handler(CommandHandler("wordcount", word_count))
    app.add_handler(CommandHandler("math", math_problem))
    app.add_handler(CommandHandler("password", generate_password))
    app.add_handler(CommandHandler("convert", convert_units))
    app.add_handler(CommandHandler("reminder", set_reminder))
    app.add_handler(CommandHandler("ascii", ascii_art))

    print("Бот запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()
