import asyncio
import logging
from log.utils import disable_loggers
from telegram.handlers import router
from telegram import TelegramBot
from config import token


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    disable_loggers('aiogram')
    
    bot = TelegramBot(token, router)
    asyncio.run(bot.start())
    