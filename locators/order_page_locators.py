from selenium.webdriver.common.by import By

class OrderPageLocators:
   COOKIE_LOC = By.XPATH, "//button[@id='rcc-confirm-button']"
   ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g']"
   ORDER_BUTTON_MIDDLE = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
   NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
   SURNAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
   ADRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
   STATION_INPUT = By.XPATH, "//input[@placeholder='* Станция метро']"
   STATION_1 = By.XPATH, ".//div[text()='Черкизовская']"
   PHONE_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
   CONTINUE_BUTTON = By.XPATH, "//button[contains(text(),'Далее')]"
   ORDER_TITLE = By.XPATH, "//div[@class='Order_Header__BZXOb']"
   DATE_INPUT = By.XPATH, "//div[@class='react-datepicker__input-container']//input[@type='text']"
   RENT_TIME_INPUT = By.XPATH, "//span[@class='Dropdown-arrow']"
   RENT_TIME_BUTTON = By.XPATH, "//div[contains(text(),'сутки')]"
   YES_BUTTON = By.XPATH, "//button[contains(text(),'Да')]"
   STATUS_BUTTON = By.XPATH, "//button[contains(text(),'Посмотреть статус')]"