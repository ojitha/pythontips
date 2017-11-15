from contextlib import contextmanager
import logging

@contextmanager
def my_exception(cls):
    try:
        yield
    except cls:
        logging.exception("my Exception")

v = 10
with my_exception(ZeroDivisionError):
    v /=0        
