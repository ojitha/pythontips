import logging
from contextlib import contextmanager

@contextmanager
def debug_logging(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


logging.getLogger().setLevel(logging.WARNING)

def my_function():
    logging.debug('Same debug info')
    logging.error('A real error!')

with debug_logging(logging.DEBUG, 'custom_log') as log:
    my_function()
    log.debug('This has been ran')
