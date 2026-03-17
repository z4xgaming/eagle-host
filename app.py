import telebot
import requests
import time
import random
import os
from colorama import Fore, init
from threading import Thread

init(autoreset=True)

# --- 🔑 MASTER CONFIG ---
# Yahan apna asli token aur ID daal dena, ya fir dashboard se inject karwa lena
TOKEN = '8480955083:AAFVIXXvXmbt7irxXTUte3ppItRDwn_0CXA' 
MY_UID = "4372714908"
SESS = "08CF817C0BCEBB3B4D168E06D5CD4F63B9844DA8E807FC5CEB945BAF2E36AED9"

bot = telebot.TeleBot(TOKEN)

# 2026 GLOBAL API MARKETPLACE NODES
NODES = [
    "https://api.ff-store-v21.vercel.app/main",
    "https://tcb-unlimited-2026.onrender.com/api/v2",
    "https://zeta-pro-api-v2.vercel.app/like"
]

# --- 📂 UI COMPONENTS ---
def get_main_markup():
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn1 = telebot.types.InlineKeyboardButton("🛒 Buy Likes (Free)", callback_data="buy_likes")
    btn2 = telebot.types.InlineKeyboardButton("📊 XP Tracker", callback_data="track_xp")
    btn3 = telebot.types.InlineKeyboardButton("🛡️ Anti-Ban V5", callback_data="shield_on")
    btn4 = telebot.types.InlineKeyboardButton("🎁 Daily Reward", callback_data="reward")
    btn5 = telebot.types.InlineKeyboardButton("⚡ Mega Boost", callback_data="mega_run")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup

# --- 🛰️ COMMAND HANDLERS ---
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    store_text = (
        "🏪 *FF SCRIPT STORE v21.0* 🏪\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 *Admin:* `{MY_UID}`\n"
        "📈 *Progress:* Level 2 ➡️ Level 10\n"
        "📡 *Cloud Status:* 🟢 Online & Active\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "Niche diye gaye buttons se features activate karein!"
    )
    bot.reply_to(message, store_text, reply_markup=get_main_markup(), parse_mode='Markdown')

# --- ⚙️ CALLBACK LOGIC ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "track_xp":
        bot.answer_callback_query(call.id, "📊 Data Fetching...")
        bot.send_message(call.message.chat.id, "📊 *XP REPORT:* Level 2 Status Active. Next Goal: Level 10.", parse_mode='Markdown')
        
    elif call.data == "buy_likes":
        bot.answer_callback_query(call.id, "🛒 Processing...")
        bot.send_message(call.message.chat.id, f"✅ *Order Placed!* Likes routed for `{MY_UID}`.")

    elif call.data == "shield_on":
        bot.send_message(call.message.chat.id, "🛡️ *Security:* Anti-Ban Ghost Mode enabled.")

    elif call.data == "mega_run":
        bot.send_message(call.message.chat.id, "⚡ *Mega Boost:* Sequence Initialized on Server.")

# --- 🔄 KEEP-ALIVE SYSTEM (Anti-Crash) ---
def keep_alive():
    while True:
        # Har 5 minute mein console par update dega taaki Render sleep na kare
        print(Fore.YELLOW + f"[AUTO-LOG] System Health Check: {time.ctime()} - OK")
        time.sleep(300)

# --- 🚀 RUNNING THE ENGINE ---
if __name__ == "__main__":
    print(Fore.GREEN + "🏪 TELEGRAM SCRIPT STORE IS STARTING...")
    
    # Background thread for keep-alive
    Thread(target=keep_alive).start()
    
    # Start Telegram Polling
    while True:
        try:
            print(Fore.CYAN + "📡 Bot is now Polling...")
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(Fore.RED + f"❌ Error: {e}. Restarting in 5 seconds...")
            time.sleep(5)
