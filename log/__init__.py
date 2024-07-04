import logging
from .__utils import edit_name

def get_logger(name: str):
    if '.' in name:
        name = edit_name(name)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

logger = get_logger(__name__)
