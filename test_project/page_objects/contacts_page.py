from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


class ContactsPage:
    def __init__(self, driver):
        self.driver = driver
        logger.info("Инициализация ContactsPage с драйвером")

    # Метод для нахождения и клика по баннеру "Тензор"
    def click_tensor_banner(self):
        logger.info("Ожидание баннера 'Тензор'")
        # Поиск баннера и клик
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                                (By.CSS_SELECTOR, "#contacts_clients > div.sbis_ru-container > div > "
                                                                  "div > div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 "
                                                                  "> div > a")))
        logger.info("Баннер 'Тензор' найден")
        tensor_banner = self.driver.find_element(By.CSS_SELECTOR, "#contacts_clients > div.sbis_ru-container > div > "
                                                                  "div > div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 "
                                                                  "> div > a")
        tensor_banner.click()
        logger.info("Клик по баннеру 'Тензор' выполнен")

        # Проверяем, что ссылка ведет на "tensor.ru"
        href = tensor_banner.get_attribute("href")
        logger.info(f"Проверка ссылки на баннере 'Тензор': {href}")
        assert "tensor.ru" in href, f"Ссылка ведет на {href}, а не на tensor.ru"

        # Переходим на новую вкладку, в которой открылся сайт tensor.ru
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logger.info("Переключение на новую вкладку с 'tensor.ru'")

        WebDriverWait(self.driver, 10).until(EC.url_contains("tensor.ru"))
        logger.info("Успешный переход на сайт tensor.ru")

    # Метод для проверки наличия тега с текстом "Карачаево-Черкесская Республика"
    def check_city_tag(self):
        logger.info("Проверка наличия тега с текстом 'Карачаево-Черкесская Республика'")
        city_tag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text.sbis_ru-link"))
        )
        assert "Карачаево-Черкесская Республика" in city_tag.text, \
            f"Тег не содержит 'Карачаево-Черкесская Республика', текст: {city_tag.text}"
        logger.info(f"Тег найден с текстом: {city_tag.text}")
        return city_tag

    # Метод для поиска блока с контактами
    def check_contacts_list(self):
        logger.info("Поиск блока с контактами (адреса, телефоны, email)")
        contacts_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                    "//*[@id='contacts_list']/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]"))
        )
        logger.info("Блок с контактами найден")
        return contacts_list

    # Метод для клика по ссылке "Карачаево-Черкесская Республика"
    def click_city_tag(self):
        logger.info("Поиск и клик по ссылке 'Карачаево-Черкесская Республика'")
        city_tag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text.sbis_ru-link")))
        assert "Карачаево-Черкесская Республика" in city_tag.text, "Тег не содержит 'Карачаево-Черкесская Республика'"
        city_tag.click()
        logger.info("Клик по ссылке 'Карачаево-Черкесская Республика' выполнен")

    # Метод для выбора региона "41 Камчатский край"
    def select_region_kamchatka(self):
        logger.info("Ожидание всплывающего окна с регионами")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.sbis_ru-Region-Panel__list-l")))

        logger.info("Поиск региона 'Камчатский край'")
        kamchatka_region = self.driver.find_element(By.XPATH, "//span[text()='41 Камчатский край']")
        kamchatka_region.click()
        logger.info("Клик по региону 'Камчатский край' выполнен")

        # Ожидание изменения заголовка вкладки
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Камчатский край")
        )
        assert EC.title_contains("Камчатский край"), f"Заголовок не содержит 'Камчатский край', текущий заголовок: " \
                                                     f"{self.driver.getTitle()}"
        logger.info("Заголовок вкладки содержит 'Камчатский край'")

        # Проверка URL
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("41")  # Проверяем, что в URL содержится число 41
        )
        current_url = self.driver.current_url
        logger.info(f"Текущий URL: {current_url}")
        assert "41" in current_url, f"URL не содержит '41', текущий URL: {current_url}"
