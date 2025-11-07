from django.core.management import BaseCommand

from data.tg_bot.main import Bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Bot ishladi!")
        bot = Bot()
        bot.run()