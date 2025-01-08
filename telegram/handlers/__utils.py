from types import ModuleType
from typing import Optional
from utils import get_dirname
from .__data.constants import TEMPLATES
from .states_group import Wait


def get_function(module: ModuleType, name: str, data: str):
    function_name = f"{name}_{data}"
    return module.__dict__[function_name]


def get_handler_name(path: str, state_name: Optional[str] = None):
    if state_name is None:
        return get_dirname(path)
    return state_name.removeprefix(f"{Wait.__name__}:")


def get_handler_text(path: str, state_name: Optional[str] = None):
    return TEMPLATES[get_handler_name(path, state_name)]
