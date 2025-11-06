import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

class ZapretBot:
    def __init__(self):
        self.token = "8323149012:AAFo6uMsT0gox1HIrOxYEPhrGmXU8-aY20E"
        self.bot = Application.builder().token(self.token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        self.bot.add_handler(CommandHandler("start", self.start))
        self.bot.add_handler(CommandHandler("apk", self.send_apk))
        self.bot.add_handler(CommandHandler("apps", self.send_apps_list))
        self.bot.add_handler(CommandHandler("help", self.help))
        self.bot.add_handler(CommandHandler("support", self.support))
    
    async def start(self, update: Update, context):
        await update.message.reply_text(
            "🔓 ZapretWhitelist Bot\n\n"
            "Доступ ко всему интернету через WhiteList 1.0\n\n"
            "Команды:\n"
            "/apk - Скачать приложение\n"
            "/apps - Какие приложения работают\n"
            "/help - Инструкция\n"
            "/support - Связь с разработчиком\n\n"
            "Бот: @ZapretWhitelist_bot\n"
            "Разработчик: @OnelifeOnedeath"
        )
    
    async def send_apk(self, update: Update, context):
        message = await update.message.reply_text("📥 Готовлю ссылки для скачивания...")
        
        # Отправляем текстовые ссылки
        download_text = """
🔗 ССЫЛКИ ДЛЯ СКАЧИВАНИЯ:

1. 📱 WhiteList 1.0 APK:
https://github.com/OnelifeOnedeath/Zepret-White-List/raw/main/WhiteList_1.0.apk

2. 🔄 Резервная ссылка:
https://transfer.sh/abc123/WhiteList_1.0.apk

3. 💾 Прямая загрузка:
https://dl.onelifeonedeath.com/whitelist.apk

📲 QR код для установки:
[отправляем следующим сообщением]

⚡ Инструкция:
1. Скачайте APK
2. Установите на Android
3. Запустите и нажмите АКТИВИРОВАТЬ
4. Разрешите VPN подключение
5. Готово!
        """
        await update.message.reply_text(download_text)
        
        # Здесь должен быть реальный файл APK
        # await update.message.reply_document(document=open('WhiteList_1.0.apk', 'rb'))
    
    async def send_apps_list(self, update: Update, context):
        apps_text = """
✅ ПРИЛОЖЕНИЯ КОТОРЫЕ РАБОТАЮТ:

🔹 Соцсети:
• Telegram • WhatsApp • Viber • Discord
• Instagram • Facebook • Twitter • VK

🔹 Видео/Музыка:
• YouTube • YouTube Music • Twitch
• Netflix • Spotify • SoundCloud

🔹 Работа:
• Gmail • Google Drive • Zoom • Teams
• Google Docs • Outlook • Dropbox

🔹 Игры:
• Steam • Epic Games • Battle.net
• Любые онлайн-игры

🔹 Браузеры:
• Chrome • Firefox • Opera • Safari

🔹 И многое другое!
        """
        await update.message.reply_text(apps_text)
    
    async def help(self, update: Update, context):
        help_text = """
🛠️ ИНСТРУКЦИЯ ПО УСТАНОВКЕ:

1. Скачайте APK через /apk
2. На Android: Настройки → Безопасность → Неизвестные источники ✅
3. Установите WhiteList 1.0
4. Запустите приложение
5. Нажмите "АКТИВИРОВАТЬ"
6. Разрешите VPN подключение
7. Готово! Интернет работает 🎉

📞 Если проблемы - пишите /support
        """
        await update.message.reply_text(help_text)
    
    async def support(self, update: Update, context):
        support_text = """
📞 КОНТАКТЫ ПОДДЕРЖКИ:

• Telegram: @OnelifeOnedeath
• Email: igorb9475@gmail.com  
• VK: OnelifeOnedeath

💬 Пишите по любым вопросам:
- Проблемы с установкой
- Приложение не работает
- Нужна помощь с настройкой
- Предложения по улучшению

⏰ Отвечаю в течение 24 часов
        """
        await update.message.reply_text(support_text)

# Запускаем бота
if __name__ == "__main__":
    print("🚀 Запуск бота @ZapretWhitelist_bot...")
    bot = ZapretBot()
    bot.bot.run_polling()
    print("✅ Бот запущен!")
