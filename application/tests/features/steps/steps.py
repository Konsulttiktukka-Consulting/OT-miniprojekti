from behave import *
from selenium import webdriver
driver = webdriver.Chrome()

@given('I am at the start page')
def step_impl(context):
    driver.get('http://localhost:5000/')

@when('I click the book list')
def step_impl(context):
    elem = driver.find_element_by_name("all books")
    elem.click()

@then('I am shown a list containing all books')
def step_impl(context):
    assert driver.current_url == 'http://localhost:5000/books'
