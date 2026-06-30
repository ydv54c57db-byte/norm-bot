from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
import re
import random
from datetime import time
from zoneinfo import ZoneInfo

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    bot_username = "@norm_again_bot"

    # згадка бота
    mentioned = bot_username in text

    # відповідь на бота
    replied_to_bot = (
        update.message.reply_to_message
        and update.message.reply_to_message.from_user
        and update.message.reply_to_message.from_user.id == context.bot.id
    )

    if mentioned or replied_to_bot:
        answers = [
            "Шо?",
            "👀",
            "Я тут",
            "Кажи",
            "Так?",
            "Хто кликав?",
            "Слухаю",
            "Мене?",
            "Норм?",
            "На зв'язку",
            "Норм чи не норм?",
            "Га?"
        ]

        await update.message.reply_text(random.choice(answers))
        return

    # Токсичні/образливі слова
    toxic_words = [
        "підорас", "пидорас", "бити дітей", "російський реп",
        "геї підораси", "геи пидарасы", "пирадас", "пидарасы",
        "педик", "пєдік", "педік", "гей як образа",
        "гомофоб", "гомофобія", "гомофобия", "підар"
    ]

    if any(word in text for word in toxic_words):
        await update.message.reply_text("Не норм.")
        return

    # пепсі погано
    pepsi_bad = (
        "пепсі" in text or "pepsi" in text
    ) and any(word in text for word in [
        "краще", "краща", "топ", "смачніша", "ніж кола", "за колу"
    ])

    if pepsi_bad:
        await update.message.reply_text("Не норм.")
        return

    # кола вибір
    has_cola = (
        "кол" in text or
        "кока" in text or
        "cola" in text or
        "coca" in text
    )

    asks_choice = any(word in text for word in [
        "яку", "яка", "який", "які",
        "купити", "взяти", "обрати", "вибрати",
        "порадь", "порадьте", "рекомендуєш",
        "краща", "найкраща", "топ"
    ])

    if has_cola and asks_choice:
        await update.message.reply_text("Кокакола нормаааль")
        return

    # норм
    if re.search(r"(?<!\w)норм(?!\w)", text):
        if random.randint(1, 10) != 1:
            await update.message.reply_text("Норм")
        else:
            rare_answers = [
                "Нормаль",
                "Не норм... А, ні\nНорм",
                "Та норм норм",
                "Абсолютно норм",
                "Сертифіковано як норм ✅",
                "Точно норм",
                "Норм++",
                "Норм, 10/10",
                "Норм, зуб даю (його ⬆️)",
                "Норм\nБез питань",
                "Мега норм",
                "Перевірила\nНорм",
                "На 100% норм",
                "Ну і що ти хочеш почути? Норм."
            ]

            await update.message.reply_text(random.choice(rare_answers))
            return
    
# повідомлення о 7:00
async def morning_message(context: ContextTypes.DEFAULT_TYPE):
    chat_id = -5458919378
    await context.bot.send_message(
        chat_id=chat_id,
        text="Хааай норміси👋\nНай ваш день буде норм"
    )

app = Application.builder().token(TOKEN).build()

# звичайні повідомлення
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

# планування
app.job_queue.run_daily(
    morning_message,
    time=time(hour=7, minute=0, tzinfo=ZoneInfo("Europe/Kyiv"))
)

app.run_polling()
