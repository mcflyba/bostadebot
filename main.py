from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.getenv("TOKEN")  # Pegará a variável do ambiente no Railway

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Bot rodando no Railway! 🚄")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    print("Bot iniciado...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
