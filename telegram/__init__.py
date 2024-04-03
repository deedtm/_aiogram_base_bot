from log import logger
from .dispatcher import BotDispatcher
from aiogram import Bot, Router
from aiogram.enums.parse_mode import ParseMode

class TelegramBot(Bot):
    def __init__(self, token: str, router: Router, parse_mode: ParseMode = ParseMode.HTML):
        super().__init__(token, parse_mode=parse_mode)
        self.dp = BotDispatcher(router)
    
    async def start(self):
        logger.info(f'Starting {self.__class__.__name__}... (~3 sec)') 
        
        await self.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self, allowed_updates=self.dp.resolve_used_update_types())
        