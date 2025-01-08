from ...__utils import get_handler_text
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def handler(msg: Message, state: FSMContext):
    await state.set_state()
    await msg.answer(text=get_handler_text(__file__))
