from selenium.webdriver.common.by import By

class SwitchPageLocators:
   SCOOTER_BUTTON = By.XPATH, "//img[@src='/assets/scooter.svg']"
   YANDEX_BUTTON = By.XPATH, "//img[@src='/assets/ya.svg']"
   NEWS_BUTTON = By.XPATH, "//div[contains(text(),'Новости')]"
   ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g']"