import requests
from colorama import Fore, init

init(autoreset=True)

# --- 📋 TERI DETAILS ---
API_KEY = 'xur3DfuVQZT2xNczj9unDwU5Fkj1'
USER_UID = 'F57R6080kxRJ3Qg3BFW4m80gGItiLB' # Jo tune di thi

def get_dashboard_info():
    print(Fore.YELLOW + "📡 Connecting to HL Gaming Server Node...")
    
    # Hum ek dummy request bhej rahe hain server ka response dekhne ke liye
    url = f"https://proapis.hlgamingofficial.com/main/games/freefire/account/api"
    params = {
        'sectionName': 'AllData',
        'PlayerUid': '8480955083', # Test ke liye
        'region': 'ind',
        'useruid': USER_UID,
        'api': API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        
        print(Fore.CYAN + "\n📊 --- DASHBOARD STATUS ---")
        if response.status_code == 200:
            data = response.json()
            if "result" in data:
                print(Fore.GREEN + "✅ STATUS: ACTIVE")
                print(Fore.WHITE + f"🆔 YOUR USER UID: {USER_UID}")
                print(Fore.WHITE + f"🔑 API KEY VALID: YES")
                print(Fore.WHITE + f"📡 SERVER STATUS: ONLINE")
            else:
                print(Fore.RED + "❌ ERROR: " + data.get('message', 'Invalid User UID or Key'))
                print(Fore.YELLOW + "💡 Tip: Dashboard par check karo ye UID 'Developer ID' hai ya nahi.")
        elif response.status_code == 401:
            print(Fore.RED + "❌ UNAUTHORIZED: Key ya UID galat hai.")
        else:
            print(Fore.RED + f"❌ SERVER SIDE PROBLEM: Code {response.status_code}")

    except Exception as e:
        print(Fore.RED + f"⚠️ Connection Failed: {str(e)}")

if __name__ == "__main__":
    get_dashboard_info()
