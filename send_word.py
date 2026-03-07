import requests
import os

# Environment variables from GitHub secrets
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

prompt = """
Give one advanced English word for vocabulary improvement.
Provide:
1. Word
2. Meaning
3. 5 example sentences using the word.
Format nicely.
"""

payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

response = requests.post(url, json=payload)
data = response.json()

text = data["candidates"][0]["content"]["parts"][0]["text"]

# Send to Telegram
telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

msg = {
    "chat_id": CHAT_ID,
    "text": text
}

requests.post(telegram_url, json=msg)
