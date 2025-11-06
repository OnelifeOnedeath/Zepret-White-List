#!/usr/bin/env python3
import webbrowser

def create_apk_guide():
    print('''
🎯 КАК СОЗДАТЬ РАБОЧИЙ APK:

1. 📥 СКАЧАТЬ ANDROID STUDIO:
   https://developer.android.com/studio
   (открываю ссылку...)

2. 🏗️ СОЗДАТЬ НОВЫЙ ПРОЕКТ:
   - File → New → New Project
   - Empty Activity
   - Name: WhiteList
   - Package: com.whitelist.bypass
   - Language: Java
   - Minimum SDK: Android 5.0

3. 📁 ЗАМЕНИТЬ ФАЙЛЫ:
   - Скопируй наш MainActivity.java в app/src/main/java/com/whitelist/bypass/
   - Скопируй наш VPNService.java в ту же папку
   - Обнови AndroidManifest.xml нашим кодом

4. 🔨 СОБРАТЬ APK:
   - Build → Generate Signed Bundle / APK
   - Выбери APK
   - Создай новый ключ (запомни пароль!)
   - Выбери build variant: release

5. 📤 ЗАГРУЗИТЬ НА GITHUB:
   - Готовый APK будет в app/build/outputs/apk/release/app-release.apk
   - Переименуй в WhiteList_1.0.apk
   - Загрузи в репозиторий

⏱️ Это займет 30-60 минут
''')
    
    # Открываем Android Studio для скачивания
    webbrowser.open("https://developer.android.com/studio")

create_apk_guide()
