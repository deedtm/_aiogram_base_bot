from .utils import get_username
from .config import templates
from log import logger
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text=templates["start"])


@router.message()
async def photo_handler(msg: Message):
    username = get_username(msg.from_user)
    logger.info(msg=f'Got message from {username}')
    
    if msg.text:
        await msg.answer(templates['text'].format(text=msg.text))
        return
    
    kwargs = {"type": msg.content_type.lower()}
    if msg.caption:
        text = ' '.join(templates['media'])
        kwargs.setdefault("caption", msg.caption)
    else:
        text = templates['media'][0]
    
    await msg.answer(text.format(**kwargs))
    