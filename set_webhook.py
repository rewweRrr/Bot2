# set_webhook.py
import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env (если файл есть в текущей директории)
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not TOKEN or not WEBHOOK_URL:
    raise RuntimeError(
        "❌ TELEGRAM_BOT_TOKEN или WEBHOOK_URL не установлены.\n"
        "Добавьте их в .env файл или задайте как переменные окружения."
    )

url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
resp = requests.post(url, data={"url": WEBHOOK_URL})
print("Ответ Telegram:", resp.json())
