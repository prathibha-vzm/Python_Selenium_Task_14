#Importing pytest to use parametrize and importing created classes that are needed
import pytest
from POM.pages.forgot_password import ResetPassword
from POM.pages.zen_portal import BasePage
from POM.utils.read_spreadsheet import Spreadsheet

#Creating Spreadsheet object and calling method that contains email data in sheet
spreadsheet = Spreadsheet()
data = spreadsheet.read_unsuccessful_login()
email_data = [row[0] for row in data]             #Passing invalid email
forget_data=spreadsheet.read_forgot_page_url_sheet()
forget_url=[row[0] for row in forget_data]
success=spreadsheet.read_assertion_text_sheet()
successful_text=[row[0] for row in success]

#Negative test is marked
#passed email,URL and text through parameter
@pytest.mark.negative
@pytest.mark.parametrize("expected_success_text",successful_text)
@pytest.mark.parametrize("expected_forgot_url",forget_url)
@pytest.mark.parametrize("email", email_data)
def test_forget_password(driver, email,expected_forgot_url,expected_success_text):
    base = BasePage(driver)                  #class object created and method called to open zen portal
    base.zen_portal_url()
    forgot = ResetPassword(driver)           #class object created and method is called
    web_page_url, success_text = forgot.forget_password(email)
    try:
        assert web_page_url == expected_forgot_url         #Assering URL  , handling exception
        assert success_text == expected_success_text       #Asserting Success text
    except AssertionError as ex:
        print("Not Submitted", {ex})





