
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext
)

from HowFarBot import *
from HowFarBot.config import PARSE_MODE

class bot:
    """All bot reactions"""
    
    def start(update: Update, context: CallbackContext):
            """Handles the start command"""
            user = update.effective_user
            update.effective_message.reply_text(
                f'Hi! <b>{user.first_name}</b>! \n' +
                'This bot uses your telegram location to '+
                'determine the distance between you and a place of your coice. '+
                'by using this bot, you agree to temporary storage and processing of your location.\n \n'+
                'To get started, simply send the desired location. f.e.: "Seattle"',
                parse_mode=PARSE_MODE
            )
            return
    dispatcher.add_handler(CommandHandler("start", start, run_async=True))


