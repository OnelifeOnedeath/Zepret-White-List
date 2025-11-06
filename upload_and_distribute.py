#!/usr/bin/env python3
import os

def upload_instructions():
    print('''
📤 ЗАГРУЗКА APK НА GITHUB:

1. 📁 Файл WhiteList_1.0.apk создан!
   Размер: ~15KB

2. 🌐 Перейди: https://github.com/OnelifeOnedeath/Zepret-White-List

3. 📎 Нажми "Add file" → "Upload files"

4. 🖱️ Перетащи WhiteList_1.0.apk в окно

5. 💬 Описание: "Add WhiteList 1.0 APK release"

6. ✅ Нажми "Commit changes"

7. 🔗 Получи ссылку:
   https://github.com/OnelifeOnedeath/Zepret-White-List/raw/main/WhiteList_1.0.apk

🎯 APK ГОТОВ К ИСПОЛЬЗОВАНИЮ!
''')

def telegram_bot_ready():
    print('''
🤖 TELEGRAM БОТ С ГОТОВОЙ ССЫЛКОЙ:

Запусти этот код для бота:

```python
from telegram.ext import Application, CommandHandler

BOT_TOKEN = "8323149012:AAFo6uMsT0gox1HIrOxYEPhrGmXU8-aY20E"

app = Application.builder().token(BOT_TOKEN).build()

async def download(update, context):
    await update.message.reply_text(
        "📱 WhiteList 1.0\\n\\n"
        "🔗 Скачать:\\n"
        "https://github.com/OnelifeOnedeath/Zepret-White-List/raw/main/WhiteList_1.0.apk\\n\\n"
        "📋 Инструкция:\\n"
        "1. Нажми ссылку на телефоне\\n"
        "2. Скачай и установи APK\\n"
        "3. Запусти приложение\\n"
        "4. Нажми CONNECT\\n\\n"
        "📞 Поддержка: @OnelifeOnedeath"
    )

app.add_handler(CommandHandler("download", download))
app.run_polling()
