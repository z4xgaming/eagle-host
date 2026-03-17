import requests

# Purani details jo kaam nahi kar rahi
key = 'xur3DfuVQZT2xNczj9unDwU5Fkj1'
user_uid = 'F57R6080kxRJ3Qg3BFW4m80gGItiLB' # Ye galat lag rahi hai
player_id = '8480955083'

# Hum dono version check karenge: main aur v2
urls = [
    f"https://proapis.hlgamingofficial.com/main/games/freefire/account/api?sectionName=AllData&PlayerUid={player_id}&region=ind&useruid={user_uid}&api={key}",
    f"https://proapis.hlgamingofficial.com/v2/games/freefire/account/api?sectionName=AllData&PlayerUid={player_id}&region=ind&useruid={user_uid}&api={key}"
]

for url in urls:
    print(f"\n🚀 Testing URL: {url[:50]}...")
    try:
        r = requests.get(url, timeout=10)
        print(f"📡 Status Code: {r.status_code}")
        print(f"📩 Response: {r.text}")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
