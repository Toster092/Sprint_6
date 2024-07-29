from selenium.webdriver.common.by import By

class MainPageLocators:
   QUESTION_LOC = By.XPATH, "//div[@id='accordion__heading-{num}']"
   ANSWER_LOC = By.XPATH, "//div[@id='accordion__panel-{num}']"
   LAST_QUESTION_LOC = By.XPATH, "//div[@id='accordion__heading-6']"
   COOKIE_LOC = By.XPATH, "//button[@id='rcc-confirm-button']"
