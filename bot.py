from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
from datetime import time

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    chat_id = update.effective_chat.id

    # 👉 завжди показує chat_id (щоб ти його побачила)
    await update.message.reply_text(f"Chat ID: {chat_id}")

    # 👉 реакція на "норм"
    if "норм" in text:
        await update.message.reply_text("Норм")

async def morning_message(context: ContextTypes.DEFAULT_TYPE):
    # поки що просто тест (без chat_id)
    # щоб не ламалось — пише в консоль
    print("Morning job works")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
