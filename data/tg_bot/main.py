import os
from idlelib.undo import Command

from telegram.ext import Application, ApplicationBuilder, CommandHandler


class Bot:

    def __init__(self):
        TOKEN = os.environ.get("TOKEN")
        self.app = ApplicationBuilder().token(TOKEN).build()
        self.app.add_handler(CommandHandler('start', self.start))

    def run(self):
        self.app.run_polling()

    async def start(self, update, context):
        user = update.effective_user
        await update.message.reply_text(
            f"Salom {user.full_name}"
        )

