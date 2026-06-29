from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
import re
from datetime import time
from zoneinfo import ZoneInfo

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Токсичні/образливі слова
    toxic_words = [
        "підорас", "пидорас", "бити дітей", "російський реп", "геї підораси", "геи пидарасы", "пирадас" , "пидарасы", "педик",
    "пєдік", "педік", "гей як образа",  "гомофоб", "гомофобія", "гомофобия", "підар"
    ]

    if any(word in text for word in toxic_words):
        await update.message.reply_text("Не норм.")
        return

    # негатив до коли
    pepsi_bad = (
        "пепсі" in text or "pepsi" in text
    ) and any(word in text for word in [
        "краще", "краща", "топ", "смачніша", "ніж кола", "за колу"
    ])

    if pepsi_bad:
        await update.message.reply_text("Не норм.")
        return

    # Кола + вибір
    has_cola = (
        "кол" in text or
        "кока" in text or
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

    if re.search(r"(?<!\w)норм(?!\w)", text):
        await update.message.reply_text("Норм")
    
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
