from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        logger.info("Инициализация TensorPage с драйвером")

    # Метод для нахождения блока "Сила в людях"
    def find_sila_v_lyudyah_block(self):
        logger.info("Поиск блока 'Сила в людях'")
        sila_v_lyudyah_block = self.driver.find_element(By.CSS_SELECTOR, "#container > div.tensor_ru-content_wrapper > div > "
                                                         "div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1)"
                                                         " > div > p.tensor_ru-Index__card-title.tensor_ru-pb-16")
        logger.info("Блок 'Сила в людях' найден")
        return sila_v_lyudyah_block

    # Метод для клика по ссылке "Подробнее" в блоке "Сила в людях"
    def click_more_link(self):
        logger.info("Ожидание ссылки 'Подробнее'")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#container > div.tensor_ru-content_wrapper > div > "
                                                               "div.tensor_ru-Index__block4-bg > div > div > "
                                                               "div:nth-child(1) > div > p:nth-child(4) > a"))
        )

        more_link = self.driver.find_element(By.CSS_SELECTOR, "#container > div.tensor_ru-content_wrapper > div > "
                                                              "div.tensor_ru-Index__block4-bg > div > div > "
                                                              "div:nth-child(1) > div > p:nth-child(4) > a")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", more_link)
        logger.info("Ссылка 'Подробнее' найдена, выполняется клик")
        more_link.click()
        logger.info("Клик по ссылке 'Подробнее' выполнен")

        # Проверка, что открылась страница с адресом "https://tensor.ru/about"
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://tensor.ru/about"))
        assert "https://tensor.ru/about" in self.driver.current_url, \
            f"Ожидалась страница https://tensor.ru/about, но открылась {self.driver.current_url}"
        logger.info("Переход на страницу 'https://tensor.ru/about' успешен")

    # Метод для проверки размеров изображений в разделе "Работаем"
    def check_images_in_rabotaem_section(self):
        logger.info("Начало проверки изображений в разделе 'Работаем'")
        # Поиск всех изображений в разделе "Работаем"
        images = self.driver.find_elements(By.CSS_SELECTOR, "div.tensor_ru-About__block3 img")
        logger.info(f"Найдено {len(images)} изображений в разделе 'Работаем'")

        # Получение высоты и ширины первой картинки для сравнения
        first_image = images[0]
        first_image_width = first_image.get_attribute("width")
        first_image_height = first_image.get_attribute("height")
        logger.info(f"Первая картинка - ширина: {first_image_width}, высота: {first_image_height}")

        # Проверка, что все остальные изображения имеют такие же размеры
        for image in images:
            assert image.get_attribute("width") == first_image_width, f"Ширина изображения {image} отличается"
            assert image.get_attribute("height") == first_image_height, f"Высота изображения {image} отличается"

            # Логируем проверенные изображения
            logger.info(f"Изображение {image} - ширина: {image.get_attribute('width')}, "
                        f"высота: {image.get_attribute('height')}")

        logger.info("Все изображения в разделе 'Работаем' имеют одинаковые размеры")
