import requests
import urllib3
from colorama import Fore, Style

# SSL Warnings ko ignore karne ke liye
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- ⚙️ TERI DETAILS ---
API_KEY = 'xur3DfuVQZT2xNczj9unDwU5Fkj1'
TARGET_IP = "216.198.79.1" # Vercel IP jo humne nikaali thi

def check_endpoint(endpoint_name, url):
    headers = {
        "Host": "proapis.hlgamingofficial.com",
        "User-Agent": "Mozilla/5.0"
    }
    try:
        print(f"{Fore.YELLOW}🔍 Checking {endpoint_name}...{Style.RESET_ALL}")
        r = requests.get(url, headers=headers, verify=False, timeout=10)
        
        # Agar response mein data mil jaye
        if r.status_code == 200:
            print(f"{Fore.GREEN}✅ SUCCESS! Response found for {endpoint_name}:{Style.RESET_ALL}")
            print(r.text)
            return True
        else:
            print(f"{Fore.RED}❌ Failed ({r.status_code}){Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error: {e}{Style.RESET_ALL}")
        return False

print(f"{Fore.CYAN}🚀 HL GAMING ID DISCOVERY STARTED...{Style.RESET_ALL}\n")

# --- 🛠️ ALAG ALAG RAASTE (ENDPOINTS) ---
# Hum check karenge ki kaunsa raasta teri ID bata raha hai
test_urls = {
    "Profile Check": f"https://{TARGET_IP}/main/profile?api={API_KEY}",
    "Account Info": f"https://{TARGET_IP}/main/user/info?api={API_KEY}",
    "Dashboard Data": f"https://{TARGET_IP}/main/dashboard?api={API_KEY}",
    "Alternative Path": f"https://{TARGET_IP}/v2/user/details?api={API_KEY}"
}

found = False
for name, url in test_urls.items():
    if check_endpoint(name, url):
        found = True
        break

if not found:
    print(f"\n{Fore.MAGENTA}💡 Bhai, server direct details nahi de raha.{Style.RESET_ALL}")
    print(f"Ek baar ye try karo: Dashboard login karne ke baad URL mein dekho,")
    print(f"kya kahin '?id=12345' jaisa kuch likha hai?")

print(f"\n{Fore.CYAN}--- Scan Finished ---{Style.RESET_ALL}")
