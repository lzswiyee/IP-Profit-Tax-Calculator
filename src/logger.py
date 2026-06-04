import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    return logging.getLogger("tax_calc")

logger = setup_logger()