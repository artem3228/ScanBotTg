import settings
from telegram.ext import *
import Responses
from Trie import Trie


# Start command
def start_command(update, context):
    update.message.reply_text('Enter email to find out if you are compromised')


# Prints if there was an error
def Error(update, context):
    print(f"{update} caused error {context.error}")


class Bot:
    db = Trie()

    # Check command check {something}
    def check_command(self, update, text1):
        if len(text1) != 2:
            update.message.reply_text("For check format is check {email}!")
            return
        status = self.db.check(text1[1])
        if status:
            update.message.reply_text("The user was found in the database")
        else:
            update.message.reply_text("The user wasn't found in the database")

    # add command add {something}
    def add_command(self, update, text1):
        if len(text1) != 2:
            update.message.reply_text("For add format is add {format}!")
            return
        self.db.add(text1[1])
        update.message.reply_text("Success!")

    def handle_message(self, update, context):
        text = str(update.message.text).lower()
        text1 = text.split()
        if text1[0] == "check":
            self.check_command(update, text1)
        elif text1[0] == "add":
            self.add_command(update, text1)
        else:
            response = Responses.sample_responses(text)
            update.message.reply_text(response)

    # starting the bot
    def Core(self):
        updater = Updater(settings.API_KEY, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(MessageHandler(Filters.text, self.handle_message))
        dp.add_error_handler(Error)

        updater.start_polling()
        updater.idle()

    # Load from the file function
    def Load_from_file(self):
        for fn in settings.BASES:
            f = open(fn, "r")
            for line in f:
                if line[len(line) - 1] == '\n':  # if the last character is a '\n' delete this character
                    line = line[:(len(line) - 1)]
                line = line.lower()
                self.db.add(line)

    def __init__(self):
        self.Load_from_file()
        print("The bot has been started")


if __name__ == '__main__':
    bot = Bot()
    bot.Core()
