#bot.py
from telegram import Update
from telegram.exit import(
	ApplicationBuilder,
	commandHandler,
	MessageHandler,
	ContextType,
	filters,
)
from config import TOKEN
from responses import get_response
from utils import format_text, log_message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text("Salut!! je suis le bot de hacker et son equipe. \n" "Envoie-moi un message et je te repondrai"
)

async def handle_message(update: Update, context: ContexTypes.DEFAULT_TYPE): """Reagit a tout les messages envoye par l'utilisateur"""
	user_message=update.message.text
	username=update.message.from_user.first_name

	formatted=format_text(user_message)
	log_message(username, formatted)

	bot_reply=get_response(formatted)

	await update.message.reply_text(bot_reply)


def main(): """Fonction principale qui demarre le bot"""
	app: ApplicationBuilder().token(TOKEN).build()
	app.add_handler(commandler("start", start))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
	print("Bot en ligne et connecte a telegram....")
	app.run_polling()


if __name__=="__main__":main()
