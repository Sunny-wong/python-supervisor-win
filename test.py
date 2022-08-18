# -*- coding: utf-8 -*-

import time
import logging
import logging.config
from concurrent_log_handler import ConcurrentRotatingFileHandler

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__file__)

def test():
    i = 1
    while True:
        print(f'{i}')
        logger.error(i)
        i += 1
        time.sleep(5)

if __name__ == '__main__':
    test()