from Config import LOGGING_FILENAME

import logging
import os.path


def createLogger():
    """
    Create a logger
    """
    # create a log file if not exist
    if not os.path.isfile(LOGGING_FILENAME):
        f = open(LOGGING_FILENAME, "w+")
        f.write("Create log file at %(asctime)s\n")
        f.close()

    # initiate the logger
    logger = logging.getLogger("aggie_stack")
    hdlr = logging.FileHandler(LOGGING_FILENAME)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.WARNING)
    return logger

