import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import inspect

@pytest.mark.usefixtures("setup")
class BaseClass:
    scroll = ["window.scrollTo(0, document.body.scrollHeight / 2);", "window.scrollTo(0, 0);"
              "window.scrollTo(0, document.body.scrollHeight);","window.scrollTo(0, 0);"]

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger
