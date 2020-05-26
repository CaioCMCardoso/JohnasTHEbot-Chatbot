from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = 'Falai,' + update.message.from_user.first_name + ', meu bom chapa!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def feedback(update, context):
    message = '''e ai meu chapa, bão ou não?\n
        1 - Bão demais\n
        2 - Não muito bão'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
    return STATE1

def inputFeedback(update, context):
    feedback = (update.message.text).lower()
    print(feedback)
    if (feedback == '1' or feedback =='bão' or feedback=='sim' or feedback=='bao' or feedback == 'tudo certo' or feedback =='tudo'):
        message = "Bão demais então"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (feedback == '2' or feedback == 'nao'):
        message = "Não fica na bad, tem que ficar suave"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2


def inputFeedback2(update, context):
    feedback = update.message.text
    message = '''Ou, vou dar uma saída aqui, mais tarde é noix!\n
            Papai te ama'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

def main ():
    token = '1139982411:AAG5NLF-2XAzn79t-0LbXFNkNDsN13YHa2s'
    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('eae', feedback)],
        states={
            STATE1: [MessageHandler(Filters.text, inputFeedback)],
            STATE2: [MessageHandler(Filters.text, inputFeedback2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    updater.dispatcher.add_handler(conversation_handler)
    updater.start_polling()
    print('Eu sou o Dougras, você não é o dougras' + str(updater))
    updater.idle()

if __name__=="__main__":
    main()