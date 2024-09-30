import pytest
from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.contacts_page import ContactsPage
from page_objects.tensor_page import TensorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_click_more_in_sila_v_lyudyah(driver):
    # Открытие главной страницы и клик по баннеру "Контакты"
    home_page = HomePage(driver)
    home_page.load()
    home_page.click_contacts_banner()

    # Клик по ссылке "Еще 231 офис в России" во всплывающем окне
    home_page.click_more_offices_link()

    # Переход на страницу контактов и клик по баннеру "Тензор"
    contacts_page = ContactsPage(driver)
    contacts_page.click_tensor_banner()

    # Переход на сайт tensor.ru, поиск блока "Сила в людях" и клик по ссылке "Подробнее"
    tensor_page = TensorPage(driver)
    tensor_page.find_sila_v_lyudyah_block()
    tensor_page.click_more_link()

    # Проверка размеров изображений в разделе "Работаем"
    tensor_page.check_images_in_rabotaem_section()
