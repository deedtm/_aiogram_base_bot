from types import ModuleType


def get_function(module: ModuleType, name: str, data: str):
    function_name = f"{name}_{data}"
    return module.__dict__[function_name]
