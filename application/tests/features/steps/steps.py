from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)

@given('I am at the start page')
def step_impl(context):
    driver.get('https://www.google.com/')

@when('I click the book list')
def step_impl(context):
    elem = driver.find_element_by_name("See all books")
    elem.click()

@then('I am shown a list containing all books')
def step_impl(context):
    print("789")
