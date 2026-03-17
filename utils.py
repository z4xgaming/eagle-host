import time
import threading
import os

def start_safety_timer():
    def countdown():
        time.sleep(7200) # 2 Hours
        print("🛑 [SAFETY] 2 Hours finished. Shutting down to prevent BAN.")
        os._exit(0)
    
    thread = threading.Thread(target=countdown, daemon=True)
    thread.start()
