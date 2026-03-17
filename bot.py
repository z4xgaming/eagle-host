import telebot
from api_handler import inject_to_game
from utils import start_safety_timer

# --- [ TOKEN LOADER ] ---
# Ab yahan direct token nahi hai, security ke liye file se read karega
try:
    with open("token.txt", "r") as f:
        API_TOKEN = f.read().strip()
except FileNotFoundError:
    print("❌ Error: 'token.txt' file nahi mili!")
    exit()

bot = telebot.TeleBot(API_TOKEN)

# Safety timer start karo (2 Hours)
start_safety_timer()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 **FLASH SYSTEM ACTIVE**\nRegion: IND | Mode: PC\nUse `/add [UID]`")

@bot.message_handler(commands=['add'])
def handle_add(message):
    try:
        uid = message.text.split()[1] if len(message.text.split()) > 1 else None
        if uid:
            status = inject_to_game(uid, "ADD_FRIEND")
            bot.reply_to(message, f"📡 **Status:** {status}\nTarget: `{uid}`")
        else:
            bot.reply_to(message, "❌ UID missing!")
    except Exception as e:
        bot.reply_to(message, "⚠️ Error: `/add [UID]` format use karein.")

bot.infinity_polling()
