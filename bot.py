from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import time

TOKEN = os.getenv("TOKEN")

CHAT_ID = -5458919378


# 💬 реакція на "норм"
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "норм" in text:
        await update.message.reply_text("Норм")


# 🌅 ранкове повідомлення
async def morning_message(app):
    await app.bot.send_message(
        chat_id=CHAT_ID,
        text="Най ваш день буде норм"
    )


# ⏰ планувальник
scheduler = AsyncIOScheduler()

async def post_init(app: Application):
    # 7:00 по UTC (Київ = 04:00 UTC)
    scheduler.add_job(
        lambda: app.create_task(morning_message(app)),
        "cron",
        hour=4,
        minute=0
    )
    scheduler.start()


# 🚀 запуск
app = Application.builder().token(TOKEN).post_init(post_init).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
