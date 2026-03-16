from flask import Flask, request, render_template, jsonify
import subprocess
import os
import signal
import telebot

app = Flask(__name__)
current_process = None

# Notification bhejne ke liye function
def send_notification(token, admin_id, filename):
    try:
        bot = telebot.TeleBot(token)
        msg = (
            "🚀 **Z4X CLOUD: DEPLOYMENT SUCCESS**\n\n"
            f"📦 **File:** `{filename}`\n"
            "🟢 **Status:** `Active 24/7`\n"
            "💬 **Bot ab response dene ke liye taiyaar hai!**"
        )
        bot.send_message(admin_id, msg, parse_mode="Markdown")
    except Exception as e:
        print(f"Notification Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deploy', methods=['POST'])
def deploy():
    global current_process
    
    token = request.form.get('token')
    admin_id = request.form.get('admin')
    file = request.files.get('file')

    if not token or not admin_id or not file:
        return jsonify({"status": "error", "msg": "Saari details bhariye!"})

    # 1. Purane bot ko kill karo (Taaki Clash na ho)
    if current_process:
        try:
            os.kill(current_process.pid, signal.SIGTERM)
        except:
            pass

    # 2. File save karo
    file_path = "hosted_bot.py"
    file.save(file_path)

    # 3. File ke andar Token aur ID inject karo
    with open(file_path, 'r') as f:
        code = f.read()
    
    code = code.replace('YOUR_BOT_TOKEN', token).replace('YOUR_ADMIN_ID', admin_id)
    
    with open(file_path, 'w') as f:
        f.write(code)

    # 4. Bot ko naye process mein start karo
    try:
        current_process = subprocess.Popen(["python3", file_path])
        # 5. Telegram par success message bhejo
        send_notification(token, admin_id, file.filename)
        return jsonify({"status": "success", "msg": "Bot Deployed!"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
