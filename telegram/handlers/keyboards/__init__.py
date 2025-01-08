from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton
from typing import Iterable, Union


def add_dict_items(builder, button_cls, items):
    for text, params in items.items():
        builder.add(button_cls(text=str(text), **params))


def add_iterable_items(builder, button_cls, items):
    for text in items:
        builder.add(button_cls(text=str(text)))


def build(items: Union[Iterable, dict], is_inline: bool = False, rows_amount: int = 3):
    builder = InlineKeyboardBuilder() if is_inline else ReplyKeyboardBuilder()
    button_cls = InlineKeyboardButton if is_inline else KeyboardButton

    if isinstance(items, dict):
        add_dict_items(builder, button_cls, items)
    else:
        add_iterable_items(builder, button_cls, items)

    builder.adjust(rows_amount)
    return builder.as_markup()
