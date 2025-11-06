#!/usr/bin/env python3
import os
import base64

# Токен бота в зашифрованном виде
ENCRYPTED_TOKEN = "ODMyMzE0OTAxMjpBQUZvNnVNc1QwZ294MUhJck94WUVQaHJHbVhVOC1hWTIwRQ=="

def get_bot_token():
    """Расшифровывает токен бота"""
    try:
        return base64.b64decode(ENCRYPTED_TOKEN).decode('utf-8')
    except:
        return None

# Безопасные настройки
BOT_CONFIG = {
    "admin": "@OnelifeOnedeath",
    "email": "igorb9475@gmail.com", 
    "backup_channel": "@ZapretWhitelist_backup",
    "max_users": 10000
}

def validate_user(user_id):
    """Проверяет пользователя"""
    trusted_users = [
        123456789,  # @OnelifeOnedeath
    ]
    return user_id in trusted_users
