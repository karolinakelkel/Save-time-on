import os
import logging

os.makedirs('logs', exist_ok=True)

logger = logging.getLogger('save_time_on')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

file_handler = logging.FileHandler('logs/app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
