import allure
from pages.base_page import BasePage
from locators.switch_page_locators import SwitchPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class SwitchPage(BasePage):
   @allure.step('Клик на логотип самоката')
   def click_on_scooter(self):
       self.click_on_element(SwitchPageLocators.ORDER_BUTTON)
       self.click_on_element(SwitchPageLocators.SCOOTER_BUTTON)
   @allure.step('Клик на логотип Яндекс')
   def click_on_yandex(self):
       original_window = self.driver.current_window_handle
       self.click_on_element(SwitchPageLocators.YANDEX_BUTTON)
       WebDriverWait(self.driver, 10).until(expected_conditions.new_window_is_opened([original_window]))
       new_window = self.driver.window_handles[-1]
       self.driver.switch_to.window(new_window)
       return self.get_text(SwitchPageLocators.NEWS_BUTTON)