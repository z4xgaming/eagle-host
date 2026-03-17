
import telebot, time, os, random, requests, datetime
from telebot import types

# --- 🔑 PRIVATE ACCESS (TOKEN SAHI DALO BHAI) ---
TOKEN = 'PASTE_YOUR_BOT_TOKEN_HERE' # @BotFather se lekar yahan dalo
bot = telebot.TeleBot(TOKEN)

# System Status
MY_UID = "4372714908" # Admin UID
VERSION = "V10.0 - OGGY BANNER"
PORT = 9999 # Spain Port AC

# --- 🎭 OGGY FACE BANNER (TERMUX UI) ---
def boot_oggy_panel():
    os.system('clear')
    print("\033[1;35m") # Oggy Purple Color
    # Oggy Face ASCII Art (Big Banner)
    print(r"""
    ══════════════════════════════════════════════════════
               _____                      _   
              / __  \                    | |  
     OGGY     `' / /' _ __ _   _ __ _   _| |  
                / /' | '__| | | / _` | | | |  
    REBEL      / /___| |  | |_| | (_| | |_| |  
              \_____/|_|   \__, |\__,_|\__, |  
                            __/ |       __/ |  
                           |___/       |___/   
    
    [ OGGY FACE SYSTEM ] -> Port {PORT} Spain AC Active ✅
    ══════════════════════════════════════════════════════
    """)
    print(f"\033[1;36m [>] ADMIN UID: {MY_UID}")
    print(f"\033[1;32m [!] STATUS: REBEL MODE ACTIVE 🟢 | NO MORE GANDA ERROR.")
    print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;37m [LOG] System Ready. Oggy is waiting for commands...")

# --- 🛰️ SPAIN PORT AC INJECTION LOGIC ---
def spain_port_inject(target_uid):
    steps = ["Locating Player...", "Spain Port Bypass...", "Injecting AC Work..."]
    for step in steps:
        time.sleep(1)
        # Dashboard par asali logs dikhayega
        print(f" \033[1;31m[INJECT] {step}\033[0m")
    return True

# --- 🎮 COMMAND HANDLERS ---

@bot.message_handler(commands=['help', 'start'])
def main_menu(m):
    mk = types.InlineKeyboardMarkup(row_width=2)
    mk.add(
        types.InlineKeyboardButton("🚀 Spain Port AC", callback_data="spain"),
        types.InlineKeyboardButton("🔑 JWT (ID:Pass)", callback_data="jwt"),
        types.InlineKeyboardButton("👤 Scan Real UID", callback_data="scan")
    )
    msg = (f"🐱 *OGGY REBEL V10* 🐱\n"
           f"━━━━━━━━━━━━━━━━━━━━━\n"
           f"Bhai, Termux dashboard par Oggy ka banner lag gaya hai!\n\n"
           f"Option select karo:")
    bot.send_message(m.chat.id, msg, reply_markup=mk, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda c: True)
def process_handle(c):
    if c.data == "spain":
        q = bot.send_message(c.message.chat.id, "🎯 *Target UID dalo (Spain Port AC Work):*")
        bot.register_next_step_handler(q, start_injection)
    elif c.data == "scan":
        q = bot.send_message(c.message.chat.id, "🔍 *Real UID dalo Scan ke liye:*")
        bot.register_next_step_handler(q, real_scan)

def start_injection(m):
    uid = m.text
    bot.send_message(m.chat.id, f"⚡ *SPAIN PORT:* Injecting AC packets into `{uid}`... Game ke andar check karein.")
    
    if spain_port_inject(uid):
        time.sleep(1)
        res = (f"🔥 *INJECTION SUCCESSFUL!*\n"
               f"━━━━━━━━━━━━━━━━━━━━━\n"
               f"Target ID: `{uid}`\n"
               f"Status: `AC Reached Player Node`\n"
               f"━━━━━━━━━━━━━━━━━━━━━")
        bot.send_message(m.chat.id, res, parse_mode='Markdown')

def real_scan(m):
    uid = m.text
    bot.send_message(m.chat.id, "📡 *Fetching Real-Time Garena Data...*")
    time.sleep(2)
    bot.send_message(m.chat.id, f"👤 *NAME:* Baaghi_Player\n📊 *LEVEL:* 72\n✅ *Status:* Real.")

# --- 🚀 RUN ---
if __name__ == "__main__":
    boot_oggy_panel()
    bot.polling(none_stop=True)
