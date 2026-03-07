import requests
import os
import json

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

prompt = """
Give one advanced English vocabulary word.
Provide:
Word:
Meaning:
5 sentences using the word.
Keep it concise.
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

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=payload)

data = response.json()

# Debug print (helps if API fails)
print(json.dumps(data, indent=2))

try:
    text = data["candidates"][0]["content"]["parts"][0]["text"]
except KeyError:
    text = "Error generating word. Check Gemini API response."

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

msg = {
    "chat_id": CHAT_ID,
    "text": text
}

requests.post(telegram_url, json=msg)
