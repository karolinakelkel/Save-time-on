import os
import logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    filename='logs/app.log',
    filemode='a'
)

logger = logging.getLogger("save_time_on")
