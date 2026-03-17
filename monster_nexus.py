import random
import os
import sys
import time

# Asli Bada Database File
DB_FILE = "nexus_unlimited_database.txt"

def get_hex():
    return "".join([random.choice('0123456789ABCDEF') for _ in range(6)])

def monster_generator():
    os.system('clear')
    print("\033[1;31m" + "🔥"*30)
    print("      NEXUS COMMANDER : UNLIMITED MONSTER ENGINE")
    print("      [ FULL CODE - NO LIMIT - TURBO SPEED ]")
    print("🔥"*30 + "\033[0m")

    name = "ONE LEVEL PLAYER"
    banner = "◢▓▓▓▓▓▓▀▀"
    
    print(f"\n\033[1;33m[!] Engine Starting... Codes 'Add' hote rahenge jab tak aap stop nahi karte.")
    print(f"[!] File: {DB_FILE}\033[0m\n")
    time.sleep(1)

    count = 0
    start_time = time.time()

    try:
        # 'a' mode taaki naya data hamesha purane ke niche ADD ho
        with open(DB_FILE, "a", encoding="utf-8") as f:
            while True:  # UNLIMITED LOOP
                batch = []
                # Performance ke liye 10,000 codes ka batch
                for _ in range(10000):
                    count += 1
                    lvl = (count % 100) + 1
                    c1, c2, c3, c4 = get_hex(), get_hex(), get_hex(), get_hex()
                    
                    # Timer Logic (Har code ke liye unique)
                    timer = f"{random.randint(0,99):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
                    
                    # Full Professional Format
                    code = (
                        f"ID:{count} | CATEGORY: ELITE-PRO\n"
                        f"[b][c][{c1}]{banner}\n"
                        f"[{c2}]█◤'╯ {name} [{c3}]Ⓥ-BADGE\n"
                        f"[FF0000]LOADING: {timer} [{c4}]LVL:{lvl}\n"
                        f"[00FF00]STATUS: SYSTEM ACTIVATED\n"
                        f"{'='*40}\n"
                    )
                    batch.append(code)
                
                f.write("".join(batch))

                # Display Speed and Progress
                elapsed = time.time() - start_time
                speed = int(count / (elapsed if elapsed > 0 else 1))
                sys.stdout.write(f"\r\033[1;32m[+] Codes Generated: {count:,} | Speed: {speed} codes/sec")
                sys.stdout.flush()

    except KeyboardInterrupt:
        print(f"\n\n\033[1;35m[STOPPED] Commander ne engine rok diya. Total {count:,} codes saved!")

if __name__ == "__main__":
    monster_generator()
