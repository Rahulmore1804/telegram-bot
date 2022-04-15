from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import constants as keys
from telegram.ext import *
import responses as rr

print("started")
def start_command(update:Update,context:CallbackContext):
    update.message.reply_text("hello welcome  wiki bot")
    update.message.reply_text("use /search command to get info")
def help_command(update:Update,context:CallbackContext):
    update.message.reply_text("contact @rmore")


def handle_message(update,context):
    text = str(update.message.text).lower()
    r1 = rr.exampleinput(text)
    update.message.reply_text(r1)
def error(update,context):
    print("error")  
def main():
     updater = Updater(keys.API_KEY, use_context=True)
     disp = updater.dispatcher 

     disp.add_handler(CommandHandler("start",start_command))
     disp.add_handler(CommandHandler("help",help_command))
     disp.add_handler(MessageHandler(Filters.text, handle_message))
     disp.add_error_handler(error)

     updater.start_polling()
     updater.idle()

main()


