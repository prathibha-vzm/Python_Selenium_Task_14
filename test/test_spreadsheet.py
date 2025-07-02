from POM.utils.read_spreadsheet import Spreadsheet
#Importing the spreadsheet to test

# This tests the valid email and password
def test_spreadsheet():
    spreadsheet_obj=Spreadsheet()
    data=spreadsheet_obj.read_sheet()

    for rows in data:
        email_data=rows[0]
        password_data=rows[1]
        print(f"\n{email_data}--{password_data}")

#This tests the Invalid Credentials
def test_unsuccessful_login():
    spreadsheets=Spreadsheet()
    data=spreadsheets.read_unsuccessful_login()

    for rows in data:
        valid_email_data=rows[0]
        print(valid_email_data)

#This is to test the Login URL
def test_assertion_url():
    spreadsheets = Spreadsheet()
    data = spreadsheets.read_assertion_url_sheet()

    for rows in data:
        assert_url = rows[0]
        print(assert_url)

# This is to test the logout URL
def test_logout_url():
    sheet_obj=Spreadsheet()
    data=sheet_obj.read_logout_assertion_url()
    # To access as string
    for row in data:
        logout_url=row[0]
        print(logout_url)

# This is to test the valid email and empty password
def test_missing_password():
    sheet_obj=Spreadsheet()
    data=sheet_obj.read_unsuccessful_password_login()

    for row in data:
        miss_pwd=row[0]
        print(miss_pwd)

# This is to test the success test that comes after forgot link and sending valid email
def test_email_sent_text():
    sheet_obj=Spreadsheet()
    data=sheet_obj.read_assertion_text_sheet()

    for row in data:
        text=row[0]
        print(text)