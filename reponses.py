import requests
from config import AI_API_KEY, AI_API_URL
from utils import clean_text

def get_reponse(user_message: str) -> str:
    user_message = clean_text(user_message)

    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Context-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content" : "Tu es un assistant utile et clair"
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": 0.7
    }

    try:
        reponse = requests.post(
            AI_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        reponse.raise_for_status()

        data = reponse.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return "Erreur IA. Reeesaie plsu tard"
    