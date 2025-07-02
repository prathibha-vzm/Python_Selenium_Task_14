#This is the base page or login page URL
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def zen_portal_url(self):
        self.driver.get("https://v2.zenclass.in/login")