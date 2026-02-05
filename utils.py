from datetime import datetime

def clean_text(text: str) -> str:
    return text.strip()

def log_message(user: str, message: str):
    with open("messages.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {user}: {message}\n")
        print(f"[{datetime.now()}] {user}: {message}\n")
