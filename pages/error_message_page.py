from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Error:
    def __init__(self,driver):
        self.driver=driver
        self.error_locator=(By.XPATH, "//p[@id=':r0:-helper-text']")
        self.wait=WebDriverWait(driver,10)
    def error_text(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.error_locator))
            print("Invalid Credentials")
        except (NoSuchElementException,TimeoutException):
            print("Valid Credentials")
