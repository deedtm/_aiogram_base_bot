from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ...states_group import Wait
from ...__data.constants import TEMPLATES
from ...__utils import get_handler_text
from ...keyboards import reply_button


async def handler(msg: Message, state: FSMContext):
    me = await msg.bot.me()
    mkp_data = [
        value for value in [
            me.id,
            me.username,
            me.first_name,
            me.last_name,
            me.full_name,
            me.language_code,
            me.url,
        ] if value is not None
    ]
    await msg.answer(
        text=get_handler_text(__file__), reply_markup=reply_button.mkp(mkp_data)
    )
    await state.update_data({"mkp_data": mkp_data})
    await state.set_state(Wait.reply_button)
