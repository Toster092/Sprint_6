from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
   def __init__(self, driver):
       self.driver = driver
   def go_to_site(self, URL):
       return self.driver.get(URL)
   def find_element_located(self, locator, time=10):
       return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))
   def find_elements_located(self, locator, time=10):
       return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator))
   def scroll_to_element_located(self, locator):
       element = self.find_element_located(locator)
       self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
   def click_on_element(self, locator):
       return self.find_element_located(locator).click()
   def click_on_cookie(self, locator):
       self.find_element_located(locator).click()
   def get_text(self, locator):
       return self.find_element_located(locator).text
   def format_locator(self, locator, num):
       method, loc = locator
       formatted_loc = loc.format(num=num)
       return (method, formatted_loc)
   def input_text(self, locator, text):
       element = self.find_element_located(locator)
       element.send_keys(text)
