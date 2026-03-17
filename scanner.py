import requests
import urllib3
from colorama import Fore, Style

urllib3.disable_warnings()

# --- TERI DETAILS ---
API_KEY = 'xur3DfuVQZT2xNczj9unDwU5Fkj1'
PLAYER_ID = '8480955083' # Test karne ke liye ek FF ID
TARGET_IP = "216.198.79.1"

# Jo numbers tune dhoondhe hain unki list
uids_to_test = ['43727149', '6080', '9844', '9999', '84809550', '2026']

def test_uid(u_id):
    url = f"https://{TARGET_IP}/main/games/freefire/account/api"
    params = {
        'sectionName': 'AllData',
        'PlayerUid': PLAYER_ID,
        'region': 'ind',
        'useruid': u_id,
        'api': API_KEY
    }
    headers = {"Host": "proapis.hlgamingofficial.com", "User-Agent": "Mozilla/5.0"}
    
    try:
        r = requests.get(url, params=params, headers=headers, verify=False, timeout=5)
        data = r.json()
        
        if data.get('status') == 'success' or 'result' in data:
            return True, data['result']['AccountInfo'].get('AccountName')
        else:
            return False, data.get('message', 'Invalid')
    except:
        return False, "Connection Error"

print(f"{Fore.CYAN}🕵️ Starting Auto-Scan for {len(uids_to_test)} UIDs...{Style.RESET_ALL}\n")

for uid in uids_to_test:
    print(f"Testing UID: {Fore.YELLOW}{uid}{Style.RESET_ALL}", end=" -> ")
    success, result = test_uid(uid)
    
    if success:
        print(f"{Fore.GREEN}✅ MATCH FOUND! (Name: {result}){Style.RESET_ALL}")
        print(f"\n{Fore.MAGENTA}🔥 Bhai, mil gaya! Tera real UserUID hai: {uid}{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}❌ Failed ({result}){Style.RESET_ALL}")

print(f"\n{Fore.CYAN}--- Scan Finished ---{Style.RESET_ALL}")
