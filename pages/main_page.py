import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
class MainPage(BasePage):
   @allure.step('Клик на вопрос и получение ответа')
   def click_on_question_and_get_answer(self, num):
       self.scroll_to_element_located(MainPageLocators.LAST_QUESTION_LOC)
       self.click_on_cookie(MainPageLocators.COOKIE_LOC)
       question_form_loc = self.format_locator(MainPageLocators.QUESTION_LOC, num)
       self.click_on_element(question_form_loc)
       answer_form_loc = self.format_locator(MainPageLocators.ANSWER_LOC, num)
       return self.get_text(answer_form_loc)