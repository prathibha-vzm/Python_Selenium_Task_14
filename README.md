* This directory contains code to the webpage https://v2.zenclass.in/login
* Testing Architecture
* pytest, python selenium, explicit wait, exception conditions
* POM
  1. Pages - Added login page , loout, forgot password elements with locators, click and send_keys using explicit wait.
  2. Test - Tested those pages and passed the data by reading the spreadsheet and validation.
  3. utils - contains test_data for the script and reading the spreadsheet data's.
  4. report - contains the HTML report for the test cases.
  5. screenshot - stores the screenshot taken during test run.
* conftest is to set the environment to run the test, to end the test and generate report with screenshot.
* pytest.ini to mark the test run.
