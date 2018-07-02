import logging


def setup_logging(log_file):
    logging_format = "%(asctime)s;%(levelname)s;%(message)s"
    logger = logging.getLogger("trafficking")
    hdlr = logging.FileHandler(log_file, mode="a")
    formatter = logging.Formatter(logging_format, datefmt="%Y-%m-%d %H:%M:%S")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logging("/var/log/alerts.log")
