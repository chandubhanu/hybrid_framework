import logging
import os

class LogGen:
    @staticmethod
    def loggen(delete_existing=False):
        os.makedirs(".\\Logs", exist_ok=True)
        log_file = os.path.abspath(".\\Logs\\automation.log")

        # 🧹 Delete existing log file if requested
        if delete_existing and os.path.exists(log_file):
            os.remove(log_file)

        logger = logging.getLogger("nopCommerceLogger")
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, mode='a')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
