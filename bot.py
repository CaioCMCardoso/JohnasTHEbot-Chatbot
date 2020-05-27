from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2
STATE3 = 3
STATE4 = 4
STATE5 = 5
STATE6 = 6
STATE7 = 7

def welcome(update, context):
    message = 'Wazzap,' + update.message.from_user.first_name + ', my dude!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return STATE1
    
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
        return STATE3
    elif (feedback == '2' or feedback == 'nao' or feedback == 'não'):
        message = "Não fica na bad, tem que ficar suave"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE5


def inputFeedback2(update, context):
    feedback = update.message.text
    message = '''Bom, eu vou ter que dar uma saída, mas se precisar, só chamar ai, vlw flw'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return STATE7

def feedback2(update, context):
    message = '''Top show boladão, ta afim de trocar ideias?\n
                    1 - sim\n
                    2 - não'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
    return STATE4

def feedback3(update, context):
    message = '''Poxa, que triste, cê precisa trocar uma ideia?\n
                    1 - sim\n
                    2 - não'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
    return STATE6

def inputFeedback3(update, context):
    feedback = (update.message.text).lower()
    print(feedback)
    if (feedback == '1' or feedback =='quero' or feedback=='sim' or feedback=='bora' or feedback == 'demais' or feedback =='na hora'):
        message = "Que vergonha, seus pais sabem que tu é drogado na net?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (feedback == '2' or feedback == 'nao'):
        message = "Oxe, que careta, não vou conversar com gente careta..."
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2

def inputFeedback4(update, context):
    feedback = (update.message.text).lower()
    print(feedback)
    if (feedback == '1' or feedback =='quero' or feedback=='sim' or feedback=='bora' or feedback == 'demais' or feedback =='na hora'):
        message = 'Olha, eu não sou psicólogo, cê devia procurar alguém que não é um robô kakaka'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (feedback == '2' or feedback == 'nao'):
        message = "Ah, então ta bom então!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
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
            STATE2: [MessageHandler(Filters.text, inputFeedback2)],
            STATE3: [MessageHandler(Filters.text, feedback2)],
            STATE4: [MessageHandler(Filters.text, inputFeedback3)],
            STATE5: [MessageHandler(Filters.text, feedback3)],
            STATE6: [MessageHandler(Filters.text, inputFeedback4)],
            STATE7: [CommandHandler('eae', feedback)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    updater.dispatcher.add_handler(conversation_handler)
    updater.start_polling()
    print('Eu sou o Dougras, você não é o dougras' + str(updater))
    updater.idle()

if __name__=="__main__":
    main()
