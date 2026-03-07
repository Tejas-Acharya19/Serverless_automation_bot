import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

prompt = """
Give one advanced English vocabulary word.
Provide:
Word
Meaning
5 example sentences.
"""

payload = {
    "contents": [
        {
            "parts": [{"text": prompt}]
        }
    ]
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if "candidates" in data:
        text = data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        text = "⚠️ Gemini API did not return expected output."

except Exception as e:
    text = f"Error generating word: {str(e)}"

# Send message to Telegram
telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

msg = {
    "chat_id": CHAT_ID,
    "text": text
}

requests.post(telegram_url, json=msg)
