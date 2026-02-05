from datetime import datetime

def clean_text(text: str) -> str:
    return text.strip()

def add_timestamp(message: str) -> str:
    time = datetime.now().strftime("%H:%M")
    return f"[{time} {message}]"