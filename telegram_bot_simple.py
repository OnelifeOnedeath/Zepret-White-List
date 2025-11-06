#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Твой токен
BOT_TOKEN = "8519727279:AAE278hfJodKIE4Opxf0R-DkriqMrq4TZuw"

class SimpleBot:
    def __init__(self):
        self.app = Application.builder().token(BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("download", self.download))
        self.app.add_handler(CommandHandler("help", self.help))
    
    async def start(self, update: Update, context):
        await update.message.reply_text(
            "🤖 WhiteList Bot\n\n"
            "Скачай приложение для доступа ко всему интернету\n\n"
            "Команды:\n"
            "/download - Скачать приложение\n"
            "/help - Помощь\n\n"
            "Разработчик: @OnelifeOnedeath"
        )
    
    async def download(self, update: Update, context):
        """Отправляет ссылку на скачивание"""
        download_text = """
📱 WhiteList 1.0

🔗 Скачать приложение:

https://github.com/OnelifeOnedeath/Zepret-White-List/raw/main/WhiteList_1.0.apk

📋 Инструкция:
1. Нажми ссылку на телефоне
2. Скачай файл
3. Установи APK
4. Запусти и нажми АКТИВИРОВАТЬ
5. Готово! Интернет работает

📞 Поддержка: @OnelifeOnedeath
"""
        await update.message.reply_text(download_text)
    
    async def help(self, update: Update, context):
        help_text = """
🆘 Помощь:

• Скачать: /download
• Проблемы: @OnelifeOnedeath
• Исходный код: https://github.com/OnelifeOnedeath/Zepret-White-List

📱 Приложение работает через мобильную сеть и WiFi
"""
        await update.message.reply_text(help_text)
    
    def run(self):
        """Запуск бота"""
        print("🚀 Запускаем бота...")
        print(f"✅ Токен: {BOT_TOKEN}")
        self.app.run_polling()

# ЗАПУСК БОТА
if __name__ == "__main__":
    bot = SimpleBot()
    bot.run()
