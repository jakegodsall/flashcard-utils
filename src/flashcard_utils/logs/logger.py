import logging
import sys


def get_logger(name: str = __name__, level: str = "WARNING"):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if len(logger.handlers) == 0:
        handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter(
            fmt="%(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
