#!/usr/bin/env python3
import requests

def check_bot_token():
    """Проверяет работоспособность токена бота"""
    token = "8323149012:AAFo6uMsT0gox1HIrOxYEPhrGmXU8-aY20E"
    
    print("[+] Проверяем токен бота...")
    
    try:
        response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
        if response.status_code == 200:
            data = response.json()
            print("✅ Токен рабочий!")
            print(f"🤖 Имя бота: {data['result']['first_name']}")
            print(f"🔗 Username: @{data['result']['username']}")
            return True
        else:
            print("❌ Токен не работает!")
            return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

check_bot_token()
