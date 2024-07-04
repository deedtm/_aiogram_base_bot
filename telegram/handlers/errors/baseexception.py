from aiogram.types import Message
from .log import logger
from ..data.constants import TEMPLATES


async def handler(msg: Message, err: BaseException):
    err_msg = f"{err.__class__.__name__}:{err.__str__()}"
    logger.error(err_msg)
    
    template = TEMPLATES["error"]
    text = template.format(error=err_msg)
    await msg.answer(text)
    