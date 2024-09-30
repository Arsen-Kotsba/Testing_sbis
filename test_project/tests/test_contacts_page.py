import pytest
from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.contacts_page import ContactsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_check_city_tag_and_contacts_list(driver):
    # Открытие главной страницы и переход в раздел "Контакты"
    home_page = HomePage(driver)
    home_page.load()
    home_page.click_contacts_banner()
    home_page.click_more_offices_link()

    # Проверка наличия тега с текстом "Карачаево-Черкесская Республика" и клик по ссылке
    contacts_page = ContactsPage(driver)
    city_tag = contacts_page.check_city_tag()
    contacts_page.click_city_tag()

    # Проверка блока с контактами (адреса, телефоны, email)
    contacts_list = contacts_page.check_contacts_list()

    # Ожидание всплывающего окна и выбор региона "Камчатский край"
    contacts_page.select_region_kamchatka()

    # Логирование успешного выполнения
    assert city_tag is not None, "Тег с текстом 'Карачаево-Черкесская Республика' не найден"
    assert contacts_list is not None, "Блок с контактами не найден"
