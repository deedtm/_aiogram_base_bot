from .exceptions import CommandDoesNotExist, StateDoesNotExist, ExceptionDoesNotExist
from .__utils import get_function
from . import global_variables


def get_command(command: str):
    vars = global_variables.get()
    try:
        if command in vars:
            module = vars[command]
            return module.messages.handler
    except AttributeError as err:
        pass
    raise CommandDoesNotExist(command)


def get_state(state_data: str):
    vars = global_variables.get()
    response, data = state_data.split(":")[1:3]
    try:
        if response in vars:
            module = vars[response].states
            return get_function(module, "state", data)
    except AttributeError as err:
        pass
    raise StateDoesNotExist(response)


def get_exception(err: BaseException):
    vars = global_variables.get()
    class_name = err.__class__.__name__.lower()
    try:
        if class_name in vars:
            module = vars[class_name]
            return module.handler
    except AttributeError as err:
        pass
    raise ExceptionDoesNotExist(class_name)
