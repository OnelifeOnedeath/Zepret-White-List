import os
import time
import subprocess

def restart_on_crash():
    while True:
        try:
            print("[+] Starting WhiteList proxy...")
            # Запускаем прокси
            process = subprocess.Popen(["python", "mobile_proxy.py"])
            process.wait()  # Ждем завершения
        except Exception as e:
            print(f"[-] Crash detected: {e}")
        
        print("[+] Restarting in 10 seconds...")
        time.sleep(10)

if __name__ == "__main__":
    restart_on_crash()
