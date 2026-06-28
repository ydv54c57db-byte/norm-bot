from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
from datetime import time

TOKEN = os.getenv("TOKEN")

#CHAT_ID = -1001234567890


# реакція на "норм"
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "норм" in text:
        await update.message.reply_text("Норм")

#if "id" in text or "chat" in text:
       # await update.message.reply_text(f"Chat ID: {chat_id}")

# повідомлення щоранку
async def morning_message(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="Най ваш день буде норм"
    )


# запуск щоденної задачі
#async def start_jobs(app):
   # app.job_queue.run_daily(
      #  morning_message,
       # time=time(hour=4, minute=0)  # 7:00 по Києву (UTC+3 → 04:00 UTC)
  #  )


# 🚀 запуск бота
app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.post_init = start_jobs

app.run_polling()
