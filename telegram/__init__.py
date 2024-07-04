from log import get_logger
from .dispatcher import BotDispatcher
from aiogram import Bot, Router
from aiogram.client.default import DefaultBotProperties
from .handlers import base


class TelegramBot(Bot):
    def __init__(self, token: str, router: Router, default_bot_properties: DefaultBotProperties = DefaultBotProperties()):
        super().__init__(token, default=default_bot_properties)
        self.dp = BotDispatcher(router)
        self.logger = get_logger(__name__)
    
    async def start(self):
        self.logger.info(f'Starting {self.__class__.__name__}... (~3 sec)') 
        
        await self.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self, allowed_updates=self.dp.resolve_used_update_types())
        