import httpx
from config import AI_API_KEY
from utils import clean_text

GEMINI_API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.0-flash:generateContent"
)

async def get_reponse(user_message: str) -> str:
    user_message = clean_text(user_message)

    url = f"{GEMINI_API_URL}?key={AI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]
    
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            print("⚠️ Trop de requêtes vers Gemini. Réessaie plus tard.")
            return "⚠️ Trop de requêtes ! Attends quelques secondes avant de réessayer."
        else:
            print("❌ Erreur Gemini:", e)
            return "❌ L'IA ne répond pas pour le moment."
