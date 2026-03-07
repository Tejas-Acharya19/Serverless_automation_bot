import requests
import json
import os
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
prompt = """
You are an English tutor.

Teach short English grammar patterns used in daily life.

Rules:
- Give 5 grammar patterns.
- Each pattern must have:
  1. Grammar word or phrase
  2. Short meaning
  3. 5 simple daily-life examples (office / home / work)

Keep explanations very short.

Format:

1. Grammar Pattern
Meaning:

Examples:
1.
2.
3.
4.
5.

2. Grammar Pattern
Meaning:

Examples:
1.
2.
3.
4.
5.

Continue until 5 patterns.
"""

gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

response = requests.post(gemini_url, json=payload).json()

text = response["candidates"][0]["content"]["parts"][0]["text"]
answer = text.strip()
# Save state
state = {"answer": answer}
with open("quiz_state.json", "w") as f:
    json.dump(state, f)

message = f"📘 Daily English Practice\n\n{text}"

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
