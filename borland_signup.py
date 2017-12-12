import xlrd
from behave import *
import time
from environment import *
from selenium.webdriver.support.ui import Select

use_step_matcher("re")

wb = xlrd.open_workbook('./AutomationTestData.xlsx')
ws = wb.sheet_by_name("Signup")


baseUrl = "https://demo.borland.com/InsuranceWebExtJS/index.jsf"


@given("User opens Borland website")
def step_impl(context):
    browser.get('http://demo.borland.com/InsuranceWebExtJS/index.jsf')


@then("print the title")
def step_impl(context):
    title = browser.title
    print("\n Website title is " + str(title))


@step("Signup option is available")
def step_impl(context):
    try:
        assert True
        assert browser.find_element_by_id("login-form:signup")
        print("\n Signup option available")
    except AssertionError:
        print("\n Signup option not available")


for row in range(1, ws.nrows):
    print("\n" + str(ws.cell(row, 4).value))
    if ws.cell(row, 0) == xlrd.XL_CELL_EMPTY:
        print("\n break")
        break
    else:
        # Scenario 2: User navigates to Sign up page
        @given("User is on borland home page")
        def step_impl(context):
            try:
                assert True
                assert browser.title == "InsuranceWeb: Home"
                print("\n user is on home page")
            except AssertionError:
                print("\n Fail to open borland home page")
                pass


        @when("User selects Sign up option")
        def step_impl(context):
            try:
                assert True
                assert browser.find_element_by_name("login-form:signup")
                signupbutton = browser.find_element_by_name("login-form:signup")
                signupbutton.click()
            except AssertionError:
                print("\n Signup option not available")
                exit(1)


        @then("User should see Sign up page")
        def step_impl(context):
            try:
                assert True
                assert "Sign up" in browser.title
                print("\n Sign up page loaded")
            except AssertionError:
                print("\n Error while loading Sign up page")
                exit(1)


        # Scenario 2: User enters account information
        @given("User is on Sign up page")
        def step_impl(context):
            try:
                assert True
                assert "Sign up" in browser.title
                print("\n user is on sign up page")
            except AssertionError:
                print("\n Error on Sign up page")


        @when("User enters First Name")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 1) != xlrd.XL_CELL_EMPTY
                firstname = ws.cell(row, 1).value
                print("\n first name: " + str(firstname))
                fname = browser.find_element_by_id("signup:fname")
                fname.send_keys(firstname)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid first name")
                pass


        @step("User enters Last Name")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 2) != xlrd.XL_CELL_EMPTY
                lastname = ws.cell(row, 2).value
                print("\n last name: " + str(lastname))
                lname = browser.find_element_by_id("signup:lname")
                lname.send_keys(lastname)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid last name")
                pass


        @step("User enters Birthdate")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 3) != xlrd.XL_CELL_EMPTY
                birthdate = ws.cell(row, 3).value
                print("\n Birth date: " + str(birthdate))
                bdate = browser.find_element_by_id("BirthDate")
                bdate.send_keys(birthdate)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid Birth date")
                pass


        @step("User enters Email address")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 4) != xlrd.XL_CELL_EMPTY
                emailid = ws.cell(row, 4).value
                print("\n emailid: " + str(emailid))
                emailfield = browser.find_element_by_id("signup:email")
                emailfield.send_keys(emailid)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid email")
                pass


        @step("User enters Mailing address")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 5) != xlrd.XL_CELL_EMPTY
                mailingaddr = ws.cell(row, 5).value
                print("\n Mailing Address: " + str(mailingaddr))
                streetfield = browser.find_element_by_id("signup:street")
                streetfield.send_keys(mailingaddr)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid mailing address")
                pass


        @step("User enters City")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 6) != xlrd.XL_CELL_EMPTY
                city = ws.cell(row, 6).value
                print("\n City: " + str(city))
                cityfield = browser.find_element_by_id("signup:city")
                cityfield.send_keys(city)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid City")
                pass


        @step("User selects State")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 7) != xlrd.XL_CELL_EMPTY
                state = ws.cell(row, 7).value
                print("\n State: " + str(state))
                stateselect = Select(browser.find_element_by_id('signup:state'))
                stateselect.select_by_visible_text(state)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid State")
                pass


        @step("User enters Postal code")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 8) != xlrd.XL_CELL_EMPTY
                postcode = ws.cell(row, 8).value
                print("\n Post code: " + str(postcode))
                postcodefield = browser.find_element_by_id("signup:zip")
                postcodefield.send_keys(postcode)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid Postal code")
                pass


        @step("User enters password")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 9) != xlrd.XL_CELL_EMPTY
                password = ws.cell(row, 9).value
                print("\n Password: ")
                passfield = browser.find_element_by_id("signup:password")
                passfield.send_keys(password)
                time.sleep(1)
            except AssertionError:
                print("\n Invalid Postal code")
                pass


        @step("User clicks SIGN UP button")
        def step_impl(context):
            try:
                assert True
                assert browser.find_element_by_name("signup:signup")
                signupbutton = browser.find_element_by_name("signup:signup")
                signupbutton.click()
                time.sleep(1)
            except AssertionError:
                print("\n Error while signing up")
                exit(1)


        @then("User should be signed up successfully")
        def step_impl(context):
            try:
                assert True
                assert "Account Details" in browser.title
                assert browser.find_element_by_id("signup:continue")
                print("\n User registered successfully")
            except AssertionError:
                print("\n Error while signing in")


        time.sleep(1)
