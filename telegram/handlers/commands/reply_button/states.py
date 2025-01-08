from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ...__data.constants import TEMPLATES
from ...__utils import get_handler_text
from ...keyboards import reply_button


async def state_response(msg: Message, state: FSMContext):
    state_name = await state.get_state()
    state_data = await state.get_data()
    await msg.answer(
        text=get_handler_text(__file__, state_name),
        reply_markup=reply_button.mkp(state_data["mkp_data"]),
    )
    # await state.set_state()
