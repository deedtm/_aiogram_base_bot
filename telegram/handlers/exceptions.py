class HandlerException(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DoesNotExistException(HandlerException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class CommandDoesNotExist(DoesNotExistException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class StateDoesNotExist(DoesNotExistException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ExceptionDoesNotExist(DoesNotExistException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        