import pytest #Imported Pytest
# Imported class files
from POM.pages.error_message_page import Error
from POM.pages.forgot_password_page import ResetPassword
from POM.pages.login_page import LoginPage
from POM.pages.logout_page import Logout
from POM.pages.zen_portal_base_page import BasePage
from POM.utils.read_spreadsheet import Spreadsheet
# To read the username and password from spreadsheet
spreadsheet=Spreadsheet()
data=spreadsheet.read_sheet()
test_data = list(zip([row[0] for row in data], [row[1] for row in data]))
email=[row[0] for row in data]

# This is to read the Url from sheet
asserted=spreadsheet.read_assertion_url_sheet()
assert_data=[row[0] for row in asserted]

#passed the sheet data through parameters
@pytest.mark.sanity
@pytest.mark.parametrize("email_reset",email)
@pytest.mark.parametrize("expected_url",assert_data)
@pytest.mark.parametrize("email_data,password_data",test_data)
def test_all(driver, email_data, password_data,expected_url,email_reset):
    base_obj=BasePage(driver)
    base_obj.zen_portal_url()
    login_obj=LoginPage(driver)
    login_obj.email_input(email_data)
    login_obj.password_input(password_data)
    login_obj.login_button()
    dashboard_url = driver.current_url
    if dashboard_url==expected_url:  #validating the login and next step to logout from the page
        logout_obj=Logout(driver)
        login_url=logout_obj.logout()
        print(login_url)
    else:                            #If login failed the error message will execute
        error_obj=Error(driver)
        error_obj.error_text()
        forgot_obj=ResetPassword(driver)
        success_txt=forgot_obj.forget_password(email_reset)
        print(success_txt)



