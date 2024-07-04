import asyncio
import logging
from telegram import TelegramBot
from config import token, parse_mode, disable_link_preview
from log.utils import disable_loggers
from aiogram.client.default import DefaultBotProperties
from telegram.handlers.data.objects import router


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    disable_loggers('aiogram')
    
    default = DefaultBotProperties(parse_mode=parse_mode, link_preview_is_disabled=disable_link_preview)
    bot = TelegramBot(token, router, default)
    asyncio.run(bot.start())
    