from aiogram.types import Message
from .log import logger
from ..data.constants import TEMPLATES
from ...utils import get_username


async def message_handler(msg: Message):
    username = get_username(msg.from_user)
    logger.info(msg=f'Got message from {username}')
    
    if msg.text:
        await msg.answer(TEMPLATES['text'].format(text=msg.text))
        return
    
    kwargs = {"type": msg.content_type.lower()}
    if msg.caption:
        text = ' '.join(TEMPLATES['media'])
        kwargs.setdefault("caption", msg.caption)
    else:
        text = TEMPLATES['media'][0]
    
    await msg.answer(text.format(**kwargs))
    