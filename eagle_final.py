import telebot, time, os
from telebot import types

# --- 🔑 TOKEN YAHAN DALO (BotFather se lo) ---
TOKEN = '8480955083:AAFVIXXvXmbt7irxXTUte3ppItRDwn_0CXA'   # <-- Apna token yahan paste karo
bot = telebot.TeleBot(TOKEN)

# System Info
MY_UID = "4372714908"      # Admin UID (apna dal sakte ho)
PORT = 9999                 # Spain Port AC

# --- 🎭 OGGY FACE BANNER (Termux UI) ---
def boot_oggy_panel():
    os.system('clear')
    # OGGY in Blue
    print("\033[1;34m")
    print("╔══════════════════════════════════════════════════════╗")
    print("║                                                      ║")
    print("║        ██████╗  ██████╗  ██████╗ ██╗   ██╗          ║")
    print("║       ██╔════╝ ██╔════╝ ██╔═══██╗╚██╗ ██╔╝          ║")
    print("║       ██║  ███╗██║  ███╗██║   ██║ ╚████╔╝           ║")
    print("║       ██║   ██║██║   ██║██║   ██║  ╚██╔╝            ║")
    print("║       ╚██████╔╝╚██████╔╝╚██████╔╝   ██║             ║")
    print("║        ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝             ║")
    print("║                                                      ║")
    # OCKROACHES in Brown/Yellow
    print("\033[1;33m")
    print("║      ░█████╗░░█████╗░░█████╗░██╗░░██╗██████╗░░░     ║")
    print("║      ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔══██╗░     ║")
    print("║      ██║░░╚═╝██║░░██║██║░░╚═╝█████═╝░██████╔╝░     ║")
    print("║      ██║░░██╗██║░░██║██║░░██╗██╔═██╗░██╔══██╗░     ║")
    print("║      ╚█████╔╝╚█████╔╝╚█████╔╝██║░╚██╗██║░░██║░     ║")
    print("║      ░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░     ║")
    print("║                                                      ║")
    # System Info in Cyan
    print("\033[1;36m")
    print(f"║          SPAIN PORT AC : {PORT} ── ACTIVE ✅          ║")
    print(f"║          ADMIN UID: {MY_UID}                         ║")
    print("║                                                      ║")
    print("╚══════════════════════════════════════════════════════╝")
    print("\033[0m")  # Reset color
    print("\033[1;32m[!] STATUS: REBEL MODE ACTIVE 🟢")
    print("\033[1;37m[LOG] System Ready. Oggy is waiting for commands...")

# --- 🛰️ SPAIN PORT AC INJECTION (FAKE) ---
def spain_port_inject(target_uid):
    steps = ["Locating Player...", "Spain Port Bypass...", "Injecting AC Work..."]
    for step in steps:
        time.sleep(1)
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
    msg = ("🐱 *OGGY REBEL V10* 🐱\n"
           "━━━━━━━━━━━━━━━━━━━━━\n"
           "Bhai, Termux dashboard par Oggy ka banner lag gaya hai!\n\n"
           "Option select karo:")
    bot.send_message(m.chat.id, msg, reply_markup=mk, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda c: True)
def process_handle(c):
    if c.data == "spain":
        q = bot.send_message(c.message.chat.id, "🎯 *Target UID dalo (Spain Port AC Work):*")
        bot.register_next_step_handler(q, start_injection)
    elif c.data == "jwt":
        # JWT button ke liye response
        bot.answer_callback_query(c.id, "🔐 JWT Token: ID: admin | PASS: oggy@9999")
        bot.send_message(c.message.chat.id, "🔑 *JWT GENERATED*\n━━━━━━━━━━━━━━\n`ID: admin`\n`PASS: oggy@9999`\n*(Demo data – real feature coming soon)*", parse_mode='Markdown')
    elif c.data == "scan":
        q = bot.send_message(c.message.chat.id, "🔍 *Real UID dalo Scan ke liye:*")
        bot.register_next_step_handler(q, real_scan)

def start_injection(m):
    uid = m.text
    bot.send_message(m.chat.id, f"⚡ *SPAIN PORT:* Injecting AC packets into `{uid}`... Game ke andar check karein.", parse_mode='Markdown')
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
    bot.send_message(m.chat.id, "📡 *Fetching Real-Time Garena Data...*", parse_mode='Markdown')
    time.sleep(2)
    # Baaghi_Player mein underscore hai – isliye parse_mode nahi diya (default plain text)
    bot.send_message(m.chat.id, f"👤 *NAME:* Baaghi_Player\n📊 *LEVEL:* 72\n✅ *Status:* Real.")

# --- 🚀 RUN ---
if __name__ == "__main__":
    boot_oggy_panel()
    print("\n✅ Bot is running... Press Ctrl+C to stop.\n")
    bot.polling(none_stop=True)
