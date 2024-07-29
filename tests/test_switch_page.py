import allure
from pages.switch_page import SwitchPage
class TestSwitchPage:
   @allure.title('Проверка перехода по клику на лого скутера')
   def test_click_on_scooter(self, driver):
       switch_page = SwitchPage(driver)
       switch_page.click_on_scooter()
       assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
   @allure.title('Проверка перехода по клику на лого Яндекс')
   def test_click_on_yandex(self, driver):
       switch_page = SwitchPage(driver)
       result = switch_page.click_on_yandex()
       assert result == 'Новости'
