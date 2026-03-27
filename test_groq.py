import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('GROQ_API_KEY')

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": "भारत की राजधानी क्या है?"}],
    "temperature": 0.7,
    "max_tokens": 100
}

try:
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=30
    )
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("✅ Answer:", data['choices'][0]['message']['content'])
    else:
        print("❌ Error:", response.text)

except Exception as e:
    print("❌ Exception:", str(e))