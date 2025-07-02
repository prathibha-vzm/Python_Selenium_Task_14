import pytest # to use fixture
from selenium import webdriver #To access chrome

@pytest.fixture()
def driver():
    option=webdriver.ChromeOptions()
    option.add_argument("--disable-notifications")  #To disable notification in address bar
    driver=webdriver.Chrome(option)  #calling option in driver
    driver.maximize_window()   #to maximize window
    return driver

#To close the webpage autouse get called automatically
@pytest.fixture(autouse=True)
def tear_down(driver):
    yield
    driver.quit()
