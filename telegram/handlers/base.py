from inspect import signature
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from log import logger
from .data.objects import router
from .utils import get_command, get_state, get_exception
from .messages.messages import message_handler


@router.message(F.chat.type == "private")
async def main(msg: Message, state: FSMContext):
    try:
        text, args = msg.text, [msg]
        state_data = await state.get_state()
        if text and text.startswith("/"):
            handler = get_command(text.split()[0][1:])
        elif text and state_data is not None:
            handler = get_state(state_data)
        else:
            handler = message_handler
    except BaseException as err:
        handler = get_exception(err)

    if "state" in signature(handler).parameters:
        args.append(state)
    await handler(*args)
