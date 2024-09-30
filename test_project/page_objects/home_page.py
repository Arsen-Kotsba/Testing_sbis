from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        logger.info("Инициализация HomePage с драйвером")
        self.url = "https://sbis.ru/"

    # Открытие главной страницы
    def load(self):
        logger.info("Открытие главной страницы https://sbis.ru/")
        self.driver.get(self.url)
        logger.info("Главная страница загружена")

    # Клик по баннеру "Контакты"
    def click_contacts_banner(self):
        logger.info("Поиск кнопки 'Контакты'")
        contacts_banner = self.driver.find_element(By.XPATH, "//div[contains(@class, 'sbisru-Header__menu-link') and "
                                                             "text()='Контакты']")
        logger.info("Кнопка 'Контакты' найдена, выполняется клик")
        contacts_banner.click()
        logger.info("Клик по кнопке 'Контакты' выполнен")

    # Ожидание всплывающего окна и клик по ссылке "Еще 231 офис в России"
    def click_more_offices_link(self):
        logger.info("Поиск и клик по ссылке")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/contacts']"))
        )
        more_offices_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/contacts']")
        logger.info("Сылка 'Еще 231 офис в России' найдена, выполняется клик")
        more_offices_link.click()
        logger.info("Клик по ссылке 'Еще 231 офис в России' выполнен")

    # Метод для клика по ссылке "Скачать локальные версии"
    def click_download_local_versions(self):
        logger.info("Поиск ссылки 'Скачать локальные версии' в футере")
        download_link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Скачать локальные версии')]")
        logger.info("Ссылка 'Скачать локальные версии' найдена, выполняется клик")
        download_link.click()
        logger.info("Клик по ссылке 'Скачать локальные версии' выполнен")
