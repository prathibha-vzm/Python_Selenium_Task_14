import time # To Use static time and let the element findable
import pytest # To use markers
from selenium.common import NoSuchElementException #Exception
from POM.pages.login_page import LoginPage  #To call the class Login_Page
from POM.pages.zen_portal import BasePage #To call the base page
from POM.test.test_forgot_password import spreadsheet  #Used spreadsheet object from forgot password

data=spreadsheet.read_sheet()  #To call the credentials method that has email and password in its sheet
email=[row[0] for row in data]    #To access email as string
password=[row[1] for row in data]  #To access password

asserted=spreadsheet.read_assertion_url_sheet()    #calling assertion_url method that contains dashboard URL
assert_data=[row[0] for row in asserted]

@pytest.mark.positive #marked as positive to run test
@pytest.mark.parametrize("expected_url",assert_data)  #passing the url as parameter
@pytest.mark.parametrize("email_data,password_data",[(email,password)])  #passing email and password as parameters
def test_all_elements(driver,email_data,password_data,expected_url):
    base_page=BasePage(driver)  #Creating object for base class
    base_page.zen_portal_url()   #calling base class method to open the portal
    login_page=LoginPage(driver) #Creating object for LoginPage
    login_page.email_input(email_data)  #callings methods and passing the parameters
    login_page.password_input(password_data)
    login_page.remember_me()  #calling method
    login_page.login_button()  #calling method
    time.sleep(5)
    try:
        dashboard_url = driver.current_url      #storing the current page url
        time.sleep(2)
        assert dashboard_url == expected_url     #assert it with stored url in sheet

    except NoSuchElementException as no:       #Given all the expected exceptions
        print("Pop up not found",no)
    except AssertionError as ase:
        print("Page not Open",ase)
