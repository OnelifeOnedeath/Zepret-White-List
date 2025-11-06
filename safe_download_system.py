#!/usr/bin/env python3
import hashlib
import datetime

class SafeDownloadSystem:
    def __init__(self):
        self.trusted_sources = [
            "github.com/OnelifeOnedeath",
            "t.me/ZapretWhitelist_backup", 
            "igorb9475@gmail.com"
        ]
    
    def generate_safe_links(self):
        """Генерирует безопасные ссылки"""
        timestamp = datetime.datetime.now().strftime("%d%m%Y")
        
        safe_links = {
            "primary": f"https://github.com/OnelifeOnedeath/Zepret-White-List/releases/download/v1.0/WhiteList_1.0.apk?{timestamp}",
            "backup": f"https://t.me/ZapretWhitelist_backup?{timestamp}",
            "direct": f"https://raw.githubusercontent.com/OnelifeOnedeath/Zepret-White-List/main/WhiteList_1.0.apk?{timestamp}",
            "email": "igorb9475@gmail.com"
        }
        return safe_links
    
    def verify_file_safety(self, file_path):
        """Проверяет безопасность файла"""
        expected_hash = "a1b2c3d4e5f67890"  # Реальный хеш нужно вычислить
        
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        
        return file_hash == expected_hash
    
    def get_download_instructions(self):
        """Инструкции по безопасному скачиванию"""
        return """
🔐 ИНСТРУКЦИЯ БЕЗОПАСНОГО СКАЧИВАНИЯ:

🏠 ДОМА (безопасно):
1. Зайдите на GitHub: onelifeonedeath.github.io
2. Скачайте из раздела Releases
3. Проверьте хеш файла

📱 ТЕЛЕФОН (через доверенного):
1. Попросите друга скачать файл
2. Передайте через Bluetooth
3. Или создайте локальную WiFi раздачу

🔄 АВАРИЙНЫЙ ВАРИАНТ:
1. Напишите @OnelifeOnedeath
2. Получите свежую ссылку
3. Скачайте через безопасное соединение

⚠️ НЕ ДЕЛАЙТЕ:
• Не качайте с чужих сайтов
• Не используйте публичные WiFi
• Не доверяйте подозрительным ссылкам
"""
