import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
   @allure.step('Клик на согласие с куки')
   def click_on_cookie(self):
       self.click_on_element(OrderPageLocators.COOKIE_LOC)
   @allure.step('Заполнение инпутов данными')
   def fill_order_form(self, name, surname, address, phone,):
       self.input_text(OrderPageLocators.NAME_INPUT, name)
       self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
       self.input_text(OrderPageLocators.ADRESS_INPUT, address)
       self.click_on_element(OrderPageLocators.STATION_INPUT)
       self.click_on_element(OrderPageLocators.STATION_1)
       self.input_text(OrderPageLocators.PHONE_INPUT, phone)
       self.click_on_element(OrderPageLocators.CONTINUE_BUTTON)
   @allure.step('Выбор срока аренды')
   def select_rent_time(self, date):
       self.input_text(OrderPageLocators.DATE_INPUT, date)
       self.click_on_element(OrderPageLocators.RENT_TIME_INPUT)
       self.click_on_element(OrderPageLocators.RENT_TIME_BUTTON)
       self.click_on_element(OrderPageLocators.ORDER_BUTTON_MIDDLE)
   @allure.step('Подтверждение заказа')
   def confirm_order(self):
       self.click_on_element(OrderPageLocators.YES_BUTTON)
       self.find_element_located(OrderPageLocators.STATUS_BUTTON)
       return self.get_text(OrderPageLocators.STATUS_BUTTON)