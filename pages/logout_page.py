#importing time, wait and by
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#This class will click on logout and go back to login page
class Logout:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.down_arrow=(By.XPATH,"//img[@id='profile-click-icon']")
        self.drop_down=(By.XPATH,"//div[text()='Log out']")
    #Here taking screenshots to verify the process
    def logout(self):
        profile_click = self.wait.until(expected_conditions.visibility_of_element_located(self.down_arrow))
        profile_click.click()
        logout_drop_down = self.wait.until(expected_conditions.visibility_of_element_located(self.drop_down))
        time.sleep(5)
        self.driver.save_screenshot("C:/Users/91956/PycharmProjects/PythonProject5/POM/reports/dashboard.png")
        logout_drop_down.click()
        time.sleep(5)
        login_url = self.driver.current_url
        self.driver.save_screenshot("C:/Users/91956/PycharmProjects/PythonProject5/POM/reports/logging_out.png")
        return login_url

