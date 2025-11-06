import os
import time

while True:
    try:
        os.system("python mobile_proxy.py")
    except:
        time.sleep(60)  # Перезапуск через минуту при падении
