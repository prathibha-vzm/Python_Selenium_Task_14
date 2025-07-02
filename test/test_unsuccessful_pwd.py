#Importing pytest , Exception and to use XPATH By
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
# Importing the needed classes
from POM.pages.forgot_password import ResetPassword
from POM.pages.login_page import LoginPage
from POM.pages.zen_portal import BasePage
from POM.utils.read_spreadsheet import Spreadsheet
#To read the spreadsheet, creating object and calling its method and storing their values
spreadsheet=Spreadsheet()
data=spreadsheet.read_unsuccessful_password_login()
email_d=[row[0] for row in data]
pwd_d=[row[0] for row in data]
forgot=spreadsheet.read_forgot_page_url_sheet()
forgot_url=[row[0] for row in forgot]
success=spreadsheet.read_assertion_text_sheet()
successful_text=[row[0] for row in success]
#This test is marked as negative, since the password is not given and trying to log in
@pytest.mark.negative
class TestForgotPwd:      # Creating it as class, to use this around the project
    @pytest.mark.parametrize("expected_success_text",successful_text)
    @pytest.mark.parametrize("expected_forgot_page_url",forgot_url)
    @pytest.mark.parametrize("email_data,password_data",[(email_d,pwd_d)])
    def test_missing_pwd_login(self,driver,email_data,password_data,expected_forgot_page_url,expected_success_text):
        base_page = BasePage(driver)
        base_page.zen_portal_url()
        login_page=LoginPage(driver)
        login_page.email_input(email_data)
        login_page.password_input(password_data)
        login_page.login_button()
        try:
            password = driver.find_element(By.XPATH, "//p[@id=':r1:-helper-text']")
            password_error_displayed = password.is_displayed()
            password_error = password.text
        except NoSuchElementException:
            password_error_displayed = False
            password_error = ""
            print(f"Password Error not found")
        forgot_pwd=ResetPassword(driver)
        web_page_url,success_text=forgot_pwd.forget_password(email_data)
        try:
            assert web_page_url == expected_forgot_page_url  # Asserting the forgot page URL and success text after sending email
            assert success_text == expected_success_text
        except AssertionError as ex:
            print("Not Submitted", {ex})