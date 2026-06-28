from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = -5458919378


# 💬 реакція на "норм"
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "норм" in text:
        await update.message.reply_text("Норм")


# 🌅 ранкове повідомлення (через простий job)
async def morning_message(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="Най ваш день буде норм"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

# ⏰ правильно додаємо job queue
job_queue = app.job_queue
job_queue.run_daily(morning_message, time=7, 0)

app.run_polling()
