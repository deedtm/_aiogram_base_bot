from aiogram.types import Message
from ...__data.constants import TEMPLATES
from ...__utils import get_handler_text


async def handler(msg: Message):
    await msg.answer(text=get_handler_text(__file__))
    