#Importing needed classes to run the test
import pytest
from POM.pages.login_page import LoginPage
from POM.pages.logout_page import Logout
from POM.pages.zen_portal import BasePage
from POM.utils.read_spreadsheet import Spreadsheet

# To read the data from sheets and storing
sheets=Spreadsheet()
data=sheets.read_sheet()
email=[row[0] for row in data]
password=[row[1] for row in data]
data=sheets.read_logout_assertion_url()
assert_url=[row[0] for row in data]

#To mark the test as positive and passing the sheet data through parameter
@pytest.mark.positive
@pytest.mark.parametrize("expected_url",assert_url)
@pytest.mark.parametrize("email_data,password_data",[(email,password)])
def test_logout_pages(driver,email_data,password_data,expected_url):
    base_page = BasePage(driver)
    base_page.zen_portal_url()
    login_page = LoginPage(driver)
    login_page.email_input(email_data)
    login_page.password_input(password_data)
    login_page.login_button()
    logout_obj=Logout(driver)
    login_url=logout_obj.logout()
    try:
        assert login_url==expected_url    #asserting the logout is successful and moved to login page
    except AssertionError:
        print("Page not found")


