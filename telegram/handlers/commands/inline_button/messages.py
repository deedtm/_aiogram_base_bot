from ...__utils import get_handler_name
from ...__data.constants import TEMPLATES
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ...keyboards import inline_button


async def handler(msg: Message, state: FSMContext):
    handler_name = get_handler_name(__file__)
    me = msg.from_user
    cb = "{}:response:{}:{}"
    mkp_data = {
        key: {"callback_data": cb.format(handler_name, key, value)}
        for key, value in {
            "ID": me.id,
            "Username": me.username,
            "First name": me.first_name,
            "Last name": me.last_name,
            "Full name": me.full_name,
            "Language code": me.language_code,
            "URL": me.url,
        }.items()
        if value is not None
    }
    await msg.answer(
        text=TEMPLATES[handler_name], reply_markup=inline_button.mkp(mkp_data)
    )
