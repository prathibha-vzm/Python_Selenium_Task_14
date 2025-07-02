import pyexcel_ods3 # To access spreadsheet
#To fetch the data from sheet
class Spreadsheet:
    #storing the file path
    def __init__(self):
        self.file_name="C:/Users/91956/Desktop/Prathibha/Guvi/selenium/test_data_zen_portal.ods"
    #This sheet contains valid/successful login credentials
    def read_sheet(self):
        read_data=pyexcel_ods3.get_data(self.file_name)
        sheet=read_data.get("credentials",[])
        row=sheet[1:]
        return row
    #This page contains Dashboard URL to confirm the successful login
    def read_assertion_url_sheet(self):
        read_data = pyexcel_ods3.get_data(self.file_name)
        sheet = read_data.get("assertion_url", [])
        row_url = sheet[1:]
        return row_url
    #This sheet contains URL of forgot password page, to assert when the forgot password link got opened
    def read_forgot_page_url_sheet(self):
        read_data = pyexcel_ods3.get_data(self.file_name)
        sheet = read_data.get("forgot_url", [])
        row_url = sheet[1:]
        return row_url

    # To assert the email sent text
    def read_assertion_text_sheet(self):
        read_data = pyexcel_ods3.get_data(self.file_name)
        sheet = read_data.get("assertion_text", [])
        row_text = sheet[1:]
        return row_text

    # This sheet contains wrong credentials to assert unsuccessful login
    def read_unsuccessful_login(self):
        read_data=pyexcel_ods3.get_data(self.file_name)
        sheet=read_data.get("unsuccessful",[])
        row_login=sheet[1:]
        return row_login

    # This sheet contains URL of Login page, which helps to assert when the page is successfully logged out and go back to login page
    def read_logout_assertion_url(self):
        read_url=pyexcel_ods3.get_data(self.file_name)
        sheet=read_url.get("logout_assertion",[])
        row_logout=sheet[1:]
        return row_logout

    #This sheet contains only email and empty password field
    def read_unsuccessful_password_login(self):
        read_data=pyexcel_ods3.get_data(self.file_name)
        sheet=read_data.get("unsuccessful_pwd",[])
        row_pwd=sheet[1:]
        return row_pwd
