from aiogram.fsm.state import State, StatesGroup


class Wait(StatesGroup):
    reply_button = State("reply_button:response")