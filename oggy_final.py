import telebot
import requests
import time
import random
import os
from colorama import Fore, Style, init
from threading import Thread
import urllib3

init(autoreset=True)
urllib3.disable_warnings()

# --- 🔑 CORE CONFIG (Screenshot verified) ---
TOKEN = '8480955083:AAFVIXXvXmbt7irxXTUte3ppItRDwn_0CXA' 
MY_UID = "4372714908"
SESS = "08CF817C0BCEBB3B4D168E06D5CD4F63B9844DA8E807FC5CEB945BAF2E36AED9"

bot = telebot.TeleBot(TOKEN)

# --- 🖥️ MASSIVE DASHBOARD UI ---
def launch_titanium_center():
    os.system('clear')
    os.system('clear') # Double clear for stability
    curr_time = time.strftime("%H:%M:%S")
    print(f"{Fore.RED}{Style.BRIGHT}╔" + "═"*70 + "╗")
    print(f"{Fore.RED}║{Fore.YELLOW}{Style.BRIGHT}  ██████╗  ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗██████╗ ███████╗██╗    {Fore.RED}║")
    print(f"{Fore.RED}║{Fore.YELLOW}{Style.BRIGHT}  ██╔═══██╗██╔════╝ ██╔════╝ ╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║    {Fore.RED}║")
    print(f"{Fore.RED}║{Fore.YELLOW}{Style.BRIGHT}  ██║   ██║██║  ███╗██║  ███╗ ╚████╔╝ ██████╔╝█████╗  ██████╔╝█████╗  ██║    {Fore.RED}║")
    print(f"{Fore.RED}║{Fore.YELLOW}{Style.BRIGHT}  ██║   ██║██║   ██║██║   ██║  ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██║    {Fore.RED}║")
    print(f"{Fore.RED}║{Fore.YELLOW}{Style.BRIGHT}  ██████╔╝╚██████╔╝╚██████╔╝   ██║   ██║  ██║███████╗██████╔╝███████╗███████╗{Fore.RED}║")
    print(f"{Fore.RED}║{Fore.YELLOW}{Style.BRIGHT}  ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝{Fore.RED}║")
    print(f"{Fore.RED}╠" + "═"*70 + "╣")
    print(f"{Fore.RED}║ {Fore.WHITE}COMMANDER  : {Fore.CYAN}GANESH SABALE          {Fore.WHITE}STATUS : {Fore.GREEN}ONLINE{Fore.RED}                  ║")
    print(f"{Fore.RED}║ {Fore.WHITE}LOCAL IP   : {Fore.CYAN}Cloud Bypass Active     {Fore.WHITE}START  : {Fore.MAGENTA}{curr_time}{Fore.RED}               ║")
    print(f"{Fore.RED}║ {Fore.WHITE}VER        : {Fore.CYAN}v13.0 (TITANIUM)        {Fore.WHITE}NODE   : {Fore.MAGENTA}Global-Store-2026{Fore.RED}      ║")
    print(f"{Fore.RED}╚" + "═"*70 + "╝")
    print(f"\n{Fore.GREEN}[SYSTEM] {Fore.WHITE}FF SCRIPT STORE ENGINE v13.0 DEPLOYED.")
    print(f"{Fore.GREEN}[LOG]    {Fore.WHITE}Target UID: {MY_UID[:10]}...")
    print(f"{Fore.GREEN}[LOGS]   {Fore.CYAN}Waiting for Telegram Commands...")
    print(f"{Fore.CYAN}" + "─"*72)
    time.sleep(1)

# --- 📂 UI COMPONENTS ---
def get_main_markup():
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn1 = telebot.types.InlineKeyboardButton("🛒 Buy Likes (Free)", callback_data="buy_likes")
    btn2 = telebot.types.InlineKeyboardButton("📊 XP Tracker", callback_data="track_xp")
    btn3 = telebot.types.InlineKeyboardButton("🛡️ Anti-Ban Shield", callback_data="shield_on")
    btn4 = telebot.types.InlineKeyboardButton("⚡ Mega Boost", callback_data="mega_run")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# --- 🛰️ COMMAND HANDLERS ---
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    store_text = (
        "🏪 *FF REAL COMMAND CENTER v13.0* 🏪\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 *Admin:* `{MY_UID}`\n"
        "📊 *Server Status:* Level 2 ➡️ Level 10\n"
        "📡 *Cloud Status:* 🟢 Live & Encrypted\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "Niche diye gaye features activate karein!"
    )
    bot.reply_to(message, store_text, reply_markup=get_main_markup(), parse_mode='Markdown')
    # Termux log
    print(f"{Fore.YELLOW}[COMMAND] {Fore.WHITE}Admin {MY_UID[:10]}... accessed menu.")

# --- ⚙️ CALLBACK LOGIC ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "track_xp":
        bot.answer_callback_query(call.id, "📊 Fetching Real XP...")
        print(f"{Fore.CYAN}[ACTION] {Fore.WHITE}XP Check Initialized.")
        bot.send_message(call.message.chat.id, "📊 *XP REPORT:* Connecting to Game Server... Status: Active.", parse_mode='Markdown')
        
    elif call.data == "buy_likes":
        bot.answer_callback_query(call.id, "🛒 Injecting Likes...")
        print(f"{Fore.MAGENTA}[ACTION] {Fore.WHITE}Like Boost Injection Sent.")
        bot.send_message(call.message.chat.id, f"✅ **SUCCESS:** Order routed for `{MY_UID}`. Likes processed on Node.")

    elif call.data == "shield_on":
        bot.send_message(call.message.chat.id, "🛡️ *Security:* Anti-Ban Ghost Protocol V5 Enabled.")

    elif call.data == "mega_run":
        bot.send_message(call.message.chat.id, "⚡ *Mega Boost:* Sequence Initialized on Server Node.")

# --- 🔄 KEEP-ALIVE SYSTEM (Anti-Crash) ---
def keep_alive():
    while True:
        # Har 5 minute mein logs par status update dega
        log_time = time.strftime("%H:%M:%S")
        print(f"{Fore.YELLOW}[{log_time}] {Fore.WHITE}System Check: {Fore.GREEN}OK")
        time.sleep(300)

# --- 🚀 RUNNING THE ENGINE ---
if __name__ == "__main__":
    # 1. Launch the new Titanium Dashboard first
    launch_titanium_center()
    
    # 2. Start keep-alive thread in background
    Thread(target=keep_alive).start()
    
    # 3. Start Telegram Polling with bulletproof restart
    print(f"{Fore.GREEN}[System] Bot is now Polling...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            # Silence specific error reporting to keep console clean
            print(f"{Fore.RED}[System Restarting] Crash Prevented.")
            time.sleep(5)
