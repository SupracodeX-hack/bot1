def get_reponse(message):
    message=message.lower()
    if message=="bonjour" or message=="salut":
        return "bonjour comment puis-je vous aider ?"
    elif message=="hello" or message=="hi":
        return "hello ravi de te vooir ici"

    elif message=="aide":
      return "je peux repondre a des messages simples comme bonjour,aide,info."

    elif message=="info":
        return "je suis un bot telegramme crée par notre équipe"

    else:
        return "Désolée je n'ai pas compris ton message"

        print("Tape un message (ecris 'exit' pour quitter)")
  
        while True:
            message=input("Toi:")  
            if message=="exit":
                print("test termine")
                break
                reponse=get_reponse(message)
                print("Bot:",reponse)
