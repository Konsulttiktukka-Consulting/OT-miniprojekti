from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

@given('I am at the start page')
def step_impl(context):
    driver.get('http://localhost:5000/')

@given('I am at the add video page')
def step_impl(context):
    driver.get('http://localhost:5000/videos/new/')
    
@when('I enter a valid youtube url and submit the form')
def step_impl(context): 
    urlform = driver.find_element_by_id("url")
    urlform.send_keys("https://www.youtube.com/watch?v=5jKZ9KGtee0")  
    elem = driver.find_element_by_name("addButton")
    elem.click()
       
@when('I click the video list button')
def step_impl(context):
    elem = driver.find_element_by_name("all videos")
    elem.click()

@when('I click the add video button')
def step_impl(context):
    elem = driver.find_element_by_name("add video")
    elem.click()
       
@then('The video is added and shown in the video list')
def step_impl(context):
    elem = driver.find_element_by_name("all videos")
    elem.click()
    assert ('SQUISH THAT CAT' in driver.page_source)
    
@then('I am shown a form to add a video')
def step_impl(context):
    assert driver.current_url == 'http://localhost:5000/videos/new/'
    assert ('Add a new video' in driver.page_source)
    assert ('Video URL' in driver.page_source)

@then('I am shown a list containing all videos')
def step_impl(context):
    assert driver.current_url == 'http://localhost:5000/videos'

@then('I can see a button to remove a video from the list')
def step_impl(context):
    assert ('remove video' in driver.page_source)
    elem = driver.find_element_by_name("delete")
    elem.click()
