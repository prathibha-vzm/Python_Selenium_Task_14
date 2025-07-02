#imported all the needed exceptions, web driver wait and other packages
import time
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, TimeoutException, \
    NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#This class all the login page elements
class LoginPage:
    def __init__(self,driver):     #stored the xpath, driver and wait
        self.driver=driver
        self.email_input=(By.XPATH,"//input[@placeholder='Enter your mail']")
        self.password_input=(By.XPATH,"//input[@placeholder='Enter your password ']")
        self.remember_checkbox=(By.XPATH,"//input[@type='checkbox']")
        self.sign_in=(By.XPATH,"//button[@class='primary-btn sign-in-pad']")
        self.wait=WebDriverWait(driver,20)

    #To click on email field, check its visibility , data availability and sending the value. Then added the exception that are expected.
    def email_input(self,email_data):
        email_element=(self.wait.until(expected_conditions.visibility_of_element_located(self.email_input)))
        try:
            if email_element.is_enabled():
                email_element.clear()
                if email_data:
                    email_element.send_keys(email_data)
        except ElementNotInteractableException as ei:
            print("Email Field is not interactable",ei)

    #To click on password field, check its visibility , data availability and sending the value. Then added the exception that are expected.
    def password_input(self,password_data):
        password_element=(self.wait.until(expected_conditions.visibility_of_element_located(self.password_input)))
        try:
            if password_element.is_enabled():
                password_element.clear()
                if password_data:
                    password_element.send_keys(password_data)
        except ElementNotInteractableException as ei:
            print("Password Field is not interactable", ei)

    #To click on remember me -check box, check it is already selected and added exceptions
    def remember_me(self):
        try:
            checkbox = (self.driver.find_element(*self.remember_checkbox))
            if not checkbox.is_selected():
                checkbox.click()
        except TimeoutException as time:
            print("Checkbox not found", time)
        except ElementClickInterceptedException as ec:
            print("Checkbox not clickable",ec)

    #To click on login button and once logged in then close any pop-ups that occurs and added exception
    def login_button(self):
        try:
            sign_in_element = (self.driver.find_element(*self.sign_in))
            if sign_in_element:
                 sign_in_element.click()
                 time.sleep(7)
                 self.driver.find_element(By.XPATH, "//button[@aria-label='Close popup']").click()

        except NoSuchElementException:
            print("Element not found")




















