from aiogram import F
from aiogram.types import CallbackQuery
from ...__utils import get_handler_name
from ...__data.objects import router
from ...__data.constants import TEMPLATES


@router.callback_query(F.data.startswith(f"{get_handler_name(__file__)}:response"))
async def response_handler(q: CallbackQuery):
    tk1, tk2, data, value = q.data.split(":", 3)
    template = TEMPLATES[tk1 + ":" + tk2]
    text = template.format(data=data.lower(), value=value)
    await q.message.edit_text(text, reply_markup=q.message.reply_markup)
    