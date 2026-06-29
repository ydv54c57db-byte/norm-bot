from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
from datetime import time
from zoneinfo import ZoneInfo

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Чи є згадка про колу
    has_cola = (
        "кол" in text or
        "кока" in text or
        "coca" in text
    )

    # Чи людина просить порадити/обрати
    asks_choice = any(word in text for word in [
        "яку", "яка", "який",
        "купити", "взяти", "обрати",
        "порадь", "порадьте", "порадите",
        "рекомендуєш", "рекомендуєте",
        "краща", "найкраща", "найсмачніша",
        "топ"
    ])

    if any(c in text for c in cola_words) and any(w in text for w in choice_words):
        await update.message.reply_text("Кокакола нормаааль")
        return

    # Реакція на "норм"
    if "норм" in text:
        await update.message.reply_text("Норм")

# повідомлення о 7:00
async def morning_message(context: ContextTypes.DEFAULT_TYPE):
    chat_id = -5458919378
    await context.bot.send_message(
        chat_id=chat_id,
        text="Хааай норми\nНай ваш день буде норм"
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
