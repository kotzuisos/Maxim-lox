import os, sys, urllib.request, zipfile, subprocess

# 1. Создаем локальную папку для временных файлов (обходим ошибку "No space left in /tmp")
os.makedirs('./my_tmp', exist_ok=True)
os.environ['TMPDIR'] = os.path.abspath('./my_tmp')
os.environ['PIP_NO_CACHE_DIR'] = '1'
os.environ['PYTHONUNBUFFERED'] = '1'

print(">>> Скачиваю архив с ботом...")
# ВАЖНО: Вставь сюда ссылку на СКАЧИВАНИЕ ZIP твоего репозитория с ботом
# Формат: https://github.com/ТВОЙ_ЛОГИН/ТВОЙ_РЕПО/archive/refs/heads/main.zip
url = "https://github.com/kotzuisos/ratko/archive/refs/heads/main.zip"
urllib.request.urlretrieve(url, "bot.zip")

print(">>> Распаковываю...")
with zipfile.ZipFile("bot.zip", 'r') as z:
    z.extractall(".")
os.remove("bot.zip") # Удаляем архив, чтобы освободить место

# Ищем распакованную папку (она будет называться типа ratko-main)
bot_folder = [f for f in os.listdir('.') if os.path.isdir(f)][0]
os.chdir(bot_folder)

print(">>> Устанавливаю зависимости...")
# Устанавливаем пакеты
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--no-cache-dir', '-r', 'requirements.txt'])

print(">>> Запускаю бота!")
# Запускаем бота
os.execv(sys.executable, [sys.executable, '-m', 'heroku', '--root', '--no-web'])
