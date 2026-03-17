import requests

def debug_forbidden():
    url = "https://proapis.hlgamingofficial.com/main/games/freefire/account/api"
    # Bina params ke check karte hain server kya bolta hai
    r = requests.get(url)
    
    print(f"📡 Status Code: {r.status_code}")
    print(f"📝 Server Message: {r.text}")
    
    if "Cloudflare" in r.text or "403 Forbidden" in r.text:
        print("\n🔥 [DETECTED]: Bhai, HL Gaming ne tere Termux IP ko block kiya hai.")
        print("Tujhe Dashboard par ja kar IP WHITELIST karna hi padega.")
    else:
        print("\n✅ Server is open, but your UID/Key is the issue.")

debug_forbidden()
