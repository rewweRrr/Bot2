# Simple Telegram webhook for Vercel (WSGI via Flask)
# Vercel will use the `app` variable as the WSGI entrypoint.
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

@app.route('/', methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def webhook(path=""):
    # Basic health-check on GET
    if request.method == 'GET':
        return 'Telegram Hello Bot (Vercel) OK'

    data = request.get_json(silent=True)
    if not data:
        return jsonify({'ok': False, 'error': 'no json body'}), 400

    # get chat id from common update shapes
    chat_id = None
    if 'message' in data and data['message'] and 'chat' in data['message']:
        chat_id = data['message']['chat']['id']
    elif 'edited_message' in data and data['edited_message'] and 'chat' in data['edited_message']:
        chat_id = data['edited_message']['chat']['id']
    else:
        # ignore callback_query, inline_query etc for simplicity
        return jsonify({'ok': True, 'status': 'ignored update type'}), 200

    if not TOKEN:
        # fail with clear message so logs show missing token
        return jsonify({'ok': False, 'error': 'TELEGRAM_BOT_TOKEN not set'}), 500

    send_url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': 'hello'
    }
    try:
        r = requests.post(send_url, json=payload, timeout=5)
        r.raise_for_status()
    except requests.RequestException as e:
        return jsonify({'ok': False, 'error': str(e)}), 502

    return jsonify({'ok': True}), 200

# Note: when running locally with `vercel dev`, the app will be picked up.
