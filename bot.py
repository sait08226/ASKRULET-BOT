from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import sqlite3  # SQLite3 doğru yazımı

def get_db():
    conn = sqlite3.connect('askcoin.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users 
                    (user_id INTEGER PRIMARY KEY, coins INTEGER DEFAULT 100)''')  # INTEGER doğru yazımı
    return conn

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id  # .id eksikti
    conn = get_db()
    conn.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))  # Virgül ve parametre düzeltildi
    conn.commit()  # com.email() değil!
    conn.close()
    update.message.reply_text("🪙 Hoş geldin! 100 AskCoin başlangıç bonusun hazır.")  # Türkçe karakter düzeltildi

def main():
    updater = Updater("7559016549:AAFxyMljTaWW6V7sGWOFAGCWhe2aZXVrTC0", use_context=True)  # Tokeni buraya yapıştır
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))  # add_bandler değil!
    updater.start_polling()  # start_pulling değil!
    updater.idle()

if __name__ == '__main__':
    main()
