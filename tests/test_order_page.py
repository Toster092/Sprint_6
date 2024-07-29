import allure
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from data import Customers
import pytest

class TestOrderPage:
   @pytest.mark.parametrize("order_button, name, surname, address, phone, order_date",
                            [(OrderPageLocators.ORDER_BUTTON, Customers.NAME_1, Customers.SURNAME_1,
                              Customers.ADDRESS_1, Customers.PHONE_1, Customers.ORDER_DATE_1),
                             (OrderPageLocators.ORDER_BUTTON_MIDDLE, Customers.NAME_2, Customers.SURNAME_2,
                              Customers.ADDRESS_2, Customers.PHONE_2, Customers.ORDER_DATE_2)
                            ])
   @allure.title('Проверка успешного заказа')
   def test_order_success(self, driver, order_button, name, surname, address, phone, order_date):
       order_page = OrderPage(driver)
       order_page.click_on_cookie()
       order_page.click_on_element(order_button)
       order_page.fill_order_form(name, surname, address, phone)
       order_page.select_rent_time(order_date)
       result = order_page.confirm_order()
       assert result == 'Посмотреть статус'