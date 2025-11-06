#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
from config_secure import get_bot_token, validate_user
import logging

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SecureBot:
    def __init__(self):
        self.token = get_bot_token()
        if not self.token:
            logger.error("❌ Не удалось расшифровать токен!")
            return
            
        self.bot = Application.builder().token(self.token).build()
        self.setup_handlers()
        logger.info("✅ Бот инициализирован с защищенным токеном")
    
    def setup_handlers(self):
        self.bot.add_handler(CommandHandler("start", self.secure_start))
        self.bot.add_handler(CommandHandler("download", self.secure_download))
        self.bot.add_handler(CommandHandler("help", self.secure_help))
    
    async def secure_start(self, update, context):
        user_id = update.effective_user.id
        if not validate_user(user_id):
            await update.message.reply_text("❌ Доступ ограничен")
            return
            
        await update.message.reply_text(
            "🔒 Secure WhiteList Bot\n\n"
            "Безопасное распространение\n\n"
            "Команды:\n"
            "/download - Получить ссылки\n"
            "/help - Помощь\n\n"
            "Разработчик: @OnelifeOnedeath"
        )
    
    async def secure_download(self, update, context):
        user_id = update.effective_user.id
        if not validate_user(user_id):
            await update.message.reply_text("❌ Доступ ограничен")
            return
            
        download_info = """
🔐 БЕЗОПАСНЫЕ ССЫЛКИ ДЛЯ СКАЧИВАНИЯ:

📱 WhiteList 1.0:

⭐ ОСНОВНЫЕ ССЫЛКИ:
1. GitHub Releases:
   onelifeonedeath.github.io/Zepret-White-List

2. Резервный канал:
   t.me/ZapretWhitelist_backup

3. Автономная раздача:
   Локальная сеть или Bluetooth

🛡️ КАК СКАЧАТЬ БЕЗОПАСНО:
• Используйте только эти ссылки
• Проверяйте подпись разработчика
• Не качайте с подозрительных сайтов
• Обновляйте через официальные каналы

📞 Если ссылки не работают:
Пишите @OnelifeOnedeath для получения новой ссылки
"""
        await update.message.reply_text(download_info)
    
    async def secure_help(self, update, context):
        user_id = update.effective_user.id
        if not validate_user(user_id):
            await update.message.reply_text("❌ Доступ ограничен")
            return
            
        help_text = """
🛡️ БЕЗОПАСНАЯ УСТАНОВКА:

1. Получите ссылку через /download
2. Скачайте на проверенном устройстве
3. Проверьте SHA256 хеш файла
4. Установите на целевое устройство
5. Активируйте приложение

🔒 МЕРЫ БЕЗОПАСНОСТИ:
• Токен бота зашифрован
• Ограниченный доступ
• Проверка пользователей
• Резервные каналы связи
"""
        await update.message.reply_text(help_text)

if __name__ == "__main__":
    print("🚀 Запуск защищенного бота...")
    bot = SecureBot()
    if bot.token:
        bot.bot.run_polling()
