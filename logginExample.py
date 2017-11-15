import logging
from contextlib import contextmanager

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


logging.getLogger().setLevel(logging.WARNING)

def my_function():
    logging.debug('Same debug info')
    logging.error('A real error!')

with debug_logging(logging.DEBUG):
    my_function()
