from loguru import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture
def driver():
    # Настройка загрузки в папку
    download_dir = r"C:\Users\user\Desktop\TestingSbis\test_project\tests"
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--safebrowsing-disable-download-protection")
    chrome_options.add_argument("--allow-running-insecure-content")

    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


# Создаем директорию для логов, если её нет
if not os.path.exists('reports/logs'):
    os.makedirs('reports/logs')

# Настройка сохранения логов в файл
logger.add("reports/logs/test_log_{time}.log",
           format="{time} {level} {message}",
           level="INFO",
           rotation="1 day",  # Архивирование по дням
           compression="zip")  # Сжатие старых логов
