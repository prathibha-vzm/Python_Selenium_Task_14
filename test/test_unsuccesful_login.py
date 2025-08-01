import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
#importing all the class needed
from POM.pages.login_page import LoginPage
from POM.pages.zen_portal_base_page import BasePage
from POM.test.test_forgot_password import spreadsheet
from POM.utils.read_spreadsheet import Spreadsheet

# Passing the wrong credentials
spreadsheets=Spreadsheet()
data=spreadsheet.read_unsuccessful_login()
#Marking the test as negative
@pytest.mark.negative
@pytest.mark.parametrize("email_data,password_data",data)
def test_all_elements(driver,email_data,password_data):
    base_page=BasePage(driver)
    base_page.zen_portal_url()
    login_page=LoginPage(driver)
    login_page.email_input(email_data)
    login_page.password_input(password_data)
    login_page.remember_me()
    login_page.login_button()
    time.sleep(5)
    try:
        email = driver.find_element(By.XPATH, "//p[@id=':r0:-helper-text']")   # locating the email error
        email_error_displayed = email.is_displayed()
        email_error = email.text
    except NoSuchElementException:
        email_error_displayed = False
        email_error = ""
        print(f"Email Error not found")
    try:
        password = driver.find_element(By.XPATH, "//p[@id=':r1:-helper-text']")  #locating the password error
        password_error_displayed = password.is_displayed()
        password_error = password.text
    except NoSuchElementException:
        password_error_displayed = False
        password_error = ""
        print(f"Password Error not found")

    if email_error_displayed and password_error_displayed:    # Using If statement to find error position
        print(f"{email_error},{password_error}")
    elif email_error_displayed:
        print(f"{email_error}")
    elif password_error_displayed:
        print(f"{password_error}")









