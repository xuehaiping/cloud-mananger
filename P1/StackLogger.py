from Config import LOGGING_FILENAME, LOGGER_NAME

import logging


def createLogger():
    """
    Create a logger
    """
    # initiate the logger
    logger = logging.getLogger(LOGGER_NAME)
    hdlr = logging.FileHandler(LOGGING_FILENAME)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    return logger

