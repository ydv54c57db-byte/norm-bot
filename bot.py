from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
from datetime import time

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "норм" in text:
        await update.message.reply_text("Норм")

# повідомлення о 7:00
async def morning_message(context: ContextTypes.DEFAULT_TYPE):
    chat_id = -5458919378
    await context.bot.send_message(
        chat_id=chat_id,
        text="Най ваш день буде норм"
    )

app = Application.builder().token(TOKEN).build()

# звичайні повідомлення
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

# планування
app.job_queue.run_daily(
    morning_message,
    time=time(hour=7, minute=8)
)

app.run_polling()
