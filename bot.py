import telebot

bot = telebot.TeleBot("YOUR_API_KEY_HERE")

activeChats = {}

def listener(messages):
    for m in messages:
        if m.content_type == 'text' and m.reply_to_message:
            text = m.text
            replier = m.from_user.username
            repliee = m.reply_to_message.from_user.username
            chatID = m.chat.id
            if chatID not in activeChats:
                activeChats[chatID] = {}
            userscores = activeChats[chatID]

            if replier == repliee:
                return

            if repliee not in userscores:
                userscores[repliee] = 0

            if text.lower() == "based":
                userscores[repliee] += 1
                bot.reply_to(m, f"@{replier} boosted @{repliee}'s based rating to {userscores[repliee]}")

            elif text.lower() == "cringe":
                userscores[repliee] -= 1
                bot.reply_to(m, f"@{replier} downgraded @{repliee}'s based rating to {userscores[repliee]}")

bot.set_update_listener(listener)

bot.polling()