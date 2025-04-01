import logging
import sys
# ✅ Loglarni faylga va konsolga yozish uchun sozlaymiz
from config import LOG_FILE

# ✅ Log sozlamalari
def loggers(log_name):
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s:%(lineno)d) - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  # Faylga yozish
        logging.StreamHandler(sys.stdout)  # Konsolga chiqarish
    ])
    logger = logging.getLogger(log_name)
    return logger
