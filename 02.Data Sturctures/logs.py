import logging
import logging.config
import traceback
from logging.handlers import RotatingFileHandler
# logging.config.fileConfig("logging.conf")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S"
    )


# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

logger = logging.getLogger(__name__)
#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("File.log")

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s-%(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("This is an error")

logger.debug("this is a debug message")

# try:
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error("The error is %s", traceback.format_exc())

logger.setLevel(logging.INFO)

#roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount = 5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello")

import time
from logging.handlers import TimedRotatingFileHandler
handler = TimedRotatingFileHandler("timed_test.log", when='s',interval=5, backupCount = 5)
logger.addHandler(handler)
for _ in range(6):
    logger.info("Hello")
    time.sleep(5)