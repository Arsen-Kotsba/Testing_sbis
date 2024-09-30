import pytest
from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.download_page import DownloadPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_download_file(driver):
    # Открытие главной страницы и клик по ссылке "Скачать локальные версии"
    home_page = HomePage(driver)
    home_page.load()
    home_page.click_download_local_versions()

    # Переход на страницу загрузки
    download_page = DownloadPage(driver)
    download_page.click_download_link()
