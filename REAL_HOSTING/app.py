import os, subprocess, requests
from flask import Flask, render_template, request

app = Flask(__name__)
UPLOAD_FOLDER = 'hosted_bots'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def notify_user(token, admin_id, filename):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        text = f"🚀 **Z4X CLOUD: DEPLOYMENT SUCCESS**\n\n📦 **File:** `{filename}`\n🟢 **Status:** Active 24/7"
        requests.post(url, data={"chat_id": admin_id, "text": text, "parse_mode": "Markdown"})
    except: pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deploy', methods=['POST'])
def deploy():
    token = request.form.get('token')
    admin = request.form.get('admin')
    file = request.files['file']

    if file and file.filename.endswith('.py'):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        with open(file_path, 'r') as f:
            content = f.read()
        
        # Injection Logic
        content = content.replace("YOUR_BOT_TOKEN", token).replace("YOUR_ADMIN_ID", admin)
        
        with open(file_path, 'w') as f:
            f.write(content)

        # Background Execution
        subprocess.Popen(['python', file_path])
        notify_user(token, admin, file.filename)
        
        return "✅ Server Started Successfully!"
    return "❌ Invalid File!", 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
