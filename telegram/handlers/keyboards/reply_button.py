from . import build
from random import choice


def do_smth_with_data(data: list):
    indices_to_remove = set()
    while len(indices_to_remove) < len(data) - 1 and choice([True, False]):
        indices_to_remove.add(choice(range(len(data))))
    d = [item for idx, item in enumerate(data) if idx not in indices_to_remove]
    return d


def mkp(data: list):
    data = do_smth_with_data(data)
    return build(data)
