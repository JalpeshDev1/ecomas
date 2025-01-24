import logging
import os
def setup_logger(log_file='app.log', log_level=logging.DEBUG):
    logger = logging.getLogger('my_logger')
    logger.setLevel(log_level)

    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - Line: %(lineno)d - %(message)s') 
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger