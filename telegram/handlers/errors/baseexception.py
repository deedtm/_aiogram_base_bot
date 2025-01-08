from aiogram.types import Message
from traceback import format_exc
from .log import logger
from ..__data.constants import TEMPLATES


async def handler(msg: Message, err: BaseException):
    err_msg = f"{err.__class__.__name__}:{err.__str__()}"
    logger.error(format_exc())
    
    template = TEMPLATES["error"]
    text = template.format(error=err_msg)
    await msg.answer(text)
    