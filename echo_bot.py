#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dotenv import load_dotenv
load_dotenv()

# Enable logging
from greeceficator import greeceficator_vowels, greeceficator_consonants, greeceficator_english

logging.basicConfig(
    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет! Напиши мне что-нибудь, а я переведу 😉\nHi! Write me something and I will translate it 😉')


def help(update, context):
    """Send a message when the command /help is issued."""
    text = (
        "Commands:\n"
        "/help - this message\n"
        "/caps <текст> - make all caps\n"
        "/lower <текст> - make all lower\n"
    )
    update.message.reply_text(text)


def echo(update, context):
    """Echo the user message."""
    text = update.message.text
    logger.info(text)
    text = greeceficator_consonants(text)
    text = greeceficator_vowels(text)
    update.message.reply_text(text)


def caps(update, context):
    """Echo the user message."""
    text = update.message.text
    logger.info(text)
    text = greeceficator_consonants(text)
    text = greeceficator_vowels(text)
    update.message.reply_text(text.upper())


def lower(update, context):
    """Echo the user message."""
    text = update.message.text
    logger.info(text)
    text = greeceficator_consonants(text)
    text = greeceficator_vowels(text)
    text = greeceficator_english(text)
    update.message.reply_text(text.lower())


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.getenv("BOT_TOKEN"), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("caps", caps))
    dp.add_handler(CommandHandler("lower", lower))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)
    logger.warning('Bot started')

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()