from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import httpx  
from config import TELEGRAM_TOKEN
from utils import log_message
from reponses import get_reponse




# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.username or "Utilisateur"
    await update.message.reply_text(
        f"👋 Bienvenue *{user_name}* sur *SupraCodexIA* 🎭\n\n"
        "Pose-moi une question et je te répondrai 🤖",
        parse_mode="Markdown"
    )

# Gestion des messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_name = update.message.from_user.username or "Utilisateur"

    # Log
    log_message(user_name, user_text)

    # Message temporaire
    status_msg = await update.message.reply_text("🤖 Réflexion en cours...")

    # Obtenir la réponse de l'IA
    ai_response = await get_reponse(user_text)

    # Mettre à jour le message
    await status_msg.edit_text(ai_response)

# Main
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, start))

    print("🤖 Bot lancé avec succès")
    app.run_polling()


# Lancement
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Programme arrêté par l'utilisateur 😥")
