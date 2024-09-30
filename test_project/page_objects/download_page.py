from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import os
import time


class DownloadPage:
    def __init__(self, driver):
        self.driver = driver
        logger.info("Инициализация DownloadPage с драйвером")

    # Метод для клика по ссылке для загрузки
    def click_download_link(self):
        logger.info("Поиск ссылки для загрузки")
        download_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"a.sbis_ru-DownloadNew-loadLink__link.js-link"))
        )
        download_link.click()
        logger.info("Клик по ссылке для загрузки выполнен")
