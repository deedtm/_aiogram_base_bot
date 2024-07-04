from aiogram.types import Message
from ...data.constants import TEMPLATES

async def handler(msg: Message):
    await msg.answer(text=TEMPLATES["start"])
    