import threading
import logging.config
from concurrent_log_handler import ConcurrentRotatingFileHandler
# import ConcurrentRotatingFileHandler
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__file__)


i = 0
def startObj():
    timer = threading.Timer(5, startObj)
    timer.start()
    global i
    i += 1
    print(i)
    logger.info(i)


if __name__ == "__main__":
    startObj()
    print("app start")