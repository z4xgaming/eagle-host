import requests
import time

# Ye khali chhod do, hamara cloud ise khud bhar dega
TOKEN = "8480955083:AAFVIXXvXmbt7irxXTUte3ppItRDwn_0CXA"
ADMIN_ID = "8037300335"

def check():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": ADMIN_ID, "text": "🔥 Z4X CLOUD SUCCESS!\nBhai tera server mast chal raha hai!"}
    requests.post(url, json=data)

if __name__ == "__main__":
    check()
    while True:
        time.sleep(60)
