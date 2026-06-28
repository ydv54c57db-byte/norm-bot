from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
from datetime import time

TOKEN = os.getenv("TOKEN")

CHAT_ID = -5458919378


# реакція на повідомлення
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "норм" in text:
        await update.message.reply_text("Норм")


# ранкове повідомлення
async def morning_message(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="Най ваш день буде норм"
    )


# запуск о 7:00 (Київ = 04:00 UTC)
async def start_jobs(app):
    app.job_queue.run_daily(
        morning_message,
        time=time(hour=4, minute=0)
    )


# 🚀 запуск бота
app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.post_init = start_jobs

app.run_polling()
