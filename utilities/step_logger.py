import logging
from functools import wraps


def log_step(description):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            class_name = args[0].__class__.__name__

            logging.info(f"[STEP] {class_name} → {description}")

            return func(*args, **kwargs)

        return wrapper

    return decorator