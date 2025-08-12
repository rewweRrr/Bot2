# Telegram Hello Bot — Vercel-ready (Python)

Этот проект содержит минимальный Telegram-бот на Python, адаптированный для деплоя на **Vercel** с использованием Serverless Functions.

Особенности:
- Endpoint: `GET/POST /api/webhook` — использовать в Telegram Webhook.
- Лёгкий: только `Flask` и `requests` в зависимостях.
- Пример `vercel.json` для явного указания Python runtime.

Файлы в проекте:
- `api/webhook.py` — основной обработчик (WSGI `app` для Vercel).
- `requirements.txt` — зависимости.
- `vercel.json` — конфигурация функций (опционально).
- `.env.example`, `.gitignore`, `LICENSE` и этот `README.md`.

Быстрое развёртывание на Vercel:
1. Зарегистрируйтесь/войдите в Vercel и создайте новый проект, подключив репозиторий GitHub.
2. В Settings → Environment Variables добавьте `TELEGRAM_BOT_TOKEN` со значением вашего токена (Production).
3. Деплой проекта. Ваш endpoint будет доступен по адресу:
   `https://<project-name>.vercel.app/api/webhook`
4. Установите webhook у Telegram (замените `<TOKEN>` и `<YOUR_URL>`):
   ```bash
   curl -F "url=https://<YOUR_PROJECT>.vercel.app/api/webhook" https://api.telegram.org/bot<TOKEN>/setWebhook
   ```

Замечания и ограничения:
- Vercel Functions — serverless: таймауты и cold starts возможны. Для простого ответа "hello" это нормально.
- Для длительных/фоновых задач используйте внешние очереди/сервисы или другой хостинг (Cloud Run / Render).

