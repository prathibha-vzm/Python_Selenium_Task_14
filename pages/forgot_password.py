#Importing Exceptions , wait, time and webdriver by to use xpath
import time
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# This class is to check the forgot password link
class ResetPassword:
    def __init__(self,driver):
        self.driver=driver
    #This page click on forgot password link and enter email and submit
    def forget_password(self,email):
        wait = WebDriverWait(self.driver, 10)
        try:
            forgot_link = wait.until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "//div[contains(text(),'Forgot Password?')]")))
            forgot_link.click()
            web_page_url = self.driver.current_url
            time.sleep(5)
            email_input = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2']")))
            email_input.send_keys(email)
            time.sleep(5)
            submit = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            "//button[@type='submit']")))
            submit.click()
            try:   # When the valid email given this statement executes
                success = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//div[@class='email-success-text']")))
                success_text = success.text
                self.driver.save_screenshot(
                    "C:/Users/91956/PycharmProjects/PythonProject5/POM/reports/reset_pwd_success.png")
                print(success_text)
                return web_page_url, success_text
            except TimeoutException:    #IF not valid this will execute
                error_message=wait.until(EC.visibility_of_element_located((By.XPATH,"//p[@id=':r2:-helper-text']")))

                print(error_message.text)
                return web_page_url,error_message.text

        except (NoSuchElementException,TimeoutException):
            print("Element not found")




